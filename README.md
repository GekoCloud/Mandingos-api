# Building the container
Requires two build-time arguments: `PORT` and `WORKERS`
> docker build -t cc_app:0 --build-arg PORT=80 --build-arg WORKERS=1 .

# Running the container
> docker run -p `HOST_PORT`:<`PORT`> cc_app:0

# Accessing the API
> curl --request POST \
--url http://<host>:<HOST_PORT>/move \
--header 'content-type: application/json' \
--data '@post.json'
