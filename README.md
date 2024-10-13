# Roki's Corner

## Quick Start

1. Create `src/.env` file based on `src/example.env`:
    ```bash
    cp src/.env.example src/.env
    ```
   Change the values in `src/.env` to match your environment.
   <br/><br/>

2. Build the Docker image:
    ```bash
    docker build -t rokis-corner-node .
    ```

3. Run the Docker container:
    ```bash
    docker run --rm -v $(pwd)/build:/app/build rokis-corner-node
    ```

4. Open the generated HTML file in your browser:
    ```bash
    open build/index.html
    ```
