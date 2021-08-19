# 23:18

# This looks for build deinition from Dockerfile
docker build -t app ./

rsync -a ./* root@46.101.88.88:/root/code/fastapi-deploy/


docker-compose -f docker-compose.traefik.yml up -d --force-recreate --remove-orphans
docker-compose -f docker-compose.yml up -d --force-recreate --remove-orphans



 sudo systemctl daemon-reload
 sudo systemctl restart docker