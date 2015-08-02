#!/usr/bin/env bash
set -o verbose

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` base.proto
protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` content.proto
protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` event_store.proto