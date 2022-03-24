#Redis
docker run -p 8081:6379 --name redisDocker redis
docker exec -it redisDocker redis-cli