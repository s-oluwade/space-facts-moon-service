#!/bin/bash

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 533266979424.dkr.ecr.us-east-1.amazonaws.com
aws ecr create-repository --repository-name moon-facts-service
docker build -t moon-facts-service .
docker tag moon-facts-service:latest 533266979424.dkr.ecr.us-east-1.amazonaws.com/moon-facts-service:latest
docker push 533266979424.dkr.ecr.us-east-1.amazonaws.com/moon-facts-service:latest
docker rmi 533266979424.dkr.ecr.us-east-1.amazonaws.com/moon-facts-service:latest