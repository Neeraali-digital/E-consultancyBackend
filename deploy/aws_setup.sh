#!/bin/bash

# AWS Deployment Setup Script for E-Consultancy Backend

echo "Setting up AWS deployment for E-Consultancy Backend..."

# 1. Create RDS PostgreSQL instance
echo "Creating RDS PostgreSQL instance..."
aws rds create-db-instance \
    --db-instance-identifier econsultancy-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username postgres \
    --master-user-password YourSecurePassword123 \
    --allocated-storage 20 \
    --vpc-security-group-ids sg-xxxxxxxxx \
    --db-name econsultancy \
    --backup-retention-period 7 \
    --storage-encrypted

# 2. Create S3 bucket for media files
echo "Creating S3 bucket for media files..."
aws s3 mb s3://econsultancy-media-bucket --region us-east-1

# 3. Create Elastic Beanstalk application
echo "Creating Elastic Beanstalk application..."
aws elasticbeanstalk create-application \
    --application-name econsultancy-backend \
    --description "E-Consultancy Django REST API Backend"

# 4. Create Elastic Beanstalk environment
echo "Creating Elastic Beanstalk environment..."
aws elasticbeanstalk create-environment \
    --application-name econsultancy-backend \
    --environment-name econsultancy-prod \
    --solution-stack-name "64bit Amazon Linux 2 v3.4.0 running Python 3.9" \
    --option-settings \
        Namespace=aws:autoscaling:launchconfiguration,OptionName=InstanceType,Value=t3.small \
        Namespace=aws:elasticbeanstalk:application:environment,OptionName=DJANGO_SETTINGS_MODULE,Value=eConsultancy.settings_prod

echo "AWS resources are being created. This may take several minutes..."
echo "Please update your .env file with the actual AWS resource details once they're ready."