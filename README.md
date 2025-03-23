## A45 Assignment2
# Overview

This is a Django-based multi-app project designed as part of an assignment. The project is fully Dockerized and integrated with Jenkins for automated CI/CD deployment.

* **Framework:** Django
* **Containerization:** Docker
* **Automation:** Jenkins
* **Deployment:** Docker Hub

# Project Structure
* StudentProject/ – Main Django project folder
* app1/ – Contains the homepage
* app2/ – Contains aboutpage
* app3/-Contains servicepage and contactpage
* templates/ – Global templates for UI
* static/ – Contains CSS for styling
* Dockerfile – Defines how the project runs inside a container
* Jenkinsfile – Automates the CI/CD pipeline
# How to Run the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/G-gunjan/A45-Assignment2.git
cd A45-assignment2
```
## 2. Run Using Docker
If you want to run the project inside a Docker container, use:  
```bash
docker build -t gunjanpandya/gunjan-assignment2:0.0.1.RELEASE .
docker run -d -p 8000:8000 gunjanpandya/gunjan-assignment2:0.0.1.RELEASE
```
Now, open http://127.0.0.1:8000/ in your browser.
## 3. Pull from Docker Hub
Instead of building manually, you can pull the prebuilt image:
```bash
docker pull gunjanpandya/gunjan-assignment2:0.0.1.RELEASE
docker run -d -p 8000:8000 gunjanpandya/gunjan-assignment2:0.0.1.RELEASE
```
your project will be live on http://127.0.0.1:8000/
## 4. Jenkins CI/CD Pipeline
The Jenkins pipeline automates:

* Pulling code from GitHub
*  Building a Docker image
*  Pushing it to Docker Hub
To trigger the pipeline, push any changes to GitHub, and Jenkins will do the rest!
### 6. Conclusion
This project demonstrates a full CI/CD pipeline with Django, Docker, and Jenkins. It ensures that every code change is automatically built, tested, and deployed using best DevOps practices.
