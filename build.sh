# Stop on error https://stackoverflow.com/a/2871034/10882657
set -e

# Build image without context
# https://stackoverflow.com/a/54666214/10882657
docker build -f Dockerfile -t vibing-image:0.1.0 .