# Deployment Guide

## Deployment Options

### Local Development
```bash
uvicorn main:app --reload
```

### Docker Deployment

Build and run:
```bash
docker build -t mindfighter-api .
docker run -p 8000:8000 mindfighter-api
```

### Docker Compose
```bash
docker-compose up -d
```

### Cloud Deployment

#### Heroku
```bash
heroku create your-app-name
git push heroku main
```

#### AWS Elastic Beanstalk
```bash
eb init
eb create
eb deploy
```

#### Google Cloud Run
```bash
gcloud run deploy mindfighter-api --source .
```

#### Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
```

## Health Checks

Verify deployment:
```bash
curl http://your-app-url/
```