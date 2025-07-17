# Python API

## Instructions

```bash
# 1 - Build the container image
docker build -t python-api .

# 2 - Run the containter locally
docker run -d python-api -p 5000:5000 python-api:latest
