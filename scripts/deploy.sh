#!/usr/bin/env bash
# Deploy the CloudFormation stacks in order (network, data, app).
set -euo pipefail

rm -rf build/lambda-package
rm -rf build
mkdir -p build/lambda-package
cp backend/directory_api/handler.py build/lambda-package
cp backend/directory_api/filtering.py build/lambda-package
cp backend/directory_api/validate.py build/lambda-package
cp data/directory/services.json build/lambda-package
cd build/lambda-package
zip -r ../lambda.zip .