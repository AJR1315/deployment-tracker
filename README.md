# Deployment Tracker

A REST API for tracking deployment history across environments.

## Current Status

🚧 Work in progress - Building as part of DevOps portfolio project

✅ Python REST API with FastAPI

- Create deployment records (POST /deployments)
- List all deployments (GET /deployments)
- Get single deployment by ID (GET /deployments/{id})
- Health check endpoint

### Completed

- [x] Python REST API with CRUD operations
- [x] PostgreSQL database integration
- [x] Docker containerisation
- [x] Local Kubernetes deployment
- [ ] Terraform infrastructure provisioning
- [ ] CI/CD pipeline with GitHub Actions

## Why This Project?

This project gives me a chance to learn Python, APIs, Terraform, Git, GitHub Actions, as well as many other in-demand skills. I have had the chance to be hands-on with many of these through my work; however, to be able to take the time and sit down to learn each of these without using AI to write for me or spending hours reading pages of documentation without getting hands-on was the main reason for this project.

## Architecture

[Architecture diagram and explanation to be added as the project develops]

## Running the Application

### Option 1: Using Docker (Recommended)

The easiest way to run everything - no Python setup required.

**Prerequisites:**

- Docker Desktop installed
- Git

**Steps:**

1. **Clone the repository**

```bash
   git clone https://github.com/yourusername/deployment-tracker.git
   cd deployment-tracker
```

2. **Build and start the application**

```bash
   docker-compose up --build
```

This starts both PostgreSQL and the API in containers.

To run in background:

```bash
   docker-compose up -d --build
```

To view logs when running in background:

```bash
   docker-compose logs -f app
```

3. **Stopping the application**

```bash
   # If running in foreground: Ctrl+C

   # If running in background:
   docker-compose down

   # To also remove database data (fresh start):
   docker-compose down -v
```

### Option 2: Local Development (Without Docker for the app)

Use this when actively developing - gives you hot-reloading.

**Prerequisites:**

- Python 3.9+ installed
- Docker Desktop (for PostgreSQL)
- Git

**Steps:**

1. **Clone the repository**

```bash
   git clone https://github.com/yourusername/deployment-tracker.git
   cd deployment-tracker
```

2. **Start the database**

```bash
   docker-compose up -d postgres
```

Note: `postgres` specifies only the database service, not the app.

3. **Create and activate virtual environment**

```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install dependencies**

```bash
   pip install -r app/requirements.txt
```

5. **Run the application**

```bash
   uvicorn app.src.main:app --reload
```

### Option 3: Using Kubernetes (Locally)

For testing Kubernetes locally.

**Prerequisites:**

- Docker Desktop installed
- minikube installed
- kubectl command line installed

**Steps:**

1. **Clone the repository**

```bash
   git clone https://github.com/yourusername/deployment-tracker.git
   cd deployment-tracker
```

2. **Start minikube**

```bash
   minikube start
```

3. **Build the Docker image for minikube**

```bash
   # Point your terminal to minikube's Docker
   eval $(minikube docker-env)
```

```bash
   # Build the image
   docker build -t deployment-tracker-app:latest ./app
```

4. **Apply the /kubernetes .yaml files**

```bash
   kubectl apply -f kubernetes
```

5. **Access the application**

```bash
   # Use this to grab the URL that minikube assigns if using Kubernetes
   minikube service deployment-tracker-app -n deployment-tracker --url
```

**Useful Commands:**

```bash
   # See everything in the namespace
   kubectl get all -n deployment-tracker
```

```bash
   # View logs from the app
   kubectl logs -n deployment-tracker -l app=deployment-tracker-app
```

```bash
   # View logs from postgres
   kubectl logs -n deployment-tracker -l app=postgres
```

```bash
   # Restart a deployment (if you wish to rebuild the image)
   kubectl rollout restart deployment/deployment-tracker-app -n deployment-tracker
```

```bash
   # Delete and start a fresh
   kubectl delete -f kubernetes/
```

## Using the Application

Once running (via either method), access:

- **Interactive API docs**: http://127.0.0.1:8000/docs
- **API root**: http://127.0.0.1:8000/
- **Health check**: http://127.0.0.1:8000/health

### Available Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /deployments` - List all deployments
- `GET /deployments/{id}` - Get specific deployment by ID
- `POST /deployments` - Create new deployment record

### Verifying Data Persistence

1. Create a few deployments via POST `/deployments`
2. List them with GET `/deployments`
3. Stop and restart the application
4. List deployments again - they should still be there

### Inspecting the Database (Optional)

To view data directly in PostgreSQL:

```bash
docker exec -it deployment-tracker-db psql -U devops -d deployments
```

Once connected:

```sql
SELECT * FROM deployments;
```

Exit with `\q`
