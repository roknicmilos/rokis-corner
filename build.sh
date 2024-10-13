#!/bin/bash

set -x # Enable printing of each command

mkdir -p /app/build
cp /app/src/index.html /app/build/index.html
cp /app/src/style.css /app/build/style.css
cp -r /app/src/assets /app/build/assets

ls -la /app/src
cat /app/src/.env

node /app/src/build.js

set +x # Disable printing of each command
