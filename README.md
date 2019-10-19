# Microservice AWS Elastic Beanstalk Deployment


## Deployment

### Containerized Microservice

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
