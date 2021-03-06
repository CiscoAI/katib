# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import api_pb2 as api__pb2


class ManagerStub(object):
  """*
  Service for Main API for Katib
  For each RPC service, we define mapping to HTTP REST API method.
  The mapping includes the URL path, query parameters and request body.
  https://cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#http
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateStudy = channel.unary_unary(
        '/api.Manager/CreateStudy',
        request_serializer=api__pb2.CreateStudyRequest.SerializeToString,
        response_deserializer=api__pb2.CreateStudyReply.FromString,
        )
    self.GetStudy = channel.unary_unary(
        '/api.Manager/GetStudy',
        request_serializer=api__pb2.GetStudyRequest.SerializeToString,
        response_deserializer=api__pb2.GetStudyReply.FromString,
        )
    self.DeleteStudy = channel.unary_unary(
        '/api.Manager/DeleteStudy',
        request_serializer=api__pb2.DeleteStudyRequest.SerializeToString,
        response_deserializer=api__pb2.DeleteStudyReply.FromString,
        )
    self.GetStudyList = channel.unary_unary(
        '/api.Manager/GetStudyList',
        request_serializer=api__pb2.GetStudyListRequest.SerializeToString,
        response_deserializer=api__pb2.GetStudyListReply.FromString,
        )
    self.CreateTrial = channel.unary_unary(
        '/api.Manager/CreateTrial',
        request_serializer=api__pb2.CreateTrialRequest.SerializeToString,
        response_deserializer=api__pb2.CreateTrialReply.FromString,
        )
    self.GetTrials = channel.unary_unary(
        '/api.Manager/GetTrials',
        request_serializer=api__pb2.GetTrialsRequest.SerializeToString,
        response_deserializer=api__pb2.GetTrialsReply.FromString,
        )
    self.GetTrial = channel.unary_unary(
        '/api.Manager/GetTrial',
        request_serializer=api__pb2.GetTrialRequest.SerializeToString,
        response_deserializer=api__pb2.GetTrialReply.FromString,
        )
    self.RegisterWorker = channel.unary_unary(
        '/api.Manager/RegisterWorker',
        request_serializer=api__pb2.RegisterWorkerRequest.SerializeToString,
        response_deserializer=api__pb2.RegisterWorkerReply.FromString,
        )
    self.GetWorkers = channel.unary_unary(
        '/api.Manager/GetWorkers',
        request_serializer=api__pb2.GetWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetWorkersReply.FromString,
        )
    self.UpdateWorkerState = channel.unary_unary(
        '/api.Manager/UpdateWorkerState',
        request_serializer=api__pb2.UpdateWorkerStateRequest.SerializeToString,
        response_deserializer=api__pb2.UpdateWorkerStateReply.FromString,
        )
    self.GetWorkerFullInfo = channel.unary_unary(
        '/api.Manager/GetWorkerFullInfo',
        request_serializer=api__pb2.GetWorkerFullInfoRequest.SerializeToString,
        response_deserializer=api__pb2.GetWorkerFullInfoReply.FromString,
        )
    self.GetSuggestions = channel.unary_unary(
        '/api.Manager/GetSuggestions',
        request_serializer=api__pb2.GetSuggestionsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionsReply.FromString,
        )
    self.GetShouldStopWorkers = channel.unary_unary(
        '/api.Manager/GetShouldStopWorkers',
        request_serializer=api__pb2.GetShouldStopWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetShouldStopWorkersReply.FromString,
        )
    self.GetMetrics = channel.unary_unary(
        '/api.Manager/GetMetrics',
        request_serializer=api__pb2.GetMetricsRequest.SerializeToString,
        response_deserializer=api__pb2.GetMetricsReply.FromString,
        )
    self.SetSuggestionParameters = channel.unary_unary(
        '/api.Manager/SetSuggestionParameters',
        request_serializer=api__pb2.SetSuggestionParametersRequest.SerializeToString,
        response_deserializer=api__pb2.SetSuggestionParametersReply.FromString,
        )
    self.GetSuggestionParameters = channel.unary_unary(
        '/api.Manager/GetSuggestionParameters',
        request_serializer=api__pb2.GetSuggestionParametersRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionParametersReply.FromString,
        )
    self.GetSuggestionParameterList = channel.unary_unary(
        '/api.Manager/GetSuggestionParameterList',
        request_serializer=api__pb2.GetSuggestionParameterListRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionParameterListReply.FromString,
        )
    self.SetEarlyStoppingParameters = channel.unary_unary(
        '/api.Manager/SetEarlyStoppingParameters',
        request_serializer=api__pb2.SetEarlyStoppingParametersRequest.SerializeToString,
        response_deserializer=api__pb2.SetEarlyStoppingParametersReply.FromString,
        )
    self.GetEarlyStoppingParameters = channel.unary_unary(
        '/api.Manager/GetEarlyStoppingParameters',
        request_serializer=api__pb2.GetEarlyStoppingParametersRequest.SerializeToString,
        response_deserializer=api__pb2.GetEarlyStoppingParametersReply.FromString,
        )
    self.GetEarlyStoppingParameterList = channel.unary_unary(
        '/api.Manager/GetEarlyStoppingParameterList',
        request_serializer=api__pb2.GetEarlyStoppingParameterListRequest.SerializeToString,
        response_deserializer=api__pb2.GetEarlyStoppingParameterListReply.FromString,
        )
    self.SaveStudy = channel.unary_unary(
        '/api.Manager/SaveStudy',
        request_serializer=api__pb2.SaveStudyRequest.SerializeToString,
        response_deserializer=api__pb2.SaveStudyReply.FromString,
        )
    self.SaveModel = channel.unary_unary(
        '/api.Manager/SaveModel',
        request_serializer=api__pb2.SaveModelRequest.SerializeToString,
        response_deserializer=api__pb2.SaveModelReply.FromString,
        )
    self.ReportMetricsLogs = channel.unary_unary(
        '/api.Manager/ReportMetricsLogs',
        request_serializer=api__pb2.ReportMetricsLogsRequest.SerializeToString,
        response_deserializer=api__pb2.ReportMetricsLogsReply.FromString,
        )
    self.GetSavedStudies = channel.unary_unary(
        '/api.Manager/GetSavedStudies',
        request_serializer=api__pb2.GetSavedStudiesRequest.SerializeToString,
        response_deserializer=api__pb2.GetSavedStudiesReply.FromString,
        )
    self.GetSavedModels = channel.unary_unary(
        '/api.Manager/GetSavedModels',
        request_serializer=api__pb2.GetSavedModelsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSavedModelsReply.FromString,
        )


class ManagerServicer(object):
  """*
  Service for Main API for Katib
  For each RPC service, we define mapping to HTTP REST API method.
  The mapping includes the URL path, query parameters and request body.
  https://cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#http
  """

  def CreateStudy(self, request, context):
    """*
    Create a Study from Study Config.
    Generate a unique ID and store the Study to DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStudy(self, request, context):
    """* 
    Get a Study Config from DB by ID of Study.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteStudy(self, request, context):
    """* 
    Delete a Study from DB by Study ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStudyList(self, request, context):
    """*
    Get all Study Configs from DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTrial(self, request, context):
    """*
    Create a Trial from Trial Config.
    Generate a unique ID and store the Trial to DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrials(self, request, context):
    """* 
    Get a Trial Configs from DB by ID of Study.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrial(self, request, context):
    """*
    Get a Trial Configuration from DB by ID of Trial.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterWorker(self, request, context):
    """*
    Create a Worker from Worker Config.
    Generate a unique ID and store the Worker to DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkers(self, request, context):
    """* 
    Get a Worker Configs and Status from DB by ID of Study, Trial or Worker.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateWorkerState(self, request, context):
    """* 
    Update a Status of Worker.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetWorkerFullInfo(self, request, context):
    """* 
    Get full information related to specified Workers.
    It includes Worker Config, HyperParameters and Metrics Logs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestions(self, request, context):
    """* 
    Get Suggestions from a Suggestion service.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetShouldStopWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMetrics(self, request, context):
    """*
    Get metrics of workers.
    You can get all logs of metrics since start of the worker.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetSuggestionParameters(self, request, context):
    """*
    Create or Update parameter set for a suggestion service.
    If you specify an ID of parameter set, it will update the parameter set by your request.
    If you don't specify an ID, it will create a new parameter set for corresponding study and suggestion service.
    The parameters are key-value format.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestionParameters(self, request, context):
    """*
    Get suggestion parameter set from DB specified.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSuggestionParameterList(self, request, context):
    """*
    Get all suggestion parameter sets from DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetEarlyStoppingParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEarlyStoppingParameters(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEarlyStoppingParameterList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveStudy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReportMetricsLogs(self, request, context):
    """*
    Report a logs of metrics for workers.
    The logs for each worker must have timestamp and must be ordered in time series.
    When the log you reported are already reported before, it will be dismissed and get no error.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSavedStudies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSavedModels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateStudy': grpc.unary_unary_rpc_method_handler(
          servicer.CreateStudy,
          request_deserializer=api__pb2.CreateStudyRequest.FromString,
          response_serializer=api__pb2.CreateStudyReply.SerializeToString,
      ),
      'GetStudy': grpc.unary_unary_rpc_method_handler(
          servicer.GetStudy,
          request_deserializer=api__pb2.GetStudyRequest.FromString,
          response_serializer=api__pb2.GetStudyReply.SerializeToString,
      ),
      'DeleteStudy': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteStudy,
          request_deserializer=api__pb2.DeleteStudyRequest.FromString,
          response_serializer=api__pb2.DeleteStudyReply.SerializeToString,
      ),
      'GetStudyList': grpc.unary_unary_rpc_method_handler(
          servicer.GetStudyList,
          request_deserializer=api__pb2.GetStudyListRequest.FromString,
          response_serializer=api__pb2.GetStudyListReply.SerializeToString,
      ),
      'CreateTrial': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTrial,
          request_deserializer=api__pb2.CreateTrialRequest.FromString,
          response_serializer=api__pb2.CreateTrialReply.SerializeToString,
      ),
      'GetTrials': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrials,
          request_deserializer=api__pb2.GetTrialsRequest.FromString,
          response_serializer=api__pb2.GetTrialsReply.SerializeToString,
      ),
      'GetTrial': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrial,
          request_deserializer=api__pb2.GetTrialRequest.FromString,
          response_serializer=api__pb2.GetTrialReply.SerializeToString,
      ),
      'RegisterWorker': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterWorker,
          request_deserializer=api__pb2.RegisterWorkerRequest.FromString,
          response_serializer=api__pb2.RegisterWorkerReply.SerializeToString,
      ),
      'GetWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkers,
          request_deserializer=api__pb2.GetWorkersRequest.FromString,
          response_serializer=api__pb2.GetWorkersReply.SerializeToString,
      ),
      'UpdateWorkerState': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateWorkerState,
          request_deserializer=api__pb2.UpdateWorkerStateRequest.FromString,
          response_serializer=api__pb2.UpdateWorkerStateReply.SerializeToString,
      ),
      'GetWorkerFullInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetWorkerFullInfo,
          request_deserializer=api__pb2.GetWorkerFullInfoRequest.FromString,
          response_serializer=api__pb2.GetWorkerFullInfoReply.SerializeToString,
      ),
      'GetSuggestions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestions,
          request_deserializer=api__pb2.GetSuggestionsRequest.FromString,
          response_serializer=api__pb2.GetSuggestionsReply.SerializeToString,
      ),
      'GetShouldStopWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetShouldStopWorkers,
          request_deserializer=api__pb2.GetShouldStopWorkersRequest.FromString,
          response_serializer=api__pb2.GetShouldStopWorkersReply.SerializeToString,
      ),
      'GetMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.GetMetrics,
          request_deserializer=api__pb2.GetMetricsRequest.FromString,
          response_serializer=api__pb2.GetMetricsReply.SerializeToString,
      ),
      'SetSuggestionParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetSuggestionParameters,
          request_deserializer=api__pb2.SetSuggestionParametersRequest.FromString,
          response_serializer=api__pb2.SetSuggestionParametersReply.SerializeToString,
      ),
      'GetSuggestionParameters': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestionParameters,
          request_deserializer=api__pb2.GetSuggestionParametersRequest.FromString,
          response_serializer=api__pb2.GetSuggestionParametersReply.SerializeToString,
      ),
      'GetSuggestionParameterList': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestionParameterList,
          request_deserializer=api__pb2.GetSuggestionParameterListRequest.FromString,
          response_serializer=api__pb2.GetSuggestionParameterListReply.SerializeToString,
      ),
      'SetEarlyStoppingParameters': grpc.unary_unary_rpc_method_handler(
          servicer.SetEarlyStoppingParameters,
          request_deserializer=api__pb2.SetEarlyStoppingParametersRequest.FromString,
          response_serializer=api__pb2.SetEarlyStoppingParametersReply.SerializeToString,
      ),
      'GetEarlyStoppingParameters': grpc.unary_unary_rpc_method_handler(
          servicer.GetEarlyStoppingParameters,
          request_deserializer=api__pb2.GetEarlyStoppingParametersRequest.FromString,
          response_serializer=api__pb2.GetEarlyStoppingParametersReply.SerializeToString,
      ),
      'GetEarlyStoppingParameterList': grpc.unary_unary_rpc_method_handler(
          servicer.GetEarlyStoppingParameterList,
          request_deserializer=api__pb2.GetEarlyStoppingParameterListRequest.FromString,
          response_serializer=api__pb2.GetEarlyStoppingParameterListReply.SerializeToString,
      ),
      'SaveStudy': grpc.unary_unary_rpc_method_handler(
          servicer.SaveStudy,
          request_deserializer=api__pb2.SaveStudyRequest.FromString,
          response_serializer=api__pb2.SaveStudyReply.SerializeToString,
      ),
      'SaveModel': grpc.unary_unary_rpc_method_handler(
          servicer.SaveModel,
          request_deserializer=api__pb2.SaveModelRequest.FromString,
          response_serializer=api__pb2.SaveModelReply.SerializeToString,
      ),
      'ReportMetricsLogs': grpc.unary_unary_rpc_method_handler(
          servicer.ReportMetricsLogs,
          request_deserializer=api__pb2.ReportMetricsLogsRequest.FromString,
          response_serializer=api__pb2.ReportMetricsLogsReply.SerializeToString,
      ),
      'GetSavedStudies': grpc.unary_unary_rpc_method_handler(
          servicer.GetSavedStudies,
          request_deserializer=api__pb2.GetSavedStudiesRequest.FromString,
          response_serializer=api__pb2.GetSavedStudiesReply.SerializeToString,
      ),
      'GetSavedModels': grpc.unary_unary_rpc_method_handler(
          servicer.GetSavedModels,
          request_deserializer=api__pb2.GetSavedModelsRequest.FromString,
          response_serializer=api__pb2.GetSavedModelsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Manager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SuggestionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSuggestions = channel.unary_unary(
        '/api.Suggestion/GetSuggestions',
        request_serializer=api__pb2.GetSuggestionsRequest.SerializeToString,
        response_deserializer=api__pb2.GetSuggestionsReply.FromString,
        )


class SuggestionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetSuggestions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SuggestionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSuggestions': grpc.unary_unary_rpc_method_handler(
          servicer.GetSuggestions,
          request_deserializer=api__pb2.GetSuggestionsRequest.FromString,
          response_serializer=api__pb2.GetSuggestionsReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.Suggestion', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class EarlyStoppingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetShouldStopWorkers = channel.unary_unary(
        '/api.EarlyStopping/GetShouldStopWorkers',
        request_serializer=api__pb2.GetShouldStopWorkersRequest.SerializeToString,
        response_deserializer=api__pb2.GetShouldStopWorkersReply.FromString,
        )


class EarlyStoppingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetShouldStopWorkers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EarlyStoppingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetShouldStopWorkers': grpc.unary_unary_rpc_method_handler(
          servicer.GetShouldStopWorkers,
          request_deserializer=api__pb2.GetShouldStopWorkersRequest.FromString,
          response_serializer=api__pb2.GetShouldStopWorkersReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.EarlyStopping', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))