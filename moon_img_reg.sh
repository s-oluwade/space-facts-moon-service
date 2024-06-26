#!/bin/bash

docker tag moon-facts-service:latest 533266979424.dkr.ecr.us-east-1.amazonaws.com/moon-facts-service:latest
docker push 533266979424.dkr.ecr.us-east-1.amazonaws.com/moon-facts-service:latest
