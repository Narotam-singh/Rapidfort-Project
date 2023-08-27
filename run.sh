#!/bin/bash

PORT_MAPPING="5000:5000"
IMAGE_NAME="rapidfort-project:v1.0"

docker run -d -p "$PORT_MAPPING" "$IMAGE_NAME"
