# AWS-segmentation-report

This repository contains code and report for "Capstone Project - Arvato Customer Segmentation" done as part of Udacity Machine Learning Engineer Nanodegree program.

In this project, the demographic data of German population and the customer data have been analysed in order to perform Customer Segmentation and Customer Acquisition. Arvato Financial Solutions is a services company that provides financial services, Information Technology (IT) services and Supply Chain Management (SCM) solutions for business customers on a global scale.

This project is to help a Mail-Order company to acquire new customers to sell its organic products. The goal of this project is to understand the customer demographics as compared to general population in order to decide whether to approach a person for future products.

This project is divided into two steps:

Customer Segmentation using Unsupervised Learning, in this part a thorough data analysis and feature engineering steps are performed to prepare the data for further steps. A Principal Component Analysis (PCA) is performed for dimensionality reduction. Then K-Means Clustering is performed on the PCA components to cluster the general population and the customer population into different segments. These clusters are studied to determine what features make a customer with the help of cluster weights and component weights.

Customer Acquisition using Supervised Learning, in this part of the project the customers data with defined targets indicating the past responses of the customers has been used to train Supervised Learning algorithms. Then the trained model is used to make predictions on unseen test data to determine whether a person could be a possible customer.

## Files 
- **proposal.pdf** My project proposal. Introducing the problem and my proposed solutions at the time. Some aspects changed as I was progressing throughout the project.
- **report.pdf** My project report. Splited into 5 major parts: Definition, Analysis, Methodology and Results.
- **Notebooks 1,2 and 3** Containing respectively the code for Data preprocessing, Dimanesionality reduction / clustering and Model creation.
- **source_pytorch** Contain the model/train/predict.py files required for the creation and deployment of a pytorch model with SageMaker.

## Instructions
This project has been entirely built within a "ml.m4.xlarge" SageMaker notebook instance. The "conda_pytorch_p36" kernel was select to run each notebook. 
If you plan on executing this code, you should ideally do it in the exact same environment as to avoid dependencies issues. Otherwise, just solve them as you go.
