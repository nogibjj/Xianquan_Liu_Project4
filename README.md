# Project#4: Continuous Delivery of FastAPI Data Engineering API on AWS

[![Python application test with Github Actions](https://github.com/nogibjj/XL_Project4/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/XL_Project4/actions/workflows/main.yml)

[![AWS CodeBuild Continuos Delivery](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiUllWS3FhMFp4T28yWWVMSDh2Yk5PWWxvMVB2WWJlMTVYNnhzOWZkTDBCcy8wRGgxZ0N0T0g3ZmRVdTZWZ3JkeERwVDZhNDUrUHg0OWE1WHlkZjVsTDYwPSIsIml2UGFyYW1ldGVyU3BlYyI6IndHRUwwMWU4VXVmQmJia0wiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

Welcome! This is my fourth project for the Data Engineering System class at Duke.

For this project, I created a microservice using FastAPI that can generate a random 8-digit password, pushed tested source code to Github, performed continuous integration with Github actions, and configured the build server to deploy changes on build (Continuous Delivery).

## Ways to Setup Continuous Delivery:
* Create ECR repository in AWS

* Navigate to ECR repo created and follow "push" instructions

* Navigate to AWS App Runner and Setup Continuous Delivery using ECR

* Setup AWS Code Build to push container after each build (which triggers auto-deploy)

![Screenshot_20221123_225147](https://user-images.githubusercontent.com/112578003/203692198-41debea0-40dc-4336-a0c8-7d1fb245112e.jpg)
