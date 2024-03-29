"""
This type stub file was generated by pyright.
"""

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple
from google.pubsub_v1.types import schema

class ListSchemasPager:
    """A pager for iterating through ``list_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemasResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSchemas`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., schema.ListSchemasResponse], request: schema.ListSchemasRequest, response: schema.ListSchemasResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemasRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemasResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[schema.ListSchemasResponse]:
        ...
    
    def __iter__(self) -> Iterator[schema.Schema]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListSchemasAsyncPager:
    """A pager for iterating through ``list_schemas`` requests.

    This class thinly wraps an initial
    :class:`google.pubsub_v1.types.ListSchemasResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``schemas`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSchemas`` requests and continue to iterate
    through the ``schemas`` field on the
    corresponding responses.

    All the usual :class:`google.pubsub_v1.types.ListSchemasResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[schema.ListSchemasResponse]], request: schema.ListSchemasRequest, response: schema.ListSchemasResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.pubsub_v1.types.ListSchemasRequest):
                The initial request object.
            response (google.pubsub_v1.types.ListSchemasResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[schema.ListSchemasResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[schema.Schema]:
        ...
    
    def __repr__(self) -> str:
        ...
    


