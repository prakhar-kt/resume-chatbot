# 🐳 Docker Deployment Guide

This guide covers deploying your resume chatbot using Docker containers on various platforms.

## 🚀 Quick Local Testing

### Step 1: Build and Run Locally

```bash
# Create .env file
cp .env.example .env
# Edit .env with your actual API keys

# Build the Docker image
docker build -t resume-chatbot .

# Run the container
docker run -p 8000:8000 --env-file .env resume-chatbot

# Or use docker-compose (recommended)
docker-compose up --build
```

Visit `http://localhost:8000` to test your chatbot.

---

## ☁️ Cloud Deployment Options

### Option 1: Railway (Docker) - Recommended

Railway supports Docker deployments automatically.

1. **Add `railway.json`** to your project root:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE"
  },
  "deploy": {
    "healthcheckPath": "/health",
    "healthcheckTimeout": 100,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

2. **Deploy to Railway**:
   - Connect your GitHub repository
   - Railway auto-detects Dockerfile
   - Set environment variables in Railway dashboard
   - Deploy automatically!

### Option 2: Google Cloud Run

Google Cloud Run is perfect for containerized apps with automatic scaling.

1. **Install Google Cloud CLI**:

```bash
# macOS
brew install google-cloud-sdk

# Or download from: https://cloud.google.com/sdk/docs/install
```

2. **Setup and Deploy**:

```bash
# Login and set project
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/resume-chatbot

# Deploy to Cloud Run
gcloud run deploy resume-chatbot \
  --image gcr.io/YOUR_PROJECT_ID/resume-chatbot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars ANTHROPIC_API_KEY=your_key_here \
  --port 8000
```

3. **Get your public URL** from the output.

### Option 3: AWS ECS with Fargate

1. **Install AWS CLI and create ECR repository**:

```bash
# Create ECR repository
aws ecr create-repository --repository-name resume-chatbot

# Get login token
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
```

2. **Build and push image**:

```bash
# Build for ARM64 (Fargate)
docker build --platform linux/amd64 -t resume-chatbot .

# Tag and push
docker tag resume-chatbot:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/resume-chatbot:latest
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/resume-chatbot:latest
```

3. **Create ECS service** using AWS Console or Terraform.

### Option 4: DigitalOcean App Platform

1. **Create `app.yaml`**:

```yaml
name: resume-chatbot
services:
- name: web
  source_dir: /
  github:
    repo: your-username/resume-chatbot
    branch: main
  run_command: uv run uvicorn app:app --host 0.0.0.0 --port 8000
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  http_port: 8000
  health_check:
    http_path: /health
  envs:
  - key: ANTHROPIC_API_KEY
    scope: RUN_TIME
    type: SECRET
    value: your_api_key_here
```

2. **Deploy via DigitalOcean dashboard** or CLI.

---

## 🔧 Production Optimizations

### Multi-stage Dockerfile (Smaller Image)

Create `Dockerfile.prod`:

```dockerfile
# Build stage
FROM python:3.11-slim as builder

WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy only necessary files
COPY --from=builder /app/.venv /app/.venv
COPY . .

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose for Production

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.prod
    restart: unless-stopped
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    restart: unless-stopped

  # Optional: Redis for caching
  redis:
    image: redis:alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

---

## 📊 Monitoring and Logging

### Add Application Monitoring

1. **Health checks** are built into the Dockerfile
2. **Structured logging** - modify your app to use JSON logs:

```python
import logging
import json

# Add to app.py
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

def log_structured(level, message, **kwargs):
    log_data = {
        'timestamp': datetime.utcnow().isoformat(),
        'level': level,
        'message': message,
        **kwargs
    }
    logging.info(json.dumps(log_data))
```

### Monitoring Stack with Docker Compose

Create `docker-compose.monitoring.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    # ... your app config

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

---

## 🔐 Security Best Practices

### 1. Use Multi-stage Builds
- Smaller final image
- No build tools in production

### 2. Non-root User
- Already implemented in Dockerfile
- Reduces attack surface

### 3. Security Scanning

```bash
# Scan image for vulnerabilities
docker scout cves resume-chatbot

# Or use Trivy
trivy image resume-chatbot
```

### 4. Environment Variables

Never hardcode secrets in Dockerfile:

```dockerfile
# ❌ Bad
ENV ANTHROPIC_API_KEY=sk-ant1234...

# ✅ Good - use at runtime
ENV ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
```

---

## 🚀 CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy Resume Chatbot

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: docker build -t resume-chatbot .
    
    - name: Deploy to Railway
      uses: railwayapp/cli@v2
      with:
        token: ${{ secrets.RAILWAY_TOKEN }}
        command: up --detach
```

---

## 🎯 Quick Deployment Commands

### Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway up
```

### Google Cloud Run
```bash
gcloud run deploy --source .
```

### DigitalOcean
```bash
doctl apps create --spec app.yaml
```

---

## 🔍 Troubleshooting

### Common Docker Issues

1. **Build failures**:
   ```bash
   docker build --no-cache -t resume-chatbot .
   ```

2. **Port issues**:
   ```bash
   docker run -p 8000:8000 resume-chatbot
   ```

3. **Environment variables**:
   ```bash
   docker run --env-file .env resume-chatbot
   ```

4. **Check logs**:
   ```bash
   docker logs <container-id>
   ```

### Performance Tuning

1. **Use Alpine Linux** for smaller images
2. **Multi-stage builds** for production
3. **Health checks** for container orchestration
4. **Resource limits** in docker-compose

---

**🐳 Your containerized resume chatbot is ready for any cloud platform!**