## Running Locally

### Prerequisites

- Python 3.9+ installed
- Docker Desktop installed
- Git (to clone the repository)

### Setup

1. **Clone the repository**

```bash
   git clone https://github.com/yourusername/deployment-tracker.git
   cd deployment-tracker
```

2. **Start the PostgreSQL database**

```bash
   docker-compose up -d
```

This starts PostgreSQL in a Docker container. The `-d` flag runs it in the background.

Verify it's running:

```bash
   docker-compose ps
```

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

The `--reload` flag enables hot-reloading - the server automatically restarts when you save changes to your code.

### Using the Application

Once running, the terminal will display:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Available URLs:**

- **Interactive API docs**: http://127.0.0.1:8000/docs
- **API root**: http://127.0.0.1:8000/
- **Health check**: http://127.0.0.1:8000/health

The `/docs` endpoint provides an interactive interface where you can test all API endpoints directly in your browser.

### Available Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /deployments` - List all deployments
- `GET /deployments/{id}` - Get specific deployment by ID
- `POST /deployments` - Create new deployment record

### Verifying Data Persistence

To confirm your deployments are stored in the database:

1. Create a few deployments via POST `/deployments`
2. List them with GET `/deployments`
3. Stop the application (Ctrl+C)
4. Restart it (`uvicorn app.src.main:app --reload`)
5. List deployments again - they should still be there

### Inspecting the Database (Optional)

To view data directly in PostgreSQL:

```bash
docker exec -it deployment-tracker-db psql -U devops -d deployments
```

Once connected, run:

```sql
SELECT * FROM deployments;
```

Exit with `\q`

### Stopping Everything

```bash
# Stop the application: Ctrl+C in the terminal running uvicorn

# Stop the database:
docker-compose down

# Stop and remove all data (fresh start):
docker-compose down -v
```
