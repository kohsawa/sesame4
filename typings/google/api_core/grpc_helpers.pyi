"""
This type stub file was generated by pyright.
"""

import grpc

"""Helpers for :mod:`grpc`."""
_STREAM_WRAP_CLASSES = ...
class _StreamingResponseIterator(grpc.Call):
    def __init__(self, wrapped, prefetch_first_result=...) -> None:
        ...
    
    def __iter__(self): # -> Self@_StreamingResponseIterator:
        """This iterator is also an iterable that returns itself."""
        ...
    
    def __next__(self):
        """Get the next response from the stream.

        Returns:
            protobuf.Message: A single response from the stream.
        """
        ...
    
    def add_callback(self, callback):
        ...
    
    def cancel(self):
        ...
    
    def code(self):
        ...
    
    def details(self):
        ...
    
    def initial_metadata(self):
        ...
    
    def is_active(self):
        ...
    
    def time_remaining(self):
        ...
    
    def trailing_metadata(self):
        ...
    


def wrap_errors(callable_): # -> (*args: Unknown, **kwargs: Unknown) -> _StreamingResponseIterator:
    """Wrap a gRPC callable and map :class:`grpc.RpcErrors` to friendly error
    classes.

    Errors raised by the gRPC callable are mapped to the appropriate
    :class:`google.api_core.exceptions.GoogleAPICallError` subclasses.
    The original `grpc.RpcError` (which is usually also a `grpc.Call`) is
    available from the ``response`` property on the mapped exception. This
    is useful for extracting metadata from the original error.

    Args:
        callable_ (Callable): A gRPC callable.

    Returns:
        Callable: The wrapped gRPC callable.
    """
    ...

def create_channel(target, credentials=..., scopes=..., ssl_credentials=..., credentials_file=..., quota_project_id=..., default_scopes=..., default_host=..., **kwargs):
    """Create a secure channel with credentials.

    Args:
        target (str): The target service address in the format 'hostname:port'.
        credentials (google.auth.credentials.Credentials): The credentials. If
            not specified, then this function will attempt to ascertain the
            credentials from the environment using :func:`google.auth.default`.
        scopes (Sequence[str]): A optional list of scopes needed for this
            service. These are only used when credentials are not specified and
            are passed to :func:`google.auth.default`.
        ssl_credentials (grpc.ChannelCredentials): Optional SSL channel
            credentials. This can be used to specify different certificates.
        credentials_file (str): A file with credentials that can be loaded with
            :func:`google.auth.load_credentials_from_file`. This argument is
            mutually exclusive with credentials.
        quota_project_id (str): An optional project to use for billing and quota.
        default_scopes (Sequence[str]): Default scopes passed by a Google client
            library. Use 'scopes' for user-defined scopes.
        default_host (str): The default endpoint. e.g., "pubsub.googleapis.com".
        kwargs: Additional key-word args passed to :func:`grpc.secure_channel`.

    Returns:
        grpc.Channel: The created channel.

    Raises:
        google.api_core.DuplicateCredentialArgs: If both a credentials object and credentials_file are passed.
    """
    ...

_MethodCall = ...
_ChannelRequest = ...
class _CallableStub:
    """Stub for the grpc.*MultiCallable interfaces."""
    def __init__(self, method, channel) -> None:
        ...
    
    def __call__(self, request, timeout=..., metadata=..., credentials=...):
        ...
    


class ChannelStub(grpc.Channel):
    """A testing stub for the grpc.Channel interface.

    This can be used to test any client that eventually uses a gRPC channel
    to communicate. By passing in a channel stub, you can configure which
    responses are returned and track which requests are made.

    For example:

    .. code-block:: python

        channel_stub = grpc_helpers.ChannelStub()
        client = FooClient(channel=channel_stub)

        channel_stub.GetFoo.response = foo_pb2.Foo(name='bar')

        foo = client.get_foo(labels=['baz'])

        assert foo.name == 'bar'
        assert channel_stub.GetFoo.requests[0].labels = ['baz']

    Each method on the stub can be accessed and configured on the channel.
    Here's some examples of various configurations:

    .. code-block:: python

        # Return a basic response:

        channel_stub.GetFoo.response = foo_pb2.Foo(name='bar')
        assert client.get_foo().name == 'bar'

        # Raise an exception:
        channel_stub.GetFoo.response = NotFound('...')

        with pytest.raises(NotFound):
            client.get_foo()

        # Use a sequence of responses:
        channel_stub.GetFoo.responses = iter([
            foo_pb2.Foo(name='bar'),
            foo_pb2.Foo(name='baz'),
        ])

        assert client.get_foo().name == 'bar'
        assert client.get_foo().name == 'baz'

        # Use a callable

        def on_get_foo(request):
            return foo_pb2.Foo(name='bar' + request.id)

        channel_stub.GetFoo.response = on_get_foo

        assert client.get_foo(id='123').name == 'bar123'
    """
    def __init__(self, responses=...) -> None:
        ...
    
    def __getattr__(self, key):
        ...
    
    def unary_unary(self, method, request_serializer=..., response_deserializer=...):
        """grpc.Channel.unary_unary implementation."""
        ...
    
    def unary_stream(self, method, request_serializer=..., response_deserializer=...):
        """grpc.Channel.unary_stream implementation."""
        ...
    
    def stream_unary(self, method, request_serializer=..., response_deserializer=...):
        """grpc.Channel.stream_unary implementation."""
        ...
    
    def stream_stream(self, method, request_serializer=..., response_deserializer=...):
        """grpc.Channel.stream_stream implementation."""
        ...
    
    def subscribe(self, callback, try_to_connect=...): # -> None:
        """grpc.Channel.subscribe implementation."""
        ...
    
    def unsubscribe(self, callback): # -> None:
        """grpc.Channel.unsubscribe implementation."""
        ...
    
    def close(self): # -> None:
        """grpc.Channel.close implementation."""
        ...
    

