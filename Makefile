# Variables
APP_NAME = openbcg-api
DOCKER_COMPOSE_FILE = docker-compose.yml

# Default target
.PHONY: all
all: build

# Build the Docker image
.PHONY: build
build:
	@echo "Building Docker image..."
	docker build -t $(APP_NAME) .

# Run the Docker container
.PHONY: run
run:
	@echo "Running Docker container..."
	docker run -d --name $(APP_NAME)-container -p 8000:80 $(APP_NAME)

# Stop and remove the Docker container
.PHONY: stop
stop:
	@echo "Stopping Docker container..."
	docker stop $(APP_NAME)-container
	@echo "Removing Docker container..."
	docker rm $(APP_NAME)-container

# Use Docker Compose to build and run services
.PHONY: compose-up
compose-up:
	@echo "Starting services with Docker Compose..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) up --build -d

# Stop and remove services with Docker Compose
.PHONY: compose-down
compose-down:
	@echo "Stopping services with Docker Compose..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) down

# Display logs from Docker Compose services
.PHONY: logs
logs:
	@echo "Displaying logs..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs -f

# Clean up Docker images and containers
.PHONY: clean
clean: stop
	@echo "Cleaning up Docker images..."
	docker rmi $(APP_NAME)

# Clean build: Stop, remove, and rebuild everything
.PHONY: clean-build
clean-build: clean
	@echo "Performing a clean build..."
	docker-compose -f $(DOCKER_COMPOSE_FILE) build --no-cache
