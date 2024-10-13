# Roki's Corner

## Quick Start

1. Build the Docker image:
    ```bash
    docker build -t rokis-corner-node .
    ```

2. Run the Docker container:
    ```bash
    docker run --rm -v $(pwd)/build:/app/build rokis-corner-node
    ```

3. Open the generated HTML file in your browser:
    ```bash
    open build/index.html
    ```
