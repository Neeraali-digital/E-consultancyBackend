# AWS Deployment Guide

## Prerequisites

1. AWS CLI installed and configured
2. Docker installed (for containerized deployment)
3. Python 3.9+ and pip

## Deployment Options

### Option 1: AWS Elastic Beanstalk (Recommended)

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB application**
   ```bash
   eb init -p python-3.9 econsultancy-backend
   ```

3. **Create environment**
   ```bash
   eb create econsultancy-prod
   ```

4. **Set environment variables**
   ```bash
   eb setenv SECRET_KEY=your-secret-key \
            DB_NAME=econsultancy \
            DB_USER=postgres \
            DB_PASSWORD=your-password \
            DB_HOST=your-rds-endpoint \
            ALLOWED_HOSTS=your-domain.com
   ```

5. **Deploy**
   ```bash
   eb deploy
   ```

### Option 2: AWS ECS with Docker

1. **Build and push Docker image**
   ```bash
   docker build -t econsultancy-backend .
   docker tag econsultancy-backend:latest your-account.dkr.ecr.region.amazonaws.com/econsultancy:latest
   docker push your-account.dkr.ecr.region.amazonaws.com/econsultancy:latest
   ```

2. **Create ECS task definition and service**
   - Use AWS Console or CLI to create ECS resources
   - Configure environment variables in task definition

### Option 3: AWS Lambda (Serverless)

1. **Install Zappa**
   ```bash
   pip install zappa
   ```

2. **Initialize Zappa**
   ```bash
   zappa init
   ```

3. **Deploy**
   ```bash
   zappa deploy production
   ```

## Required AWS Resources

### 1. RDS PostgreSQL Database
```bash
aws rds create-db-instance \
    --db-instance-identifier econsultancy-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username postgres \
    --master-user-password YourPassword123 \
    --allocated-storage 20 \
    --db-name econsultancy
```

### 2. S3 Bucket for Media Files
```bash
aws s3 mb s3://econsultancy-media-files
```

### 3. Security Groups
- Allow HTTP/HTTPS traffic (ports 80, 443)
- Allow PostgreSQL traffic (port 5432) from application

## Environment Variables

Create `.env` file with:
```
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DB_NAME=econsultancy
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=your-rds-endpoint.amazonaws.com
DB_PORT=5432
USE_S3=TRUE
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=econsultancy-media-files
AWS_S3_REGION_NAME=us-east-1
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com
```

## Post-Deployment Steps

1. **Run migrations**
   ```bash
   python manage_prod.py migrate
   ```

2. **Create superuser**
   ```bash
   python manage_prod.py createsuperuser
   ```

3. **Collect static files**
   ```bash
   python manage_prod.py collectstatic
   ```

## Monitoring and Logging

- Use AWS CloudWatch for application logs
- Set up AWS CloudWatch alarms for monitoring
- Configure AWS X-Ray for distributed tracing

## Cost Optimization

- Use t3.micro instances for development
- Enable auto-scaling based on CPU/memory usage
- Use RDS reserved instances for production
- Implement S3 lifecycle policies for old media files

## Security Best Practices

- Use IAM roles instead of access keys when possible
- Enable VPC for network isolation
- Use AWS Secrets Manager for sensitive data
- Enable SSL/TLS certificates via AWS Certificate Manager
- Regular security updates and patches