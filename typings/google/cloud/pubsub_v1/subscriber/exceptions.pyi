"""
This type stub file was generated by pyright.
"""

from enum import Enum
from google.api_core.exceptions import GoogleAPICallError
from typing import Optional

class AcknowledgeStatus(Enum):
    SUCCESS = ...
    PERMISSION_DENIED = ...
    FAILED_PRECONDITION = ...
    INVALID_ACK_ID = ...
    OTHER = ...


class AcknowledgeError(GoogleAPICallError):
    """Error during ack/modack/nack operation on exactly-once-enabled subscription."""
    def __init__(self, error_code: AcknowledgeStatus, info: Optional[str]) -> None:
        ...
    


__all__ = ("AcknowledgeError", )
