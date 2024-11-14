# FastAPI Kubernetes Deployment with Argo CD and GitHub Actions

This repository automates the deployment of a FastAPI application on a Kubernetes cluster using Argo CD for continuous deployment and GitHub Actions for CI/CD.

## Prerequisites

- **Docker**: To build and test Docker images locally.
- **Minikube** or **Kubernetes Cluster**: For running Kubernetes locally or in the cloud.
- **kubectl**: Kubernetes CLI for applying and managing cluster resources.
- **Argo CD**: For continuous deployment on Kubernetes.
- **GitHub Actions**: For CI/CD automation.ps to create an python fast api app and create CICD pipeline to deploy the app on kubernetes with argo cd.

### A typical top-level directory description

### REPO: python-app

    ├── .github
        ├── workflows
            ├──ci.yml   #CI-CD file 
    ├── fastapi-app       # Folder for keeping any templates for build and deployment of the fast api app
        ├── Dockerfile    # Dockerfile for fast api app
        ├── main.py       # main app file
        ├── test-main.py   # unit test file for app
        ├── requirement.txt  #packages for app
    ├── k8s              # all kubernetes templates yaml files
        ├── deployment.yaml   
        ├── service.yaml   
        ├── namespace.yaml  
        ├── argo-cd.yaml  
    └── README.mdww


## Setup Instructions

**Once you have pushed all code and k8s manifest files and ci.yml CICD file to the repo**

### 1. Install minikube and start minikube and install argo-cd
- brew install minikube
- minikube start --cpus=4 --memory=8192
- kubectl create namespace argocd
- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
- kubectl port-forward svc/argocd-server -n argocd 8080:443

### 2. Login to argo ui using username: admin and get the password using below command and use port fowarding to access the ui at 'https://localhost:8080/'
- kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d\n
- kubectl port-forward svc/argocd-server -n argocd 8080:443


### 3. Use the argo-cd.yaml to deploy the app and see the deployment under argo ui
- kubectl apply -f argo-cd.yaml

### 4. CICD setup is done
- Now whenever you make any changes in this repo the CICD will be triggered automatically and starts executing and from argo ui you can see the latest changes.
