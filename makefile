# Variables
IMAGE_NAME = myapp
CONTAINER_NAME = myapp_container

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run Docker container
run:
	docker run -d --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop Docker container
stop:
	docker stop $(CONTAINER_NAME)

# Remove Docker container
remove:
	docker rm $(CONTAINER_NAME)

# Clean up Docker resources
clean: stop remove
	docker rmi $(IMAGE_NAME)

# Default target
.DEFAULT_GOAL := build
