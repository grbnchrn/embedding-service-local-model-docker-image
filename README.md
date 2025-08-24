
# Info
A ready-to-run Dockerfile + API server (like a FastAPI service) that exposes nomic-embed-text-v1.5 directly as an embeddings endpoint

# Build the Docker image
docker build -t embedding-service .

# Run the container
docker run -p 8000:8000 embedding-service


# To test this image

curl -X POST http://localhost:8000/embed \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello world"}'
