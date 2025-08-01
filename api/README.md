# Python API

## Instructions

### Docker commands
1 - Build the container image
```bash
docker build -t python-api .
```

2 - Run the containter locally
```bash
docker run -d python-api -p 5000:5000 python-api:latest
```

### Docker Compose
1 - Spin up the environemnt
```bash
docker compose up --build --detach
```
2 - Clean up the environment
```bash
docker compose down -v
```
