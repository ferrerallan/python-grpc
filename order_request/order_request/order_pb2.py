# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: order_request/order.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'order_request/order.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19order_request/order.proto\x12\x05order\"M\n\x0cOrderRequest\x12\x15\n\rcustomer_name\x18\x01 \x01(\t\x12\x14\n\x0cproduct_name\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"6\n\x11OrderConfirmation\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2N\n\x0cOrderService\x12>\n\x0b\x43reateOrder\x12\x13.order.OrderRequest\x1a\x18.order.OrderConfirmation\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'order_request.order_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDERREQUEST']._serialized_start=36
  _globals['_ORDERREQUEST']._serialized_end=113
  _globals['_ORDERCONFIRMATION']._serialized_start=115
  _globals['_ORDERCONFIRMATION']._serialized_end=169
  _globals['_ORDERSERVICE']._serialized_start=171
  _globals['_ORDERSERVICE']._serialized_end=249
# @@protoc_insertion_point(module_scope)
