# 🐳 Advanced Docker Guide

## 🔗 Docker Swarm (Orchestration)

### Enable Swarm
```bash
docker swarm init
```

### Add a worker node (token will be generated after `init`)
```bash
docker swarm join --token <token> <manager_ip>:2377
```

### Create a service
```bash
docker service create --name web --replicas 3 -p 80:80 nginx
```

### List services
```bash
docker service ls
```

### Scale service
```bash
docker service scale web=5
```

### Remove a service
```bash
docker service rm web
```

---

## 🔐 Docker Secrets

### Create a secret
```bash
echo "my_password" | docker secret create db_password -
```

### List secrets
```bash
docker secret ls
```

### Use secret in Docker Compose
```yaml
services:
  db:
    image: postgres
    secrets:
      - db_password

secrets:
  db_password:
    external: true
```

---

## 🔄 CI/CD Integration (Example with GitHub Actions)

```yaml
# .github/workflows/docker.yml
name: Build and Push Docker Image

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Log in to Docker Hub
      run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

    - name: Build the Docker image
      run: docker build -t myuser/myapp:latest .

    - name: Push the Docker image
      run: docker push myuser/myapp:latest
```

---

## 💻 VS Code Integration

### 1. Install Extension
Install the **Docker extension** from the VS Code Marketplace.

### 2. Add devcontainer support
```bash
mkdir .devcontainer
```

### 3. Sample `devcontainer.json`
```json
{
  "name": "Python Dev",
  "image": "python:3.10",
  "workspaceFolder": "/workspace",
  "mounts": ["source=${localWorkspaceFolder},target=/workspace,type=bind"],
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  }
}
```

### 4. Open folder in container
`F1 → Remote-Containers: Reopen in Container`

---

## 🧠 Bonus Tips

- Use `--mount` instead of `-v` for better readability in volumes.
- Use `docker stats` to monitor container resource usage.
- Use `docker inspect <name/id>` to get full container details.

---

## 📚 Resources

- [Docker Swarm](https://docs.docker.com/engine/swarm/)
- [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [VS Code + Docker](https://code.visualstudio.com/docs/containers/overview)