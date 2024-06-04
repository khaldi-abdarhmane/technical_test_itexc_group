docker compose -f dev_scripts/docker/docker-compose.yml up itexc_group-db -d -db
docker compose -f dev_scripts/docker/docker-compose.yml up -d pgadmin4
echo "DB_HOST="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' itexc_group-db) > dev_scripts/.local.env
