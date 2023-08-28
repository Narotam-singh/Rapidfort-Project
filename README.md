# Rapidfort-Project

# Getting Started  
**Prerequistes**  
1. Flask (backend)
2. Docker (Containerisation)
3. Kubectl ( for Local Kuberentes Deployment)

**Cloning Repository**  
  
```git clone https://github.com/Narotam-singh/Rapidfort-Project```  

**Installing Docker Desktop**  

  https://www.docker.com/products/docker-desktop/

**Building Docker File**

```docker build -t image-name:tag path-to-dockerfile-directory```

**Installing Kubectl(Minikube)**  

  https://minikube.sigs.k8s.io/docs/start/  
  
**Creating Kuberenetes Manifest Files**  

  ```kubectl apply -f deployment.yaml``` 
  
  ```kubectl apply -f service.yaml```
  
**Running the Application Locally**  

  ```minikube service rapidfort-project```
  
  
  


