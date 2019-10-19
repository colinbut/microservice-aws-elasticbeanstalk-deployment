#!/bin/bash

git clone https://github.com/colinbut/microservice-nodejs.git
cd microservice-nodejs
zip microservice-nodejs.zip *
eb deploy