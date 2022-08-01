"""
This type stub file was generated by pyright.
"""

import threading
import typing
from typing import Any, Callable, Optional, Sequence
from google.cloud.pubsub_v1.publisher import Client as PublisherClient, futures
from google.cloud.pubsub_v1.publisher._batch import base
from google.pubsub_v1 import types as gapic_types
from google.cloud import pubsub_v1
from google.cloud.pubsub_v1 import types
from google.pubsub_v1.services.publisher.client import OptionalRetry

if typing.TYPE_CHECKING:
    ...
_LOGGER = ...
_CAN_COMMIT = ...
_SERVER_PUBLISH_MAX_BYTES = ...
_raw_proto_pubbsub_message = ...
class Batch(base.Batch):
    """A batch of messages.

    The batch is the internal group of messages which are either awaiting
    publication or currently in progress.

    A batch is automatically created by the PublisherClient when the first
    message to be published is received; subsequent messages are added to
    that batch until the process of actual publishing _starts_.

    Once this occurs, any new messages sent to :meth:`publish` open a new
    batch.

    If you are using this library, you most likely do not need to instantiate
    batch objects directly; they will be created for you. If you want to
    change the actual batching settings, see the ``batching`` argument on
    :class:`~.pubsub_v1.PublisherClient`.

    Any properties or methods on this class which are not defined in
    :class:`~.pubsub_v1.publisher.batch.BaseBatch` should be considered
    implementation details.

    Args:
        client:
            The publisher client used to create this batch.
        topic:
            The topic. The format for this is ``projects/{project}/topics/{topic}``.
        settings:
            The settings for batch publishing. These should be considered immutable
            once the batch has been opened.
        batch_done_callback:
            Callback called when the response for a batch publish has been received.
            Called with one boolean argument: successfully published or a permanent
            error occurred. Temporary errors are not surfaced because they are retried
            at a lower level.
        commit_when_full:
            Whether to commit the batch when the batch is full.
        commit_retry:
            Designation of what errors, if any, should be retried when commiting
            the batch. If not provided, a default retry is used.
        commit_timeout:
            The timeout to apply when commiting the batch. If not provided, a default
            timeout is used.
    """
    def __init__(self, client: PublisherClient, topic: str, settings: types.BatchSettings, batch_done_callback: Callable[[bool], Any] = ..., commit_when_full: bool = ..., commit_retry: OptionalRetry = ..., commit_timeout: types.OptionalTimeout = ...) -> None:
        ...
    
    @staticmethod
    def make_lock() -> threading.Lock:
        """Return a threading lock.

        Returns:
            A newly created lock.
        """
        ...
    
    @property
    def client(self) -> PublisherClient:
        """A publisher client."""
        ...
    
    @property
    def messages(self) -> Sequence[gapic_types.PubsubMessage]:
        """The messages currently in the batch."""
        ...
    
    @property
    def settings(self) -> types.BatchSettings:
        """Return the batch settings.

        Returns:
            The batch settings. These are considered immutable once the batch has
            been opened.
        """
        ...
    
    @property
    def size(self) -> int:
        """Return the total size of all of the messages currently in the batch.

        The size includes any overhead of the actual ``PublishRequest`` that is
        sent to the backend.

        Returns:
            The total size of all of the messages currently in the batch (including
            the request overhead), in bytes.
        """
        ...
    
    @property
    def status(self) -> base.BatchStatus:
        """Return the status of this batch.

        Returns:
            The status of this batch. All statuses are human-readable, all-lowercase
            strings.
        """
        ...
    
    def cancel(self, cancellation_reason: base.BatchCancellationReason) -> None:
        """Complete pending futures with an exception.

        This method must be called before publishing starts (ie: while the
        batch is still accepting messages.)

        Args:
            The reason why this batch has been cancelled.
        """
        ...
    
    def commit(self) -> None:
        """Actually publish all of the messages on the active batch.

        .. note::

            This method is non-blocking. It opens a new thread, which calls
            :meth:`_commit`, which does block.

        This synchronously sets the batch status to "starting", and then opens
        a new thread, which handles actually sending the messages to Pub/Sub.

        If the current batch is **not** accepting messages, this method
        does nothing.
        """
        ...
    
    def publish(self, message: gapic_types.PubsubMessage) -> Optional[pubsub_v1.publisher.futures.Future]:
        """Publish a single message.

        Add the given message to this object; this will cause it to be
        published once the batch either has enough messages or a sufficient
        period of time has elapsed. If the batch is full or the commit is
        already in progress, the method does not do anything.

        This method is called by :meth:`~.PublisherClient.publish`.

        Args:
            message: The Pub/Sub message.

        Returns:
            An object conforming to the :class:`~concurrent.futures.Future` interface
            or :data:`None`. If :data:`None` is returned, that signals that the batch
            cannot accept a message.

        Raises:
            pubsub_v1.publisher.exceptions.MessageTooLargeError: If publishing
                the ``message`` would exceed the max size limit on the backend.
        """
        ...
    

