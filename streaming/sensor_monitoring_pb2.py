# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: sensor_monitoring.proto
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
    'sensor_monitoring.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17sensor_monitoring.proto\x12\x11sensor_monitoring\"Y\n\nSensorData\x12\x11\n\tsensor_id\x18\x01 \x01(\t\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12\x10\n\x08humidity\x18\x03 \x01(\x02\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"*\n\x05\x41lert\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08\x63ritical\x18\x02 \x01(\x08\x32l\n\x17SensorMonitoringService\x12Q\n\x10StreamSensorData\x12\x1d.sensor_monitoring.SensorData\x1a\x18.sensor_monitoring.Alert\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_monitoring_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENSORDATA']._serialized_start=46
  _globals['_SENSORDATA']._serialized_end=135
  _globals['_ALERT']._serialized_start=137
  _globals['_ALERT']._serialized_end=179
  _globals['_SENSORMONITORINGSERVICE']._serialized_start=181
  _globals['_SENSORMONITORINGSERVICE']._serialized_end=289
# @@protoc_insertion_point(module_scope)