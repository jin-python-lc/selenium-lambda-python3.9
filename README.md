# selenium-lambda-python3.9

## Diagram

## Codebuild Setup

### Environment Image
docker:dind

### Environment Variable of Codebuild Buildproject
HTTPS_PROXY：proxy
HTTP_PROXY：proxy
NO_PROXY：localhost, 169.254.169.254, 169.254.170.2, endpoints
REPOSITORY_NAME：ECR repository name
LAMBDA_FUNCTION_NAME：Lambda function name