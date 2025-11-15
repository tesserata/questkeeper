#!/bin/bash

PROTO_ROOT="libs/api_contracts/proto"
OUT_ROOT="libs/api_contracts/src"
P2P_OUT="libs/api_contracts/src/qk_api_contracts/pydantic"

rm -rf "$P2P_OUT/"*

python -m grpc_tools.protoc \
  -I "$PROTO_ROOT" \
  --python_out="$OUT_ROOT" \
  --grpc_python_out="$OUT_ROOT" \
  --pyi_out="$OUT_ROOT" \
  --protobuf-to-pydantic_out="$P2P_OUT" \
  qk_api_contracts/grpc/common.proto \
  qk_api_contracts/grpc/meta.proto \
  qk_api_contracts/grpc/servers.proto \
  qk_api_contracts/grpc/worker_service.proto \
  qk_api_contracts/grpc/characters/models.proto \
  qk_api_contracts/grpc/characters/commands_service.proto \
  qk_api_contracts/grpc/characters/query_service.proto \
  qk_api_contracts/grpc/events/models.proto \
  qk_api_contracts/grpc/events/commands_service.proto \
  qk_api_contracts/grpc/events/query_service.proto \
  qk_api_contracts/grpc/sessions/models.proto \
  qk_api_contracts/grpc/sessions/commands_service.proto \
  qk_api_contracts/grpc/sessions/query_service.proto

mv "$P2P_OUT/qk_api_contracts/grpc"/* "$P2P_OUT"
rmdir "$P2P_OUT/qk_api_contracts/grpc"
rmdir "$P2P_OUT/qk_api_contracts"