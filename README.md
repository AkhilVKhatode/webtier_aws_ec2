# Web Tier for Elastic Cloud Application

## Overview

The objective is to develop an elastic application that can automatically scale out and in on-demand and cost-effectively using IaaS resources from Amazon Web Services (AWS). The application includes a web tier that handles HTTP POST requests for face recognition and returns classification results.

## Project Structure

- Develop the web tier using AWS EC2.

## Setup Instructions

### Prerequisites

- AWS account
- Python 3.x
- Flask
- Gunicorn
- AWS CLI

### AWS Setup

1. **Create an AWS Account:**
   - Go to the [AWS Signup Page](https://aws.amazon.com/)
   - Choose Account Type as “Personal” and complete the registration.

2. **Generate AWS Access Key:**
   - Go to the AWS console, click on your account name, and select "Security Credentials."
   - Generate a new key under "Access keys" and note the Access Key ID and Secret Access Key.

3. **Create IAM Users:**
   - Create two IAM users: one for development with full permissions and one for grading with `AmazonEC2ReadOnlyAccess` permissions.

4. **Install and Configure AWS CLI:**
   - Install AWS CLI following the [documentation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
   - Configure CLI using the command:
     ```bash
     aws configure
     ```
     Provide the Access Key, Secret Key, default region (us-east-1), and output format (json).

### Local Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AkhilVKhatode/webtier_aws_ec2.git
   cd webtier_aws_ec2
   ```
2. **Install Dependencies:**
   ```pip install -r requirements.txt```
3. **Run the Application:**
   ```gunicorn -w 4 -b 0.0.0.0:5000 webtier:app```

### EC2 Setup

1. **Create an EC2 Instance:**
   Use AMI “ami-00ddb0e5626798373” for basic Ubuntu 18.04.
   Assign a static Elastic IP address to the instance.
2. **Deploy the Application:**
   SSH into the EC2 instance.
   Install necessary software (Python, Flask, Gunicorn).
3. **Run the Application:**
   Clone the repository and run the application using Gunicorn.

### Usage
  - The web tier accepts HTTP POST requests with image files for face recognition.
  - The endpoint for the requests is the root endpoint (/).
  - Example request format: ```curl -X POST -F "inputFile=@path/to/image.jpg" http://<EC2-instance-IP>:5000/```
  - The response will be in plain text format: <filename>:<prediction_results>.

### File Descriptions
  - webtier.py: Main application file containing the Flask app and Gunicorn server configuration.
  - requirements.txt: List of Python dependencies required to run the application.
