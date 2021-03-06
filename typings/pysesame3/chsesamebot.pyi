"""
This type stub file was generated by pyright.
"""

from typing import Callable, List, Optional, TYPE_CHECKING, Union
from pysesame3.auth import CognitoAuth, WebAPIAuth
from pysesame3.const import CHSesame2ShadowStatus
from pysesame3.device import SesameLocker
from pysesame3.helper import CHSesameBotMechStatus
from pysesame3.history import CHSesame2History

if TYPE_CHECKING:
    ...
logger = ...
class CHSesameBot(SesameLocker):
    def __init__(self, authenticator: Union[WebAPIAuth, CognitoAuth], device_uuid: str, secret_key: str) -> None:
        """SESAME bot Device Specific Implementation.

        Args:
            authenticator (Union[WebAPIAuth, CognitoAuth]):
            device_uuid (str): The UUID of the device
            secret_key (str): The secret key of the device
        """
        ...
    
    @property
    def mechStatus(self) -> CHSesameBotMechStatus:
        """Return a mechanical status of a device.

        Returns:
            CHSesameBotMechStatus: Current mechanical status of the device.
        """
        ...
    
    def subscribeMechStatus(self, callback: Optional[Callable[[CHSesameBot, CHSesameBotMechStatus], None]] = ...) -> None:
        """Subscribe to a topic at AWS IoT

        Args:
            callback (Callable[[CHSesameBot, CHSesameBotMechStatus], None], optional): The registered callback will be executed once an update is delivered. Defaults to `None`.

        Raises:
            NotImplementedError: If the authenticator is not `AuthType.SDK`.
        """
        ...
    
    @property
    def historyEntries(self) -> List[CHSesame2History]:
        """Return the history of all events with a device.

        Returns:
            list[CHSesame2History]: A list of events.
        """
        ...
    
    def getDeviceShadowStatus(self) -> CHSesame2ShadowStatus:
        """Return a cached shadow status of a device.
        In order to refresh the shadow, run `mechStatus`.

        Returns:
            CHSesame2ShadowStatus: Shadow (assumed) status of the device.
        """
        ...
    
    def setDeviceShadowStatus(self, status: CHSesame2ShadowStatus) -> None:
        """Set a shadow status of a device.

        Args:
            status (CHSesame2ShadowStatus): Desired shadow (assumed) status

        Raises:
            ValueError: If `status` is invalid.
        """
        ...
    
    def click(self, history_tag: str = ...) -> bool:
        """Locking.

        Args:
            history_tag (str): The key tag to sent when locking and unlocking. Defaults to `pysesame3`.

        Returns:
            bool: `True` if it is successfully locked, `False` if not.
        """
        ...
    
    def __str__(self) -> str:
        """Return a string representation of an object.

        Returns:
            str: The string representation of the object.
        """
        ...
    


