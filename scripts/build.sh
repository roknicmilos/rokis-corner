#!/bin/bash

set -x # Enable printing of each command

rm -rf /app/build
mkdir -p /app/build

cp /app/src/index.html /app/build/index.html
cp /app/src/style.css /app/build/style.css
cp -r /app/src/assets /app/build/assets

node /app/src/build.js

set +x # Disable printing of each command
