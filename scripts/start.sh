#!/bin/bash

echo "Building the project..."
docker build -t rokis-corner-node .

echo "Running the project..."
docker run --rm -v $(pwd)/build:/app/build rokis-corner-node

echo "Opening the project in the browser..."
open build/index.html
