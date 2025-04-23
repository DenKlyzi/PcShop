.DEFAULT_GOAL=start

start:
	docker compose -f docker-compose.yml --project-name pcshop up
.PHONY=start

rebuild:
	docker compose -f docker-compose.yml --project-name pcshop up --build
.PHONY=rebuild

stop:
	docker compose -f docker-compose.yml --project-name pcshop down --remove-orphans
.PHONY=stop
