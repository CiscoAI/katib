from pkg.suggestion.NAS_Reinforcement_Learning.Controller import Controller
from pkg.suggestion.NAS_Reinforcement_Learning.Operation import SearchSpace
from pkg.suggestion.NAS_Reinforcement_Learning.SuggestionParam import parseSuggestionParam
import tensorflow as tf
import numpy as np
import random
import grpc
from pkg.api.python import api_pb2
from pkg.api.python import api_pb2_grpc
import logging
from logging import getLogger, StreamHandler, INFO, DEBUG


class NasrlService(api_pb2_grpc.SuggestionServicer):
    def __init__(self):
        self.manager_addr = "vizier-core"
        self.manager_port = 6789
        self.tf_graph = tf.get_default_graph()
        self.is_init = False
        self.is_first_run = True

    def init_controller(self, request):
        self._get_suggestion_param(request.param_id)
        self._get_search_space(request.study_id)

        with self.tf_graph.as_default():
            self.controller = Controller(
                num_layers=self.num_layers,
                num_operations=self.num_operations,
                lstm_size=self.suggestion_config['lstm_num_cells'],
                lstm_num_layers=self.suggestion_config['lstm_num_layers'],
                lstm_keep_prob=self.suggestion_config['lstm_keep_prob'],
                lr_init=self.suggestion_config['init_learning_rate'],
                lr_dec_start=self.suggestion_config['lr_decay_start'],
                lr_dec_every=self.suggestion_config['lr_decay_every'],
                lr_dec_rate=self.suggestion_config['lr_decay_rate'],
                l2_reg=self.suggestion_config['l2_reg'],
                entropy_weight=self.suggestion_config['entropy_weight'],
                bl_dec=self.suggestion_config['baseline_decay'],
                optim_algo=self.suggestion_config['optimizer'],
                skip_target=self.suggestion_config['skip-target'],
                skip_weight=self.suggestion_config['skip-weight'],
                name="controller")

            self.controller.build_trainer()
        
        self.is_init = True

    def GetSuggestions(self, request, context):
        trials = []

        if not self.is_init:
            self.init_controller(request)

        with self.tf_graph.as_default():

            saver = tf.train.Saver()

            controller_ops = {
                  "train_step": self.controller.train_step,
                  "loss": self.controller.loss,
                  "train_op": self.controller.train_op,
                  "lr": self.controller.lr,
                  "grad_norm": self.controller.grad_norm,
                  "optimizer": self.controller.optimizer,
                  "baseline": self.controller.baseline,
                  "entropy": self.controller.sample_entropy,
                  "sample_arc": self.controller.sample_arc,
                  "skip_rate": self.controller.skip_rate}

            run_ops = [
                controller_ops["loss"],
                controller_ops["entropy"],
                controller_ops["lr"],
                controller_ops["grad_norm"],
                controller_ops["baseline"],
                controller_ops["skip_rate"],
                controller_ops["train_op"]]

            if self.is_first_run:
                with tf.Session() as sess:
                    sess.run(tf.global_variables_initializer())
                    arc = sess.run(controller_ops["sample_arc"])
                    saver.save(sess, "ctrl_cache/controller.ckpt")

                self.is_first_run = False

            else:
                with tf.Session() as sess:
                    saver.restore(sess, "ctrl_cache/controller.ckpt")
                    valid_acc = self.controller.reward
                    result = self.GetEvaluationResult()
                    loss, entropy, lr, gn, bl, skip, _ = sess.run(
                        fetches=run_ops,
                        feed_dict={valid_acc: result})
                    arc = sess.run(controller_ops["sample_arc"])

                    saver.save(sess, "ctrl_cache/controller.ckpt")

        print(arc)
        
        return api_pb2.GetSuggestionsReply(trials=trials)

    def GetEvaluationResult(self):
        # fake results for tseting
        # will complete this part after training container is built and integrated
        return random.uniform(0, 1)

    def _get_search_space(self, studyID):

        # this function need to
        # 1) get the number of layers
        # 2) get the I/O size
        # 2) get the available operations

        channel = grpc.beta.implementations.insecure_channel(self.manager_addr, self.manager_port)
        with api_pb2.beta_create_Manager_stub(channel) as client:
            gsrep = client.GetStudy(api_pb2.GetStudyRequest(study_id=studyID, job_type="NAS"), 10)
        
        all_params = gsrep.study_config.nas_config
        graph_config = all_params.graph_config
        search_space_raw = all_params.operations

        self.num_layers = int(graph_config.num_layers)
        self.input_size = list(map(int, graph_config.input_size))
        self.output_size = list(map(int, graph_config.output_size))

        search_space_object = SearchSpace(search_space_raw)


        print("\n==================== Search Space ====================")
        self.num_operations = search_space_object.num_operations
        print("There are", self.num_operations, "operations in total")
        self.search_space = search_space_object.search_space
        for opt in self.search_space:
            opt.print_op()
            print()

    def _get_suggestion_param(self, paramID):
        channel = grpc.beta.implementations.insecure_channel(self.manager_addr, self.manager_port)
        with api_pb2.beta_create_Manager_stub(channel) as client:
            gsprep = client.GetSuggestionParameters(api_pb2.GetSuggestionParametersRequest(param_id=paramID), 10)
        
        params_raw = gsprep.suggestion_parameters

        suggestion_params = parseSuggestionParam(params_raw)

        print("\n=============== Parameters for LSTM Controller ===============")
        for spec in suggestion_params:
            print(spec, suggestion_params[spec])

        self.suggestion_config = suggestion_params




