"""
This type stub file was generated by pyright.
"""

import requests
from typing import TYPE_CHECKING, Tuple
from .cloud import AWSIoT, SesameCloud
from .const import AuthType

if TYPE_CHECKING:
    ...
class WebAPIAuth(requests.auth.AuthBase):
    def __init__(self, apikey: str) -> None:
        """Generic Implementation for Web API Authentication.

        Args:
            apikey (str): API Key
        """
        ...
    
    @property
    def login_method(self) -> AuthType:
        """Return a login method of this authentication.

        Returns:
            AuthType: `WebAPI` or `SDK`
        """
        ...
    
    @property
    def sesame_cloud(self) -> SesameCloud:
        ...
    
    @property
    def aws_iot(self):
        ...
    
    def __call__(self, request: requests.models.PreparedRequest) -> requests.models.PreparedRequest:
        """Function to transform HTTP request with `requests.Request`.

        This function aims to be called during request setup.

        Args:
            request (requests.models.PreparedRequest): The HTTP request to be transformed.
        """
        ...
    


class CognitoAuth:
    def __init__(self, apikey: str, client_id: str = ...) -> None:
        """Generic Implementation for Cognito Authentication.

        Args:
            apikey (str): API Key
            client_id (str): Client ID (Optional)
        """
        ...
    
    @property
    def login_method(self) -> AuthType:
        """Return a login method of this authentication.

        Returns:
            AuthType: `WebAPI` or `SDK`
        """
        ...
    
    @property
    def sesame_cloud(self) -> SesameCloud:
        ...
    
    @property
    def aws_iot(self) -> AWSIoT:
        ...
    
    @property
    def client_id(self) -> str:
        """Return a client id.

        Returns:
            str: Client ID
        """
        ...
    
    def authenticate(self) -> Tuple[str, str, str]:
        """Authenticate and get a credential from AWS Cognito.

        Returns:
            Tuple[str, str, str]: `access_key_id`, `secret_key` and `session_token`
        """
        ...
    
    def iot_websocket_handshake_transform(self, transform_args: mqtt.WebsocketHandshakeTransformArgs) -> None:
        """Function to transform websocket handshake request within `awscrt.mqtt.Connection`.

        This function aims to be called each time a websocket connection is attempted.

        Args:
            transform_args (mqtt.WebsocketHandshakeTransformArgs): Contains HTTP request to be transformed. The function calls `transform_args.done()` when complete.
        """
        ...
    
    def __call__(self, request: requests.models.PreparedRequest) -> requests.models.PreparedRequest:
        """Function to transform HTTP request with `requests.Request`.

        This function aims to be called during request setup.

        Args:
            request (requests.models.PreparedRequest): The HTTP request to be transformed.
        """
        ...
    


