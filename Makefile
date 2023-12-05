HOST_PORT=8080
CNTR_PORT=8000
TAG=v1.0
NAME=opp-app
REPO_HOST=180214055794.dkr.ecr.us-east-2.amazonaws.com/opp-app
TAGGED_IMAGE=$(REPO_HOST):$(TAG)

image: Dockerfile
	docker build --pull -t $(NAME):latest .

run-app-local:
	docker run --detach --publish $(HOST_PORT):$(CNTR_PORT) --name $(NAME) opp_app:latest

run-app-prod:
	docker run --detach --publish $(HOST_PORT):$(CNTR_PORT) --name $(NAME) $(TAGGED_IMAGE)

exec-app:
	docker exec -it $(NAME) bash

	