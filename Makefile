.PHONY: build clean shell stop test up

help:
	@echo "Welcome to the Schema Service\n\n"
	@echo "The list of commands for local development:\n"
	@echo "  build      Builds the docker images for the docker-compose setup"
	@echo "  clean      Stops and removes all docker containers"
	@echo "  shell      Opens a Bash shell"
	@echo "  test       Runs the Python test suite"
	@echo "  up         Runs the whole stack, served under http://localhost:8000/\n"
	@echo "  stop       Stops the docker containers"

build:
	docker-compose build

clean: stop
	docker-compose rm -f
	rm -rf coverage/ .coverage

shell:
	docker-compose run web bash

stop:
	docker-compose stop

test:
	docker-compose run web test

up:
	docker-compose up
