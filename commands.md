##### Building a Docker Image
```
docker build -t my-docker-image .
```
<br>
##### Running a Docker Container
```
docker run -d --name my-docker-container -p 8000:8000 -v .:/app my-docker-image
```
<br>
##### Running a Docker Container from a Docker Compose file
```
docker compose up -d
```

