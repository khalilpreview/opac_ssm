# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opac.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='opac.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nopac.proto\"\xd0\x01\n\x05\x41sset\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x0c\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x0c\n\x04uuid\x18\x05 \x01(\t\x12\x0e\n\x06\x62ucket\x18\x06 \x01(\t\x12\x10\n\x08\x63hecksum\x18\x07 \x01(\t\x12\x14\n\x0c\x61\x62solute_url\x18\x08 \x01(\t\x12\x19\n\x11\x66ull_absolute_url\x18\t \x01(\t\x12\x12\n\ncreated_at\x18\n \x01(\t\x12\x12\n\nupdated_at\x18\x0b \x01(\t\" \n\x06\x41ssets\x12\x16\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x06.Asset\"*\n\tAssetInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08url_path\x18\x02 \x01(\t\"\x1c\n\x0b\x41ssetExists\x12\r\n\x05\x65xist\x18\x01 \x01(\x08\"\x14\n\x06TaskId\x12\n\n\x02id\x18\x01 \x01(\t\"\x1a\n\tTaskState\x12\r\n\x05state\x18\x01 \x01(\t\"\x16\n\x06\x42ucket\x12\x0c\n\x04name\x18\x01 \x01(\t\",\n\nBucketName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08new_name\x18\x02 \x01(\t\"\x1d\n\x0c\x42ucketExists\x12\r\n\x05\x65xist\x18\x01 \x01(\x08\x32\xce\x02\n\x0c\x41ssetService\x12\x1e\n\tget_asset\x12\x07.TaskId\x1a\x06.Asset\"\x00\x12\x1e\n\tadd_asset\x12\x06.Asset\x1a\x07.TaskId\"\x00\x12!\n\x0cupdate_asset\x12\x06.Asset\x1a\x07.TaskId\"\x00\x12\"\n\x0cremove_asset\x12\x07.TaskId\x1a\x07.TaskId\"\x00\x12\'\n\x0c\x65xists_asset\x12\x07.TaskId\x1a\x0c.AssetExists\"\x00\x12\'\n\x0eget_asset_info\x12\x07.TaskId\x1a\n.AssetInfo\"\x00\x12\'\n\x0eget_task_state\x12\x07.TaskId\x1a\n.TaskState\"\x00\x12 \n\nget_bucket\x12\x07.TaskId\x1a\x07.Bucket\"\x00\x12\x1a\n\x05query\x12\x06.Asset\x1a\x07.Assets\"\x00\x32\xdc\x01\n\rBucketService\x12$\n\nadd_bucket\x12\x0b.BucketName\x1a\x07.TaskId\"\x00\x12\'\n\rupdate_bucket\x12\x0b.BucketName\x1a\x07.TaskId\"\x00\x12\'\n\rremove_bucket\x12\x0b.BucketName\x1a\x07.TaskId\"\x00\x12-\n\rexists_bucket\x12\x0b.BucketName\x1a\r.BucketExists\"\x00\x12$\n\nget_assets\x12\x0b.BucketName\x1a\x07.Assets\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='Asset.file', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='Asset.filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Asset.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Asset.metadata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Asset.uuid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='Asset.bucket', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='Asset.checksum', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_url', full_name='Asset.absolute_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='full_absolute_url', full_name='Asset.full_absolute_url', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='Asset.created_at', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='Asset.updated_at', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=223,
)


_ASSETS = _descriptor.Descriptor(
  name='Assets',
  full_name='Assets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assets', full_name='Assets.assets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=257,
)


_ASSETINFO = _descriptor.Descriptor(
  name='AssetInfo',
  full_name='AssetInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='AssetInfo.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url_path', full_name='AssetInfo.url_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=301,
)


_ASSETEXISTS = _descriptor.Descriptor(
  name='AssetExists',
  full_name='AssetExists',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='AssetExists.exist', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=331,
)


_TASKID = _descriptor.Descriptor(
  name='TaskId',
  full_name='TaskId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='TaskId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=353,
)


_TASKSTATE = _descriptor.Descriptor(
  name='TaskState',
  full_name='TaskState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='TaskState.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=381,
)


_BUCKET = _descriptor.Descriptor(
  name='Bucket',
  full_name='Bucket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Bucket.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=405,
)


_BUCKETNAME = _descriptor.Descriptor(
  name='BucketName',
  full_name='BucketName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BucketName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_name', full_name='BucketName.new_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=451,
)


_BUCKETEXISTS = _descriptor.Descriptor(
  name='BucketExists',
  full_name='BucketExists',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exist', full_name='BucketExists.exist', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=482,
)

_ASSETS.fields_by_name['assets'].message_type = _ASSET
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Assets'] = _ASSETS
DESCRIPTOR.message_types_by_name['AssetInfo'] = _ASSETINFO
DESCRIPTOR.message_types_by_name['AssetExists'] = _ASSETEXISTS
DESCRIPTOR.message_types_by_name['TaskId'] = _TASKID
DESCRIPTOR.message_types_by_name['TaskState'] = _TASKSTATE
DESCRIPTOR.message_types_by_name['Bucket'] = _BUCKET
DESCRIPTOR.message_types_by_name['BucketName'] = _BUCKETNAME
DESCRIPTOR.message_types_by_name['BucketExists'] = _BUCKETEXISTS

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), dict(
  DESCRIPTOR = _ASSET,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:Asset)
  ))
_sym_db.RegisterMessage(Asset)

Assets = _reflection.GeneratedProtocolMessageType('Assets', (_message.Message,), dict(
  DESCRIPTOR = _ASSETS,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:Assets)
  ))
_sym_db.RegisterMessage(Assets)

AssetInfo = _reflection.GeneratedProtocolMessageType('AssetInfo', (_message.Message,), dict(
  DESCRIPTOR = _ASSETINFO,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:AssetInfo)
  ))
_sym_db.RegisterMessage(AssetInfo)

AssetExists = _reflection.GeneratedProtocolMessageType('AssetExists', (_message.Message,), dict(
  DESCRIPTOR = _ASSETEXISTS,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:AssetExists)
  ))
_sym_db.RegisterMessage(AssetExists)

TaskId = _reflection.GeneratedProtocolMessageType('TaskId', (_message.Message,), dict(
  DESCRIPTOR = _TASKID,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:TaskId)
  ))
_sym_db.RegisterMessage(TaskId)

TaskState = _reflection.GeneratedProtocolMessageType('TaskState', (_message.Message,), dict(
  DESCRIPTOR = _TASKSTATE,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:TaskState)
  ))
_sym_db.RegisterMessage(TaskState)

Bucket = _reflection.GeneratedProtocolMessageType('Bucket', (_message.Message,), dict(
  DESCRIPTOR = _BUCKET,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:Bucket)
  ))
_sym_db.RegisterMessage(Bucket)

BucketName = _reflection.GeneratedProtocolMessageType('BucketName', (_message.Message,), dict(
  DESCRIPTOR = _BUCKETNAME,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:BucketName)
  ))
_sym_db.RegisterMessage(BucketName)

BucketExists = _reflection.GeneratedProtocolMessageType('BucketExists', (_message.Message,), dict(
  DESCRIPTOR = _BUCKETEXISTS,
  __module__ = 'opac_pb2'
  # @@protoc_insertion_point(class_scope:BucketExists)
  ))
_sym_db.RegisterMessage(BucketExists)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class AssetServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.get_asset = channel.unary_unary(
          '/AssetService/get_asset',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=Asset.FromString,
          )
      self.add_asset = channel.unary_unary(
          '/AssetService/add_asset',
          request_serializer=Asset.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.update_asset = channel.unary_unary(
          '/AssetService/update_asset',
          request_serializer=Asset.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.remove_asset = channel.unary_unary(
          '/AssetService/remove_asset',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.exists_asset = channel.unary_unary(
          '/AssetService/exists_asset',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=AssetExists.FromString,
          )
      self.get_asset_info = channel.unary_unary(
          '/AssetService/get_asset_info',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=AssetInfo.FromString,
          )
      self.get_task_state = channel.unary_unary(
          '/AssetService/get_task_state',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=TaskState.FromString,
          )
      self.get_bucket = channel.unary_unary(
          '/AssetService/get_bucket',
          request_serializer=TaskId.SerializeToString,
          response_deserializer=Bucket.FromString,
          )
      self.query = channel.unary_unary(
          '/AssetService/query',
          request_serializer=Asset.SerializeToString,
          response_deserializer=Assets.FromString,
          )


  class AssetServiceServicer(object):

    def get_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def add_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def update_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def remove_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def exists_asset(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_asset_info(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_task_state(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_bucket(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def query(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_AssetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get_asset': grpc.unary_unary_rpc_method_handler(
            servicer.get_asset,
            request_deserializer=TaskId.FromString,
            response_serializer=Asset.SerializeToString,
        ),
        'add_asset': grpc.unary_unary_rpc_method_handler(
            servicer.add_asset,
            request_deserializer=Asset.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'update_asset': grpc.unary_unary_rpc_method_handler(
            servicer.update_asset,
            request_deserializer=Asset.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'remove_asset': grpc.unary_unary_rpc_method_handler(
            servicer.remove_asset,
            request_deserializer=TaskId.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'exists_asset': grpc.unary_unary_rpc_method_handler(
            servicer.exists_asset,
            request_deserializer=TaskId.FromString,
            response_serializer=AssetExists.SerializeToString,
        ),
        'get_asset_info': grpc.unary_unary_rpc_method_handler(
            servicer.get_asset_info,
            request_deserializer=TaskId.FromString,
            response_serializer=AssetInfo.SerializeToString,
        ),
        'get_task_state': grpc.unary_unary_rpc_method_handler(
            servicer.get_task_state,
            request_deserializer=TaskId.FromString,
            response_serializer=TaskState.SerializeToString,
        ),
        'get_bucket': grpc.unary_unary_rpc_method_handler(
            servicer.get_bucket,
            request_deserializer=TaskId.FromString,
            response_serializer=Bucket.SerializeToString,
        ),
        'query': grpc.unary_unary_rpc_method_handler(
            servicer.query,
            request_deserializer=Asset.FromString,
            response_serializer=Assets.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'AssetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BucketServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.add_bucket = channel.unary_unary(
          '/BucketService/add_bucket',
          request_serializer=BucketName.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.update_bucket = channel.unary_unary(
          '/BucketService/update_bucket',
          request_serializer=BucketName.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.remove_bucket = channel.unary_unary(
          '/BucketService/remove_bucket',
          request_serializer=BucketName.SerializeToString,
          response_deserializer=TaskId.FromString,
          )
      self.exists_bucket = channel.unary_unary(
          '/BucketService/exists_bucket',
          request_serializer=BucketName.SerializeToString,
          response_deserializer=BucketExists.FromString,
          )
      self.get_assets = channel.unary_unary(
          '/BucketService/get_assets',
          request_serializer=BucketName.SerializeToString,
          response_deserializer=Assets.FromString,
          )


  class BucketServiceServicer(object):

    def add_bucket(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def update_bucket(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def remove_bucket(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def exists_bucket(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def get_assets(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_BucketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'add_bucket': grpc.unary_unary_rpc_method_handler(
            servicer.add_bucket,
            request_deserializer=BucketName.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'update_bucket': grpc.unary_unary_rpc_method_handler(
            servicer.update_bucket,
            request_deserializer=BucketName.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'remove_bucket': grpc.unary_unary_rpc_method_handler(
            servicer.remove_bucket,
            request_deserializer=BucketName.FromString,
            response_serializer=TaskId.SerializeToString,
        ),
        'exists_bucket': grpc.unary_unary_rpc_method_handler(
            servicer.exists_bucket,
            request_deserializer=BucketName.FromString,
            response_serializer=BucketExists.SerializeToString,
        ),
        'get_assets': grpc.unary_unary_rpc_method_handler(
            servicer.get_assets,
            request_deserializer=BucketName.FromString,
            response_serializer=Assets.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'BucketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaAssetServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def add_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def update_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def remove_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def exists_asset(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_asset_info(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_task_state(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_bucket(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def query(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaAssetServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def get_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_asset.future = None
    def add_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    add_asset.future = None
    def update_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    update_asset.future = None
    def remove_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    remove_asset.future = None
    def exists_asset(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    exists_asset.future = None
    def get_asset_info(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_asset_info.future = None
    def get_task_state(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_task_state.future = None
    def get_bucket(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_bucket.future = None
    def query(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    query.future = None


  def beta_create_AssetService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('AssetService', 'add_asset'): Asset.FromString,
      ('AssetService', 'exists_asset'): TaskId.FromString,
      ('AssetService', 'get_asset'): TaskId.FromString,
      ('AssetService', 'get_asset_info'): TaskId.FromString,
      ('AssetService', 'get_bucket'): TaskId.FromString,
      ('AssetService', 'get_task_state'): TaskId.FromString,
      ('AssetService', 'query'): Asset.FromString,
      ('AssetService', 'remove_asset'): TaskId.FromString,
      ('AssetService', 'update_asset'): Asset.FromString,
    }
    response_serializers = {
      ('AssetService', 'add_asset'): TaskId.SerializeToString,
      ('AssetService', 'exists_asset'): AssetExists.SerializeToString,
      ('AssetService', 'get_asset'): Asset.SerializeToString,
      ('AssetService', 'get_asset_info'): AssetInfo.SerializeToString,
      ('AssetService', 'get_bucket'): Bucket.SerializeToString,
      ('AssetService', 'get_task_state'): TaskState.SerializeToString,
      ('AssetService', 'query'): Assets.SerializeToString,
      ('AssetService', 'remove_asset'): TaskId.SerializeToString,
      ('AssetService', 'update_asset'): TaskId.SerializeToString,
    }
    method_implementations = {
      ('AssetService', 'add_asset'): face_utilities.unary_unary_inline(servicer.add_asset),
      ('AssetService', 'exists_asset'): face_utilities.unary_unary_inline(servicer.exists_asset),
      ('AssetService', 'get_asset'): face_utilities.unary_unary_inline(servicer.get_asset),
      ('AssetService', 'get_asset_info'): face_utilities.unary_unary_inline(servicer.get_asset_info),
      ('AssetService', 'get_bucket'): face_utilities.unary_unary_inline(servicer.get_bucket),
      ('AssetService', 'get_task_state'): face_utilities.unary_unary_inline(servicer.get_task_state),
      ('AssetService', 'query'): face_utilities.unary_unary_inline(servicer.query),
      ('AssetService', 'remove_asset'): face_utilities.unary_unary_inline(servicer.remove_asset),
      ('AssetService', 'update_asset'): face_utilities.unary_unary_inline(servicer.update_asset),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_AssetService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('AssetService', 'add_asset'): Asset.SerializeToString,
      ('AssetService', 'exists_asset'): TaskId.SerializeToString,
      ('AssetService', 'get_asset'): TaskId.SerializeToString,
      ('AssetService', 'get_asset_info'): TaskId.SerializeToString,
      ('AssetService', 'get_bucket'): TaskId.SerializeToString,
      ('AssetService', 'get_task_state'): TaskId.SerializeToString,
      ('AssetService', 'query'): Asset.SerializeToString,
      ('AssetService', 'remove_asset'): TaskId.SerializeToString,
      ('AssetService', 'update_asset'): Asset.SerializeToString,
    }
    response_deserializers = {
      ('AssetService', 'add_asset'): TaskId.FromString,
      ('AssetService', 'exists_asset'): AssetExists.FromString,
      ('AssetService', 'get_asset'): Asset.FromString,
      ('AssetService', 'get_asset_info'): AssetInfo.FromString,
      ('AssetService', 'get_bucket'): Bucket.FromString,
      ('AssetService', 'get_task_state'): TaskState.FromString,
      ('AssetService', 'query'): Assets.FromString,
      ('AssetService', 'remove_asset'): TaskId.FromString,
      ('AssetService', 'update_asset'): TaskId.FromString,
    }
    cardinalities = {
      'add_asset': cardinality.Cardinality.UNARY_UNARY,
      'exists_asset': cardinality.Cardinality.UNARY_UNARY,
      'get_asset': cardinality.Cardinality.UNARY_UNARY,
      'get_asset_info': cardinality.Cardinality.UNARY_UNARY,
      'get_bucket': cardinality.Cardinality.UNARY_UNARY,
      'get_task_state': cardinality.Cardinality.UNARY_UNARY,
      'query': cardinality.Cardinality.UNARY_UNARY,
      'remove_asset': cardinality.Cardinality.UNARY_UNARY,
      'update_asset': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'AssetService', cardinalities, options=stub_options)


  class BetaBucketServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def add_bucket(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def update_bucket(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def remove_bucket(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def exists_bucket(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def get_assets(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaBucketServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def add_bucket(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    add_bucket.future = None
    def update_bucket(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    update_bucket.future = None
    def remove_bucket(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    remove_bucket.future = None
    def exists_bucket(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    exists_bucket.future = None
    def get_assets(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    get_assets.future = None


  def beta_create_BucketService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('BucketService', 'add_bucket'): BucketName.FromString,
      ('BucketService', 'exists_bucket'): BucketName.FromString,
      ('BucketService', 'get_assets'): BucketName.FromString,
      ('BucketService', 'remove_bucket'): BucketName.FromString,
      ('BucketService', 'update_bucket'): BucketName.FromString,
    }
    response_serializers = {
      ('BucketService', 'add_bucket'): TaskId.SerializeToString,
      ('BucketService', 'exists_bucket'): BucketExists.SerializeToString,
      ('BucketService', 'get_assets'): Assets.SerializeToString,
      ('BucketService', 'remove_bucket'): TaskId.SerializeToString,
      ('BucketService', 'update_bucket'): TaskId.SerializeToString,
    }
    method_implementations = {
      ('BucketService', 'add_bucket'): face_utilities.unary_unary_inline(servicer.add_bucket),
      ('BucketService', 'exists_bucket'): face_utilities.unary_unary_inline(servicer.exists_bucket),
      ('BucketService', 'get_assets'): face_utilities.unary_unary_inline(servicer.get_assets),
      ('BucketService', 'remove_bucket'): face_utilities.unary_unary_inline(servicer.remove_bucket),
      ('BucketService', 'update_bucket'): face_utilities.unary_unary_inline(servicer.update_bucket),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_BucketService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('BucketService', 'add_bucket'): BucketName.SerializeToString,
      ('BucketService', 'exists_bucket'): BucketName.SerializeToString,
      ('BucketService', 'get_assets'): BucketName.SerializeToString,
      ('BucketService', 'remove_bucket'): BucketName.SerializeToString,
      ('BucketService', 'update_bucket'): BucketName.SerializeToString,
    }
    response_deserializers = {
      ('BucketService', 'add_bucket'): TaskId.FromString,
      ('BucketService', 'exists_bucket'): BucketExists.FromString,
      ('BucketService', 'get_assets'): Assets.FromString,
      ('BucketService', 'remove_bucket'): TaskId.FromString,
      ('BucketService', 'update_bucket'): TaskId.FromString,
    }
    cardinalities = {
      'add_bucket': cardinality.Cardinality.UNARY_UNARY,
      'exists_bucket': cardinality.Cardinality.UNARY_UNARY,
      'get_assets': cardinality.Cardinality.UNARY_UNARY,
      'remove_bucket': cardinality.Cardinality.UNARY_UNARY,
      'update_bucket': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'BucketService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
