:: Mongo
docker run -d -p 8080:27017 --name mongoDocker mongo
docker exec -it mongoDocker mongosh