skylar - hello!!

hello -Alec

Hello there!
General kenobi -Connor
hello -william

# Build Instructions
We don't need docker compose since we don't have multiple services.
We'll have the website at localhost:8081

So we need to map :80 within the docker -> :8081 outside the container

On server, run `docker build . -t website`

On server, run `docker run -p 8081:80 -d --restart always <Image ID>`