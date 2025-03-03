# Docker for MLOPs
* A repo for all things related to Docker use for MLOPs.



## What is docker?
* An open platform for developing, shippping and running applications.
* Docker helps with scaling, efficiency and compatibility. 

## Why containers?
* Easier to sync project work between multiple developers, engineers, data scientists and the entire dev team! 

## What are containers?
* An efficent way to package applications with all necessary dependencies and configurations in a project, application, machine learning model, code base, you name it. 
* A container is essentially a “portable artifact”.
* This means you can easiy share and move this “package” to ANY ENVIRONMENT ANYWHERE.
* Development AND Deployment more efficient! 
* All configurations are there, in sync and seamless transition. 


### A simple container example
* Lets say you are moving to a new house. 
  * You package all of your belongings in a moving truck and move it to your new house and unpack it there. 
  * Same concept applies using Containers like Docker!

### A technical example
* Lets say you are Developer A and you are working locally on a windows machine developing a Data Science application/project. 
  * With any project you need a lot of dependencies such as:
    * Anaconda
    * MongoDB
    * Python packages
    * FastAPI
    * etc….

* Now lets say tomorrow another engineer or data scientist "Developer B" joins the team and is using a Linux or Mac machine. 
  * This developer will have to setup their OWN development environment using the same setup as developer #1. 

* What about the QA Team?
  * They often have to send a finalized project to QA server. 
  * The QA team has to install all dependencies on their own and what if their environment is not the same as developer A or developer B?
 
* Solution: Docker images and containers


# Docker Images vs. Containers -- Overview
* Both Docker Images and Docker Containers perform "virtualization".
  * At a high level as we mentioned above, many applications require multiple dependencies & configurations such as but not limited to:
    * MySQL
    * MongoDB (or another NoSQL DB)
    * Python (or other code dependencies)
    * ...etc..
   
![image](https://github.com/user-attachments/assets/22236ce3-d8f8-4a00-9917-f85f98458950)


## Docker Images
* This is a collection of containers which are called images.
* Images Workflow: 
    * Run image —> Container created —> Application environment runs
* Docker image
  * A package or artifact 
  * We can easily move or share this artifact

## Docker Containers
* Container: Docker image —> Run —> starts application —> creates container/environment 

* A combination of layers of images from the application such as:
  * MongoDB image
  * Anaconda image
  * Python image
  * Linux image
  * ...etc..
 


# Docker and Virtual Machine Images vs. Containers: Advantages and Disadvantages
* Lets say we have an operating system such as this:
```
* Application Layer <— Layer 2 (Most changes happen here in the application layer)
* OS kernel <— Layer 1
* Hardware (e.g. linux windows or Mac)
```

![image](https://github.com/user-attachments/assets/7b7540b1-fd1f-4ccf-a716-5f0ca74aada5)

[image source](https://hanwenzhang123.medium.com/docker-vs-virtual-machine-vs-kubernetes-overview-389db7de7618)

## Docker images
* Containerize the APPLICATION layer to communicate with the OS kernel 
* Host will be the OS Kernel

### Docker Images -- Advantages vs. Disadvantages 
1. Size —> SMALL, usually in `mb`
2. Run time is FAST —> Containers start & run much faster due to less layers
3. Compatability —> can’t run on just ANY OS...
  * example: Windows versions less than 10 can’t run Linux images, etc...

## Virtual Machines (VM) Images 
1. Containerize APPLICATION & OS kernel layers
2. Each has its own container
3. Host will be the APPLICATION & OS kernel which can communicate with the computer hardware

### Virtual Machine Images -- Advantages vs. Disadvantages 
1. Size —> BIG, usually in `GB`
2. Run time is SLOW —> More layers to start and run than docker
3. Compatability —> can install on ANY OS — no compatability issues 



# Kubernetes
* This is a container orchestration platform that manages containerized applications, operating at a higher level of abstraction than virtual machines, which are designed to run entire operating systems and applications on a virtualized hardware environment; essentially, Kubernetes manages containers while VMs manage entire virtualized servers with their own OS.

![image](https://github.com/user-attachments/assets/e001437a-6982-4271-b82a-df671ceac283)

