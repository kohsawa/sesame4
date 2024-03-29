"""
This type stub file was generated by pyright.
"""

from google.api_core import client_info

"""Helpers for providing client information.

Client information is used to send information about the calling client,
such as the library and Python version, to API services.
"""
METRICS_METADATA_KEY = ...
class ClientInfo(client_info.ClientInfo):
    """Client information used to generate a user-agent for API calls.

    This user-agent information is sent along with API calls to allow the
    receiving service to do analytics on which versions of Python and Google
    libraries are being used.

    Args:
        python_version (str): The Python interpreter version, for example,
            ``'3.9.6'``.
        grpc_version (Optional[str]): The gRPC library version.
        api_core_version (str): The google-api-core library version.
        gapic_version (Optional[str]): The sversion of gapic-generated client
            library, if the library was generated by gapic.
        client_library_version (Optional[str]): The version of the client
            library, generally used if the client library was not generated
            by gapic or if additional functionality was built on top of
            a gapic client library.
        user_agent (Optional[str]): Prefix to the user agent header. This is
            used to supply information such as application name or partner tool.
            Recommended format: ``application-or-tool-ID/major.minor.version``.
    """
    def to_grpc_metadata(self): # -> tuple[Literal['x-goog-api-client'], str]:
        """Returns the gRPC metadata for this client info."""
        ...
    


DEFAULT_CLIENT_INFO = ...
