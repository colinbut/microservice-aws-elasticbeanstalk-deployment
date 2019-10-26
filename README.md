# Microservice AWS Elastic Beanstalk Deployment


## Deployment

### Containerized Microservice

#### Pre-requisities

_Need to give your instances with permission to access the docker images stored in Amazon ECR repository by adding permissions to your environment's instance profile. Can attach the __AmazonEC2ContainerRegistryReadOnly__ managed policy to the instance profile to provide read-only access to all Amazon ECR repositories... as specified in the AWS Elastic Beanstalk Documentations._

__Steps__:

1. go to containerized directory of this repo and update the docker image in the `Dockerrun.aws.json` file

2. Run the following deployment command of the eb cli:
   
```bash
eb deploy
```

### Non-Containerized Microservice

1. go to non-containerized folder of this project and run following script:

```bash
deploy.sh
```
