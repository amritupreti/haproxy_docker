# HAProxy with Docker Compose
This repository provides a simple setup for running HAProxy using Docker Compose.
Docker compose will spin 4 FastAPI servers named `server1`, `server2`, `server3`, and `server4` and a `HAProxy server` that will load balance the requests to these FastAPI servers.

## What is in the server?
All the setups are covered in the `docker-compose.yml` file. Please check it for details.

Server reads `SERVER_NAME` environment variable and returns it in the response.
Each server has a different `SERVER_NAME` env in compose file.

The server contains 4 routes:
- `/`: Returns `Home Page!`
- `/admin`: Returns `Admin Page!`. We want to restrict access to this route from the HAProxy frontend client.
- `/lightwork`: Returns `{server_name}: Doing light work!`. This route simulates a light workload.
- `/heavywork`: Returns `{server_name}: Doing heavy work!`. This route simulates a heavy workload.

## What is in the HAProxy?
HAProxy is configured to:
- Load balance requests to the FastAPI servers.
- Restrict access to the `/admin` route, allowing only requests from the HAProxy frontend client.
- Route requests to the `/lightwork` `roundrobin` to the `server1` and `server2` servers.
- Route requests to the `/heavywork` `source` to the `server3` and `server4` servers.
- Route requests to the `/` `roundrobin` to all servers.

## How to run the servers and HAProxy?
```bash
docker-compose up -d
```

**Note:**: Make sure you have Docker and Docker Compose installed on your machine.

## What is the expected output?
You can access the servers and HAProxy using the following URLs:
- `server1`: http://localhost:8001
- `server2`: http://localhost:8002
- `server3`: http://localhost:8003
- `server4`: http://localhost:8004
- `HAProxy`: http://localhost:8000
