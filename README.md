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

- [ ] Python REST API with CRUD operations
- [ ] PostgreSQL database integration
- [ ] Docker containerisation
- [ ] Local Kubernetes deployment
- [ ] Terraform infrastructure provisioning
- [ ] CI/CD pipeline with GitHub Actions

## Why This Project?

This project gives me a chance to learn Python, APIs, Terraform, Git, GitHub actions, as well as many other in-demand skills. I have had the chance to be hands-on with many of these through my work; however, to be able take the time and sit-down to learn each of these without using AI to write for me or spending hours reading pages of documentation without getting hands on was the main reason for this project.

## Architecture

[You add this as you build - start simple, expand as you go]

## Running Locally

### Prerequisites

- Python 3.9 or above installed.
- Git (to clone the repository)

### Setup

1. Clone repository:

```bash
   git clone https://github.com/yourusername/deployment-tracker.git
   cd ./deployment-tracker/
```

2. Create and activate your virtual environment

```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install requirements

```bash
   pip install -r app/requirements.txt
```

4. Run Uvicorn app

```bash
   uvicorn app.src.main:app --reload
```

--reload allows for the app to restart when changes are detected

### Using the app

App can be accessed via the address as stated after booting:

INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

Visit http://127.0.0.1:8000/docs#/ to find all the API endpoints and test.
