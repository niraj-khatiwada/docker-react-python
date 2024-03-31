docker-compose:
	docker compose -f ./docker-compose.yml --env-file ./frontend/.env --env-file ./api/.env up -d