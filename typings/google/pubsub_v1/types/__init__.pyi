"""
This type stub file was generated by pyright.
"""

from typing import Union

import google.api_core.timeout

from .pubsub import (
    AcknowledgeRequest,
    BigQueryConfig,
    CreateSnapshotRequest,
    DeadLetterPolicy,
    DeleteSnapshotRequest,
    DeleteSubscriptionRequest,
    DeleteTopicRequest,
    DetachSubscriptionRequest,
    DetachSubscriptionResponse,
    ExpirationPolicy,
    GetSnapshotRequest,
    GetSubscriptionRequest,
    GetTopicRequest,
    ListSnapshotsRequest,
    ListSnapshotsResponse,
    ListSubscriptionsRequest,
    ListSubscriptionsResponse,
    ListTopicSnapshotsRequest,
    ListTopicSnapshotsResponse,
    ListTopicsRequest,
    ListTopicsResponse,
    ListTopicSubscriptionsRequest,
    ListTopicSubscriptionsResponse,
    MessageStoragePolicy,
    ModifyAckDeadlineRequest,
    ModifyPushConfigRequest,
    PublishRequest,
    PublishResponse,
    PubsubMessage,
    PullRequest,
    PullResponse,
    PushConfig,
    ReceivedMessage,
    RetryPolicy,
    SchemaSettings,
    SeekRequest,
    SeekResponse,
    Snapshot,
    StreamingPullRequest,
    StreamingPullResponse,
    Subscription,
    Topic,
    UpdateSnapshotRequest,
    UpdateSubscriptionRequest,
    UpdateTopicRequest,
)
from .schema import (
    CreateSchemaRequest,
    DeleteSchemaRequest,
    Encoding,
    GetSchemaRequest,
    ListSchemasRequest,
    ListSchemasResponse,
    Schema,
    SchemaView,
    ValidateMessageRequest,
    ValidateMessageResponse,
    ValidateSchemaRequest,
    ValidateSchemaResponse,
)

TimeoutType = Union[
    int,
    float,
    google.api_core.timeout.ConstantTimeout,
    google.api_core.timeout.ExponentialTimeout,
]
__all__ = (
    "TimeoutType",
    "AcknowledgeRequest",
    "BigQueryConfig",
    "CreateSnapshotRequest",
    "DeadLetterPolicy",
    "DeleteSnapshotRequest",
    "DeleteSubscriptionRequest",
    "DeleteTopicRequest",
    "DetachSubscriptionRequest",
    "DetachSubscriptionResponse",
    "ExpirationPolicy",
    "GetSnapshotRequest",
    "GetSubscriptionRequest",
    "GetTopicRequest",
    "ListSnapshotsRequest",
    "ListSnapshotsResponse",
    "ListSubscriptionsRequest",
    "ListSubscriptionsResponse",
    "ListTopicSnapshotsRequest",
    "ListTopicSnapshotsResponse",
    "ListTopicsRequest",
    "ListTopicsResponse",
    "ListTopicSubscriptionsRequest",
    "ListTopicSubscriptionsResponse",
    "MessageStoragePolicy",
    "ModifyAckDeadlineRequest",
    "ModifyPushConfigRequest",
    "PublishRequest",
    "PublishResponse",
    "PubsubMessage",
    "PullRequest",
    "PullResponse",
    "PushConfig",
    "ReceivedMessage",
    "RetryPolicy",
    "SchemaSettings",
    "SeekRequest",
    "SeekResponse",
    "Snapshot",
    "StreamingPullRequest",
    "StreamingPullResponse",
    "Subscription",
    "Topic",
    "UpdateSnapshotRequest",
    "UpdateSubscriptionRequest",
    "UpdateTopicRequest",
    "CreateSchemaRequest",
    "DeleteSchemaRequest",
    "GetSchemaRequest",
    "ListSchemasRequest",
    "ListSchemasResponse",
    "Schema",
    "ValidateMessageRequest",
    "ValidateMessageResponse",
    "ValidateSchemaRequest",
    "ValidateSchemaResponse",
    "Encoding",
    "SchemaView",
)