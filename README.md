### INR_Classifier
**Microsoft-Future-Ready-Talent-Virtual-Internship-Project**


### Project Title
Automated Indian Rupee (INR) Denomination Classifier using Azure Custom Vision Service..

Industry: Finance
Training Images link:https://drive.google.com/drive/folders/1e-DNtL04nl3Il1uW-gca1nDloD4ClCQH?usp=sharing

## Core Azure Services
Azure App Service: Used for hosting the web application and API endpoints.
Visual Studio Code: Integrated development environment (IDE) for coding, testing, and deploying the project.

## Azure AI Service
Azure AI Custom Vision Service: Leveraged for training and deploying the custom image classification model for INR denomination detection.

### **Problem Statement**
The manual process of identifying and classifying Indian Rupee (INR) denominations in large volumes can be time-consuming and error-prone. This project aims to automate the classification of INR currency notes using machine learning, providing an efficient and accurate solution for financial institutions and businesses.

## **Key Features**
Automated INR Denomination Classification
User-Friendly Web Interface
Real-time Prediction
Two Image Upload Methods:
Capture Image using OpenCV (cv2)
Upload Image (JPEG, PNG, etc.)
Azure App Service Hosting
Integration with Visual Studio Code for development and deployment

## **Project Workflow**
**Set Up Environment**
1.Clone the GitHub repository:
git clone https://github.com/Aasthajain02/INR_Classifier.git

2.Navigate to the project directory:
cd INR_Classifier

3.Install dependencies:
pip install -r requirements.txt

4. Set up environment variables in config.py for Azure Custom Vision Service credentials.

**Training and Deployment**
Use Azure Custom Vision Service to create and train a custom image classification model for INR denominations.
Retrieve the prediction endpoint, prediction key, project ID, and model name from Azure Custom Vision Service.
Update config.py with the obtained credentials.


### Screenshots

1. Azure AI Custom Vision Service Training Dataset
Description: 50 images of each currency 10,20,50,100,200,500,2000 are uploaded

![Screenshot (109)](https://github.com/Aasthajain02/INR_Classifier/assets/103254304/97a17442-0ca1-4cef-a89f-531761764e3c)
![Screenshot (110)](https://github.com/Aasthajain02/INR_Classifier/assets/103254304/3c762110-17d0-4a8e-9034-967484475f22)

3. Accuracy of Quick training 
   ![Screenshot (111)](https://github.com/Aasthajain02/INR_Classifier/assets/103254304/92f82385-4b81-41dd-83ad-40a9cf04abe6)


4. Prediction image
   
   ![Screenshot (113)](https://github.com/Aasthajain02/INR_Classifier/assets/103254304/35bd2b81-1451-4369-b392-d88d5cfc7265)

## Conclusion

The INR_Classifier project demonstrates an end-to-end workflow for building a web-based INR denomination classifier using Azure services. By leveraging Azure Custom Vision Service, the project provides an efficient and scalable solution for automating the classification of INR currency notes.










