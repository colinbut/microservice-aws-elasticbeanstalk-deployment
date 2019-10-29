from string import Template
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("project_name", help="the name of the microservice project")
parser.add_argument("docker_tag", help="the tag of the docker image to deploy")
parser.add_argument("container_port", help="the container port for the docker container")
parser.add_argument("host_port", help="the host port for the docker container")
args = parser.parse_args()

vars = {
    "project_name" : args.project_name,
    "docker_tag" : args.docker_tag,
    "constainer_port" : args.container_port,
    "host_port" : args.host_port
}

DockerrunAWSJsonTemplate = """{
    \"AWSEBDockerrunVersion\": \"1\",
    \"Image\": {
        \"Name\": \"066203203749.dkr.ecr.eu-west-2.amazonaws.com/$project_name:$docker_tag\",
        \"Update\": true
    },
    \"Ports\": [
        {
            \"ContainerPort\": $constainer_port,
            \"HostPort\": $host_port
        }
    ]
}
"""

file = Template(DockerrunAWSJsonTemplate).substitute(vars)

with open("Dockerrun.aws.json", "w") as DockerrunAWSJsonFile:
    DockerrunAWSJsonFile.write(file)

subprocess.call(['eb', 'deploy'])