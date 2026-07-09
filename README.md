# 🚀 Serverless Customer Management System

A cloud-native serverless web application that enables users to add and search customer records using REST APIs. Built using AWS Lambda, Amazon API Gateway, Amazon DynamoDB, IAM, HTML, CSS, and JavaScript, the application demonstrates scalable serverless architecture, secure cloud integration, and NoSQL database operations.

---

## 📌 Project Overview

This project implements a fully serverless customer management system using AWS managed services. Users can add new customer records and retrieve existing customer details through a responsive web interface. The backend is powered by AWS Lambda and exposed through Amazon API Gateway REST APIs, while Amazon DynamoDB stores customer information.

> **Note:** This project was successfully developed, tested, and deployed on AWS Free Tier. To avoid unnecessary AWS resource usage and charges, the cloud resources were removed after successful testing. The complete source code, architecture, and screenshots are available in this repository.

---

## ✨ Features

- Add new customer records
- Search customers by Customer ID
- REST API integration using Amazon API Gateway
- Serverless backend using AWS Lambda
- Data storage using Amazon DynamoDB
- Secure access with AWS IAM
- CORS support for browser-based requests
- CloudWatch logging for monitoring and debugging
- Responsive user interface built with HTML, CSS, and JavaScript

---

## 🛠 Technologies Used

- AWS Lambda
- Amazon API Gateway (REST API)
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- HTML5
- CSS3
- JavaScript
- Python (Boto3)

---

## 📁 Project Structure

```text
Serverless-Customer-Management-System/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── lambda_function.py
│
├── architecture/
│   └── architecture.png
│
├── screenshots/
│   └── application-ui.png
│
├── README.md
└── .gitignore
```