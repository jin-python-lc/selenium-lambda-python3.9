# Diagram
![image](https://user-images.githubusercontent.com/85344890/178254825-a9d970d0-083c-4123-bb8e-e3641bc3c6a9.png)

# Codebuild Setup

## Environment Image
docker:dind

## Environment Variable
HTTPS_PROXY：proxy  
HTTP_PROXY：proxy  
NO_PROXY：localhost, 169.254.169.254, 169.254.170.2, endpoints  
REPOSITORY_NAME：ECR repository name  
LAMBDA_FUNCTION_NAME：Lambda function name  
