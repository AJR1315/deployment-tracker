# Deployment Tracker

A REST API for tracking deployment history across environments.

## Current Status

🚧 Work in progress - Building as part of DevOps portfolio project

### Completed

- [x] Python REST API with CRUD operations
- [x] PostgreSQL database integration
- [x] Docker containerisation
- [x] Local Kubernetes deployment
- [ ] Terraform infrastructure provisioning (AWS EKS)
- [ ] CI/CD pipeline with GitHub Actions

## About This Project

A portfolio project demonstrating end-to-end DevOps skills: building a REST API, containerising it, deploying to Kubernetes, provisioning infrastructure with Terraform, and automating everything with CI/CD.

### Why I Built This

This project gives me a chance to learn Python, APIs, Terraform, Git, GitHub Actions, and other in-demand DevOps skills hands-on. While I've used many of these tools at work, I wanted to build something from scratch without relying on AI to write the code for me - to genuinely understand each technology rather than just copy-pasting solutions.

### Technologies Used

- **Application:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Containerisation:** Docker, Docker Compose
- **Orchestration:** Kubernetes
- **Infrastructure as Code:** Terraform (AWS EKS)
- **CI/CD:** GitHub Actions

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        AWS Cloud                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                    EKS Cluster                             │  │
│  │  ┌─────────────────┐      ┌─────────────────┐             │  │
│  │  │   App Pod       │      │  PostgreSQL Pod │             │  │
│  │  │  ┌───────────┐  │      │  ┌───────────┐  │             │  │
│  │  │  │  FastAPI  │  │─────▶│  │  Postgres │  │             │  │
│  │  │  │   :8000   │  │      │  │   :5432   │  │             │  │
│  │  │  └───────────┘  │      │  └───────────┘  │             │  │
│  │  └─────────────────┘      └─────────────────┘             │  │
│  │           │                        │                       │  │
│  │           │                        │                       │  │
│  │      ┌────┴────┐            ┌──────┴──────┐               │  │
│  │      │ Service │            │     PVC     │               │  │
│  │      │NodePort │            │  (Storage)  │               │  │
│  │      └────┬────┘            └─────────────┘               │  │
│  └───────────┼───────────────────────────────────────────────┘  │
│              │                                                   │
└──────────────┼───────────────────────────────────────────────────┘
               │
         ┌─────┴─────┐
         │  Client   │
         │ (Browser) │
         └───────────┘
```

## API Endpoints

| Method | Endpoint            | Description           |
| ------ | ------------------- | --------------------- |
| `GET`  | `/`                 | API information       |
| `GET`  | `/health`           | Health check          |
| `GET`  | `/deployments`      | List all deployments  |
| `GET`  | `/deployments/{id}` | Get deployment by ID  |
| `POST` | `/deployments`      | Create new deployment |

### Example Request

```bash
curl -X POST "http://localhost:8000/deployments" \
  -H "Content-Type: application/json" \
  -d '{
    "service_name": "user-api",
    "version": "v1.0.0",
    "environment": "production",
    "status": "success",
    "deployed_by": "ashley"
  }'
```

### Example Response

```json
{
  "id": 1,
  "service_name": "user-api",
  "version": "v1.0.0",
  "environment": "production",
  "status": "success",
  "deployed_by": "ashley",
  "deployed_at": "2025-11-21T15:08:38.902638"
}
```

## Running the Application

### Option 1: Docker Compose (Recommended)

The simplest way to run everything locally.

**Prerequisites:**

- Docker Desktop

**Steps:**

```bash
# Clone the repository
git clone https://github.com/yourusername/deployment-tracker.git
cd deployment-tracker

# Build and start
docker-compose up --build

# Or run in background
docker-compose up -d --build

# View logs
docker-compose logs -f app

# Stop
docker-compose down

# Stop and remove all data
docker-compose down -v
```

**Access:** http://localhost:8000/docs

---

### Option 2: Local Development

For active development with hot-reloading.

**Prerequisites:**

- Python 3.9+
- Docker Desktop (for PostgreSQL)

**Steps:**

```bash
# Clone the repository
git clone https://github.com/yourusername/deployment-tracker.git
cd deployment-tracker

# Start database only
docker-compose up -d postgres

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r app/requirements.txt

# Run with hot-reload
uvicorn app.src.main:app --reload
```

**Access:** http://localhost:8000/docs

---

### Option 3: Local Kubernetes (minikube)

For testing Kubernetes deployment locally.

**Prerequisites:**

- Docker Desktop
- minikube
- kubectl

**Steps:**

```bash
# Start minikube
minikube start

# Build image in minikube's Docker
eval $(minikube docker-env)
docker build -t deployment-tracker-app:latest ./app

# Deploy
kubectl apply -f kubernetes/

# Get URL
minikube service deployment-tracker-app -n deployment-tracker --url
```

**Useful Commands:**

```bash
# View all resources
kubectl get all -n deployment-tracker

# View app logs
kubectl logs -n deployment-tracker -l app=deployment-tracker-app

# View database logs
kubectl logs -n deployment-tracker -l app=postgres

# Restart app deployment
kubectl rollout restart deployment/deployment-tracker-app -n deployment-tracker

# Delete everything
kubectl delete -f kubernetes/
```

## Project Structure

```
deployment-tracker/
├── app/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI application
│   │   ├── models.py        # SQLAlchemy models
│   │   └── database.py      # Database configuration
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── kubernetes/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── postgres-pvc.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── app-deployment.yaml
│   └── app-service.yaml
├── terraform/               # Coming soon
├── .github/
│   └── workflows/           # Coming soon
├── docker-compose.yml
└── README.md
```

## Development Notes

### Verifying Data Persistence

1. Create deployments via `POST /deployments`
2. List them with `GET /deployments`
3. Restart the application
4. Verify data persists

### Inspecting the Database

```bash
# Connect to PostgreSQL
docker exec -it deployment-tracker-db psql -U devops -d deployments

# Query deployments
SELECT * FROM deployments;

# Exit
\q
```

## License

MIT
