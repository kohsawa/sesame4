"""
This type stub file was generated by pyright.
"""

import proto

__protobuf__ = ...
class SchemaView(proto.Enum):
    r"""View of Schema object fields to be returned by GetSchema and
    ListSchemas.
    """
    SCHEMA_VIEW_UNSPECIFIED = ...
    BASIC = ...
    FULL = ...


class Encoding(proto.Enum):
    r"""Possible encoding types for messages."""
    ENCODING_UNSPECIFIED = ...
    JSON = ...
    BINARY = ...


class Schema(proto.Message):
    r"""A schema resource.

    Attributes:
        name (str):
            Required. Name of the schema. Format is
            ``projects/{project}/schemas/{schema}``.
        type_ (google.pubsub_v1.types.Schema.Type):
            The type of the schema definition.
        definition (str):
            The definition of the schema. This should contain a string
            representing the full definition of the schema that is a
            valid schema definition of the type specified in ``type``.
    """
    class Type(proto.Enum):
        r"""Possible schema definition types."""
        TYPE_UNSPECIFIED = ...
        PROTOCOL_BUFFER = ...
        AVRO = ...
    
    
    name = ...
    type_ = ...
    definition = ...


class CreateSchemaRequest(proto.Message):
    r"""Request for the CreateSchema method.

    Attributes:
        parent (str):
            Required. The name of the project in which to create the
            schema. Format is ``projects/{project-id}``.
        schema (google.pubsub_v1.types.Schema):
            Required. The schema object to create.

            This schema's ``name`` parameter is ignored. The schema
            object returned by CreateSchema will have a ``name`` made
            using the given ``parent`` and ``schema_id``.
        schema_id (str):
            The ID to use for the schema, which will become the final
            component of the schema's resource name.

            See
            https://cloud.google.com/pubsub/docs/admin#resource_names
            for resource name constraints.
    """
    parent = ...
    schema = ...
    schema_id = ...


class GetSchemaRequest(proto.Message):
    r"""Request for the GetSchema method.

    Attributes:
        name (str):
            Required. The name of the schema to get. Format is
            ``projects/{project}/schemas/{schema}``.
        view (google.pubsub_v1.types.SchemaView):
            The set of fields to return in the response. If not set,
            returns a Schema with ``name`` and ``type``, but not
            ``definition``. Set to ``FULL`` to retrieve all fields.
    """
    name = ...
    view = ...


class ListSchemasRequest(proto.Message):
    r"""Request for the ``ListSchemas`` method.

    Attributes:
        parent (str):
            Required. The name of the project in which to list schemas.
            Format is ``projects/{project-id}``.
        view (google.pubsub_v1.types.SchemaView):
            The set of Schema fields to return in the response. If not
            set, returns Schemas with ``name`` and ``type``, but not
            ``definition``. Set to ``FULL`` to retrieve all fields.
        page_size (int):
            Maximum number of schemas to return.
        page_token (str):
            The value returned by the last ``ListSchemasResponse``;
            indicates that this is a continuation of a prior
            ``ListSchemas`` call, and that the system should return the
            next page of data.
    """
    parent = ...
    view = ...
    page_size = ...
    page_token = ...


class ListSchemasResponse(proto.Message):
    r"""Response for the ``ListSchemas`` method.

    Attributes:
        schemas (Sequence[google.pubsub_v1.types.Schema]):
            The resulting schemas.
        next_page_token (str):
            If not empty, indicates that there may be more schemas that
            match the request; this value should be passed in a new
            ``ListSchemasRequest``.
    """
    @property
    def raw_page(self): # -> Self@ListSchemasResponse:
        ...
    
    schemas = ...
    next_page_token = ...


class DeleteSchemaRequest(proto.Message):
    r"""Request for the ``DeleteSchema`` method.

    Attributes:
        name (str):
            Required. Name of the schema to delete. Format is
            ``projects/{project}/schemas/{schema}``.
    """
    name = ...


class ValidateSchemaRequest(proto.Message):
    r"""Request for the ``ValidateSchema`` method.

    Attributes:
        parent (str):
            Required. The name of the project in which to validate
            schemas. Format is ``projects/{project-id}``.
        schema (google.pubsub_v1.types.Schema):
            Required. The schema object to validate.
    """
    parent = ...
    schema = ...


class ValidateSchemaResponse(proto.Message):
    r"""Response for the ``ValidateSchema`` method. Empty for now."""
    ...


class ValidateMessageRequest(proto.Message):
    r"""Request for the ``ValidateMessage`` method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The name of the project in which to validate
            schemas. Format is ``projects/{project-id}``.
        name (str):
            Name of the schema against which to validate.

            Format is ``projects/{project}/schemas/{schema}``.

            This field is a member of `oneof`_ ``schema_spec``.
        schema (google.pubsub_v1.types.Schema):
            Ad-hoc schema against which to validate

            This field is a member of `oneof`_ ``schema_spec``.
        message (bytes):
            Message to validate against the provided ``schema_spec``.
        encoding (google.pubsub_v1.types.Encoding):
            The encoding expected for messages
    """
    parent = ...
    name = ...
    schema = ...
    message = ...
    encoding = ...


class ValidateMessageResponse(proto.Message):
    r"""Response for the ``ValidateMessage`` method. Empty for now."""
    ...


__all__ = tuple(sorted(__protobuf__.manifest))