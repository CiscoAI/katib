from pkg.suggestion.NAS_Reinforcement_Learning.Controller import Controller
from pkg.suggestion.NAS_Reinforcement_Learning.Operation import SearchSpace
from pkg.suggestion.NAS_Reinforcement_Learning.SuggestionParam import parseSuggestionParam
import tensorflow as tf
import yaml
import random


class NAS_RL_Service(object):
    def __init__(self):
        self._get_suggestion_param()
        self._get_search_space()

        self.tf_graph = tf.get_default_graph()
        self.is_first_run = True

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

    def GetSuggestions(self):
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

        return arc

    def GetEvaluationResult(self):
        # fake results

        return random.uniform(0, 1)

    def _get_search_space(self):

        # this function need to
        # 1) get the number of layers
        # 2) get the I/O size
        # 2) get the available operations

        # for local testing only. Will retrieve parameters from grpc server in Katib
        with open("../nas_reinforcement_learning.yaml", 'r') as stream:
            try:
                studyjob = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        self.num_layers = int(studyjob["spec"]['graphconfig']['num_layers'])
        self.input_size = list(map(int, studyjob["spec"]['graphconfig']['input_size']))
        self.output_size = list(map(int, studyjob["spec"]['graphconfig']['output_size']))

        search_space_raw = studyjob["spec"]["operations"]
        search_space_object = SearchSpace(search_space_raw)

        self.num_operations = search_space_object.num_operations
        print("There are", self.num_operations, "operations in total")

        self.search_space = search_space_object.search_space
        for opt in self.search_space:
            opt.print_op()
            print()

    def _get_suggestion_param(self):
        # for local testing only. Will retrieve parameters from grpc server in Katib
        with open("../nas_reinforcement_learning.yaml", 'r') as stream:
            try:
                studyjob = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        params_raw = studyjob['spec']['suggestionSpec']['suggestionParameters']
        suggestion_params = parseSuggestionParam(params_raw)

        print("=============== Parameters for LSTM Controller ===============")
        for spec in suggestion_params:
            print(spec, suggestion_params[spec])

        self.suggestion_config = suggestion_params


# for testing the NAS_RL_Service only
if __name__ == "__main__":
    testing_service = NAS_RL_Service()
    for i in range(10):
        candidate = testing_service.GetSuggestions()
        print(candidate)



