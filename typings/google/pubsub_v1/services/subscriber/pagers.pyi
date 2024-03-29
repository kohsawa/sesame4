"""
This type stub file was generated by pyright.
"""

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple
from google.pubsub_v1.types import pubsub

class ListSubscriptionsPager:
    """A pager for iterating through ``list_subscriptions`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSubscriptionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``subscriptions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSubscriptions`` requests and continue to iterate
    through the ``subscriptions`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSubscriptionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., pubsub.ListSubscriptionsResponse], request: pubsub.ListSubscriptionsRequest, response: pubsub.ListSubscriptionsResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSubscriptionsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSubscriptionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[pubsub.ListSubscriptionsResponse]:
        ...
    
    def __iter__(self) -> Iterator[pubsub.Subscription]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListSubscriptionsAsyncPager:
    """A pager for iterating through ``list_subscriptions`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSubscriptionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``subscriptions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSubscriptions`` requests and continue to iterate
    through the ``subscriptions`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSubscriptionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[pubsub.ListSubscriptionsResponse]], request: pubsub.ListSubscriptionsRequest, response: pubsub.ListSubscriptionsResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSubscriptionsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSubscriptionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[pubsub.ListSubscriptionsResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[pubsub.Subscription]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListSnapshotsPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSnapshotsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., pubsub.ListSnapshotsResponse], request: pubsub.ListSnapshotsRequest, response: pubsub.ListSnapshotsResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSnapshotsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[pubsub.ListSnapshotsResponse]:
        ...
    
    def __iter__(self) -> Iterator[pubsub.Snapshot]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListSnapshotsAsyncPager:
    """A pager for iterating through ``list_snapshots`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSnapshotsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``snapshots`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSnapshots`` requests and continue to iterate
    through the ``snapshots`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSnapshotsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[pubsub.ListSnapshotsResponse]], request: pubsub.ListSnapshotsRequest, response: pubsub.ListSnapshotsResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSnapshotsRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSnapshotsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[pubsub.ListSnapshotsResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[pubsub.Snapshot]:
        ...
    
    def __repr__(self) -> str:
        ...
    


