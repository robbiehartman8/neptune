# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import identity_pb2 as identity__pb2


class IdentityStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getIdentity = channel.unary_unary(
                '/Identity/getIdentity',
                request_serializer=identity__pb2.hrData.SerializeToString,
                response_deserializer=identity__pb2.iamData.FromString,
                )
        self.enterIdentity = channel.unary_unary(
                '/Identity/enterIdentity',
                request_serializer=identity__pb2.hrData.SerializeToString,
                response_deserializer=identity__pb2.iamData.FromString,
                )


class IdentityServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enterIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.getIdentity,
                    request_deserializer=identity__pb2.hrData.FromString,
                    response_serializer=identity__pb2.iamData.SerializeToString,
            ),
            'enterIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.enterIdentity,
                    request_deserializer=identity__pb2.hrData.FromString,
                    response_serializer=identity__pb2.iamData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Identity', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Identity(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/getIdentity',
            identity__pb2.hrData.SerializeToString,
            identity__pb2.iamData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def enterIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Identity/enterIdentity',
            identity__pb2.hrData.SerializeToString,
            identity__pb2.iamData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
