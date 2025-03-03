# DL-End_to_End

## Workflow

1. Update config.yaml in config dir
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# To run the repo

## steps
Clone the repository
```bash
https://github.com/appsbotta/DL-End_to_End
```

## step - 01 Create a conda env after opening the repo
```bash
conda create -n ckn python=3.13 -y
```
```bash
conda activate ckn
```

## step - 02 Install Requirements.txt
```bash
pip install -r requirements.txt
```

## step - 03 Run app.py
```bash
python app.py
```

## DVC cmd
* dvc init
* dvc repro
* dvc dag

# AWS CI-CD Deployment using Github Actions

## 1. Login to AWS Console

## 2. Create IAM user for deployment
```bash
# give these access to IAM user
1. EC2 access -> this is virtual machine
2. ECR: Elastic COntainer registery to save your docker image in aws

# About deployment
1. build docker image of the source code

2. Push your docker image to ECR

3. Launch your EC2 instance

4. Pull your image from ECR to EC2

5. Launch your docker image in EC2

# policy
1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

```