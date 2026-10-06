#!/usr/bin/env bash
# Deploy the CloudFormation stacks in order (network, data, app).
set -euo pipefail

rm -rf build
mkdir -p build/lambda-package
cp backend/directory_api/handler.py build/lambda-package
cp backend/directory_api/filtering.py build/lambda-package
cp backend/directory_api/validate.py build/lambda-package
cp data/directory/services.json build/lambda-package
cd build/lambda-package
zip -r ../lambda.zip .
cd ../..
outputs=$(aws cloudformation describe-stacks --stack-name ithemba-data --query "Stacks[0].Outputs")
bucket=$(echo "$outputs" | jq -r '.[] | select(.OutputKey=="DeploymentBucketName") | .OutputValue')
aws s3 cp build/lambda.zip "s3://$bucket/lambda.zip"