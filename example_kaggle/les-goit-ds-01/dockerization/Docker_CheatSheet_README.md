# 🚀 Docker Cheat Sheet

## 🐳 Common Docker Commands

### 📦 Images
- `docker images`  
  List all local Docker images.
- `docker pull <image>`  
  Download an image from Docker Hub.  
  _Example:_ `docker pull nginx`
- `docker rmi <image>`  
  Remove an image.  
  _Example:_ `docker rmi ubuntu:latest`  
  _Force:_ `docker rmi -f <image_id>`

---

### 📦 Containers
- `docker ps`  
  List running containers.
- `docker ps -a`  
  List all containers (including stopped).
- `docker run <image>`  
  Run a container from an image.  
  _Example:_ `docker run -it ubuntu bash`
- `docker stop <container>`  
  Stop a running container.
- `docker rm <container>`  
  Remove a stopped container.  
  _Force:_ `docker rm -f <container_id>`

---

### 🛠️ Build
- `docker build -t <tag> .`  
  Build an image from a Dockerfile.  
  _Example:_ `docker build -t myapp:latest .`

---

### 🌐 Networks
- `docker network ls`  
  List all Docker networks.
- `docker network create <name>`  
  Create a new network.  
  _Example:_ `docker network create mynetwork`

---

### 💾 Volumes
- `docker volume ls`  
  List Docker volumes.
- `docker volume create <name>`  
  Create a Docker volume.

---

### 📋 Logs
- `docker logs <container>`  
  View logs of a container.

---

### 🔧 Exec
- `docker exec -it <container> <command>`  
  Run a command in a running container.  
  _Example:_ `docker exec -it mycontainer bash`

---

## 🧩 Docker Compose

- `docker-compose up`  
  Start services defined in `docker-compose.yml`.
- `docker-compose down`  
  Stop and remove all services.
- `docker-compose build`  
  Build services from the `docker-compose.yml`.

---

## ⚙️ Useful Flags

- `-d`  
  Run container in **detached mode**.
- `--name <name>`  
  Assign a **name** to the container.  
  _Example:_ `docker run --name web nginx`
- `-p <host_port>:<container_port>`  
  **Port mapping** from host to container.  
  _Example:_ `docker run -p 8080:80 nginx`

---

## 🧹 Cleanup
- `docker system prune`  
  Remove all stopped containers, unused networks, dangling images, and build cache.
- `docker volume prune`  
  Remove all unused volumes.
- `docker image prune`  
  Remove dangling images only.

---

## 📄 Sample Dockerfile

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## 🧩 Sample docker-compose.yml

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```

---

## 🔐 Environment Variables

- Store secrets in a `.env` file:
  ```
  DEBUG=true
  SECRET_KEY=mysecret
  ```
- Docker Compose automatically loads `.env`.

---

## 🧠 Handy Aliases

Add to your `.bashrc` or `.zshrc`:

```bash
alias dps="docker ps"
alias dpa="docker ps -a"
alias di="docker images"
alias drm="docker rm"
alias drmi="docker rmi"
alias dcu="docker-compose up"
alias dcd="docker-compose down"
alias db="docker build -t"
```

---

## 📚 Resources
- [Official Docker Documentation](https://docs.docker.com/)