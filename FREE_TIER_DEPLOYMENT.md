# AWS Free Tier Deployment Guide

## Free Tier Resources Used
- **EC2 t2.micro** (750 hours/month free)
- **RDS db.t2.micro** (750 hours/month free)
- **S3** (5GB storage free)
- **Elastic Beanstalk** (no additional cost)

## Step 1: Install AWS CLI and EB CLI

```bash
pip install awscli awsebcli
aws configure
```

## Step 2: Create Free Tier RDS Database

```bash
aws rds create-db-instance \
    --db-instance-identifier econsultancy-free \
    --db-instance-class db.t2.micro \
    --engine postgres \
    --master-username postgres \
    --master-user-password YourPassword123 \
    --allocated-storage 20 \
    --db-name econsultancy \
    --publicly-accessible \
    --no-multi-az \
    --storage-type gp2
```

## Step 3: Create S3 Bucket

```bash
aws s3 mb s3://econsultancy-media-free-tier
```

## Step 4: Deploy with Elastic Beanstalk

```bash
# Initialize EB
eb init -p python-3.9 econsultancy-backend --region us-east-1

# Create environment with t2.micro
eb create econsultancy-free --instance-type t2.micro --single-instance

# Set environment variables
eb setenv \
    SECRET_KEY=your-secret-key-here \
    DEBUG=False \
    DB_NAME=econsultancy \
    DB_USER=postgres \
    DB_PASSWORD=YourPassword123 \
    DB_HOST=your-rds-endpoint.amazonaws.com \
    ALLOWED_HOSTS=your-eb-url.elasticbeanstalk.com \
    USE_S3=TRUE \
    AWS_STORAGE_BUCKET_NAME=econsultancy-media-free-tier

# Deploy
eb deploy
```

## Step 5: Get RDS Endpoint

```bash
aws rds describe-db-instances --db-instance-identifier econsultancy-free --query 'DBInstances[0].Endpoint.Address'
```

## Free Tier Limitations
- **750 hours/month** for EC2 and RDS (31 days = 744 hours)
- **Single instance** only (no load balancing)
- **20GB** database storage
- **5GB** S3 storage

## Cost Monitoring
- Set up billing alerts in AWS Console
- Monitor usage in AWS Cost Explorer
- Stay within free tier limits to avoid charges