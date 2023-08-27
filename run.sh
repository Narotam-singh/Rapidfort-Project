#!/bin/bash

PORT_MAPPING="5000:5000"
IMAGE_NAME="rapidfort-project:latest"

docker run -d -p "$PORT_MAPPING" "$IMAGE_NAME"
