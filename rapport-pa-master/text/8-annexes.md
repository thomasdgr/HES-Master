# Annexes

## Chatbot

This microservice, produced by Thomas Dagier for Master MSE PA aims to expose a chatbot for HEIA-FR students. The chatbot is available [here](https://chatbot.kube.isc.heia-fr.ch/showcase).

See repport for further informations about the application and the technologies used.

The specification file is defined according to openapi v3 (OAS3).

## Running the web service - linux / mac

The web api is in the folder `/api_rest/`. I used uvicorn and fastapi for the development. You may use an own
Python virtual environment in the `/api_rest/` folder installing the python modules from `/api_rest/requirements.txt`.

- Tools should work with python3.They were used with **python 3.7**, **python 3.8** and **python 3.9**.
- Clone the repository, create virtualenv, activate the virtual env, install required packages and test.

```sh
  python3 -m venv venv
  source ./venv/bin/activate
  pip install --upgrade pip
  pip install -r ./api_rest/requirements.txt
  export OPENAI_API_KEY="YOUR_API_KEY"
  uvicorn api_rest.main:rootapp --reload
```

The OpenAPI specifications are available under the route `/specification` and the Swagger interface to test the API under the route `/docs`. The showcase is under the route `/showcase`.

## How to launch the tool with docker image on Linux

Make sure docker is installed. Follow instructions [here](https://docs.docker.com/get-docker/) to install docker.

```sh
  docker build -t registry.forge.hefr.ch/thomas.dagierjo/pa-chatbot/
                  pa-chatbot:latest .
  docker run -it -p 8000:8000 registry.forge.hefr.ch/thomas.dagierjo/pa-chatbot/
                  pa-chatbot:latest   
```

To quit the docker image, use `exit`

## How to deploy on Kubernetes

Preliminary steps: you need to check that you are connected to the K8S iCoSys cluster with a ``kubectl version --short``. For that you need to
create a file in your path ``~/.kube/config`` with the cluster Kubeconfig file that you find under you cluster on ``https://rancher.kube.isc.heia-fr.ch/``.

You need to create a Docker images that is then pushed on Gitlab Container Registry, our repository of images. Then scripts are used to let Kubernetes deploy a service from the pushed image stored on Gitlab Container Registry.

### Dockerisation on Gitlab Container Registry

One important step is to build the Docker image with a proper tag. The parts of the tag will be used by the deployment scripts. In our case, the tag is :
``registry.forge.hefr.ch/thomas.dagierjo/pa-chatbot/pa-chatbot:latest``

Where the first part defines the container registry (``registry.forge.hefr.ch``), the second part defines the namespace (``thomas.dagierjo/pa-chatbot``), the third part defines the image name (``pa-chatbot:latest``) and the last part the version number that will be incremented when new versions of the langid will be done (``dev``). So the building of the image is done with ``docker build -t registry.forge.hefr.ch/thomas.dagierjo/pa-chatbot/pa-chatbot:latest .``. You need to login to Gitlab Container Registry from Docker so that when you do a docker push, it is pushed on
Gitlab Container Registry. The login is done with ``docker login registry.forge.hefr.ch``. The push is then done with ``docker push registry.forge.hefr.ch/thomas.dagierjo/pa-chatbot/pa-chatbot:latest`` After that your image should be visible [here](https://gitlab.forge.hefr.ch/thomas.dagierjo/pa-chatbot/container_registry/).

\pagebreak

### Deployment on K8S

To let K8S pull these images, you should create a secret in the cluster with your credentials to reach the image. I did it with `kubectl -n ragfish create secret docker-registry my-secret --docker-server=registry.forge.hefr.ch --docker-username=XXX --docker-password=XXX`.

The `XXX` docker-password must be changed with the token created on Gitlab Container Registry. You create it [here](https://gitlab.forge.hefr.ch/-/profile/personal_access_tokens). You need to check the `read_registry` box at least.

The first time you deploy on K8S, you need to `kubectl apply` the config files like that:

```sh
kubectl apply -f api_rest/deploy.yaml
```

After this, you may want to have a look in the Rancher [web interface](https://rancher.k8s.tic.heia-fr.ch/) to make sure everything is correctly deployed and running.

For any issue, please refer to the following [documentation](https://clusterdoc.kube.isc.heia-fr.ch/getting-started/deployment-application/).

### Deployment on K8S with Gitlab CI

A CI/CD pipeline is set up within Gitlab's project to facilitate the building of a Docker image and its deployment on Kubernetes (K8S). Our development workflow involves two environments: a dev environment for working on new and revised software code, and a staging environment for deploying software into production. You can access the configuration details [here](https://gitlab.forge.hefr.ch/thomas.dagierjo/pa-chatbot/-/blob/main/.gitlab-ci.yml).

## Using the service

When the deployment is done, you can access the service [here](http://chatbot.kube.isc.heia-fr.ch/showcase)

\pagebreak

## Ollama Server Deployment

Done by Thomas Dagier & Sam Corpataux in May 2024.

### Script to deploy ollama on kubernetes

First, make sure you configured your kubectl to point to the right cluster.
Config should be in `~/.kube/config` or you can use `kubectl config use-context <context>` to switch context.

### Using kubectl

To deploy the application, run the following command:
```bash
kubectl apply -f deploy.yaml
```

### Testing the deployment

First, you'll need to pull a model:
```bash
curl https://ollama.kube.isc.heia-fr.ch/api/pull -d '{
  "name": "mistral"
}'
```

Then, you can generate text using the following command:
```bash
curl https://ollama.kube.isc.heia-fr.ch/api/generate -d '{
  "model": "mistral",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

### Monitoring the deployment

To check the GPU RAM available, you can run the following command:
```bash 
ssh checkgpu@icolab-gpu-6.isc.heia-fr.ch
ssh checkgpu@icolab-gpu-10.isc.heia-fr.ch
```

Warning: This will show how much RAM is not used, not how much is available for reservation.
This is why, if the command shows 14000 Mib are available, you can't reserve 55*256 Mib during the deployment.

### Opened issues

- [X] Issue with nginx, we need to switch port manually and randomly
- [ ] Not enough GPU RAM (max tencent.com/vcuda-memory: 20 so 20*256= 5120) to hold the weights of Llama3 for example
- [ ] Not that fast (however, Phi3 is faster than Llama3)

### Documentation

- [K8s ISC Cluster Documentation](https://clusterdoc.kube.isc.heia-fr.ch/gpu/specify-gpu-deployment/)
- [Ollama Helm Chart](https://github.com/otwld/ollama-helm)
- [An example to serve Ollama on Kubernetes cluster](https://medium.com/@erdkse/have-your-llm-api-on-your-kubernetes-cluster-38caa59ea6eb)

### Deployment script

```yaml
# SERVICE
---
apiVersion: v1
kind: Service
metadata:
  name: ollama
  namespace: ollama-namespace
spec:
  type: ClusterIP
  selector:
    name: ollama
  ports:
    - protocol: TCP
      port: 80
      targetPort: 11434

# DEPLOY
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama
  namespace: ollama-namespace
spec:
  selector:
    matchLabels:
      name: ollama
  template:
    metadata:
      labels:
        name: ollama
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                - key: kubernetes.io/hostname
                  operator: In
                  values:
                    - icolab-gpu-10
      containers:
      - name: ollama
        image: ollama/ollama:latest
        ports:
        - name: http
          containerPort: 11434
          protocol: TCP
        resources:
          requests:
            tencent.com/vcuda-core: 10 # 10 % of CUDA cores
            tencent.com/vcuda-memory: 20 # 20 * 256MiB = 5120MiB
          limits:
            tencent.com/vcuda-core: 10
            tencent.com/vcuda-memory: 20

# INGRESS
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ollama-ingress
  annotations:
    nginx.ingress.kubernetes.io/use-regex: 'true'
    nginx.ingress.kubernetes.io/rewrite-target: /$1
    nginx.ingress.kubernetes.io/ssl-redirect: 'true'
    nginx.ingress.kubernetes.io/proxy-body-size: 20m
    nginx.ingress.kubernetes.io/proxy-connect-timeout: '3600'
    nginx.ingress.kubernetes.io/proxy-read-timeout: '3600'
    nginx.ingress.kubernetes.io/proxy-send-timeout: '3600'
  namespace: ollama-namespace
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - ollama.kube.isc.heia-fr.ch
      secretName: tls-secret
  rules:
    - host: ollama.kube.isc.heia-fr.ch
      http:
        paths:
          - path: /(.*)
            pathType: ImplementationSpecific
            backend:
              service:
                name: ollama
                port:
                  number: 11434
```


\pagebreak