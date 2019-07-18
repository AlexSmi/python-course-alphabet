init:
ifneq ("$(wildcard .env)",".env")
	cp .env.example .env
endif
ifneq ("$(wildcard .venv)",".venv")
	python3 -m venv .venv
endif
	docker-compose build

up:
	docker-compose up

stop:
ifdef purge
	docker-compose rm -fsv
	docker-compose down --rmi all --remove-orphans -v
else
	docker-compose stop
endif

migrate:
	docker-compose run --rm server ./manage.py migrate

show_migrate:
	docker-compose run --rm server ./manage.py showmigrations

shell_server:
	docker-compose run --rm server sh

ipdb:
	docker-compose run --rm --service-ports server

shell:
	docker-compose run --rm server ./manage.py shell

ss:
	$(MAKE) shell_server
