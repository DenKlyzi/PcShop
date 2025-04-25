.DEFAULT_GOAL := start

start:
	docker compose -f docker-compose.yml --project-name pcshop up

rebuild:
	docker compose -f docker-compose.yml --project-name pcshop up --build

stop:
	docker compose -f docker-compose.yml --project-name pcshop down --remove-orphans

.PHONY: start rebuild stop
