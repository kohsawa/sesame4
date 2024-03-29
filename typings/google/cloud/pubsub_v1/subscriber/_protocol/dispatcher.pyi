"""
This type stub file was generated by pyright.
"""

import typing
import queue
from typing import Sequence, Union
from google.cloud.pubsub_v1.subscriber._protocol import requests
from google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager import StreamingPullManager

if typing.TYPE_CHECKING:
    ...
RequestItem = Union[requests.AckRequest, requests.DropRequest, requests.LeaseRequest, requests.ModAckRequest, requests.NackRequest,]
_LOGGER = ...
_CALLBACK_WORKER_NAME = ...
_MAX_BATCH_SIZE = ...
_MAX_BATCH_LATENCY = ...
_ACK_IDS_BATCH_SIZE = ...
_MIN_EXACTLY_ONCE_DELIVERY_ACK_MODACK_RETRY_DURATION_SECS = ...
_MAX_EXACTLY_ONCE_DELIVERY_ACK_MODACK_RETRY_DURATION_SECS = ...
class Dispatcher:
    def __init__(self, manager: StreamingPullManager, queue: queue.Queue) -> None:
        ...
    
    def start(self) -> None:
        """Start a thread to dispatch requests queued up by callbacks.

        Spawns a thread to run :meth:`dispatch_callback`.
        """
        ...
    
    def stop(self) -> None:
        ...
    
    def dispatch_callback(self, items: Sequence[RequestItem]) -> None:
        """Map the callback request to the appropriate gRPC request.

        Args:
            items:
                Queued requests to dispatch.
        """
        ...
    
    def ack(self, items: Sequence[requests.AckRequest]) -> None:
        """Acknowledge the given messages.

        Args:
            items: The items to acknowledge.
        """
        ...
    
    def drop(self, items: Sequence[Union[requests.AckRequest, requests.DropRequest, requests.NackRequest]]) -> None:
        """Remove the given messages from lease management.

        Args:
            items: The items to drop.
        """
        ...
    
    def lease(self, items: Sequence[requests.LeaseRequest]) -> None:
        """Add the given messages to lease management.

        Args:
            items: The items to lease.
        """
        ...
    
    def modify_ack_deadline(self, items: Sequence[requests.ModAckRequest]) -> None:
        """Modify the ack deadline for the given messages.

        Args:
            items: The items to modify.
        """
        ...
    
    def nack(self, items: Sequence[requests.NackRequest]) -> None:
        """Explicitly deny receipt of messages.

        Args:
            items: The items to deny.
        """
        ...
    


