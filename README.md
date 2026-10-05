# AWS CI/CD Portfolio Dashboard

A real-world AWS CI/CD project that automatically tests, builds, and deploys a portfolio website whenever code is changed in GitHub.

## Live Website

http://yaman-cicd-portfolio-20261005.s3-website.ap-south-1.amazonaws.com

## GitHub Repository

https://github.com/Quazi-Yaman/AWS-CICD-Portfolio

---

## Project Overview

This project demonstrates a complete CI/CD workflow using GitHub and AWS services.

The portfolio website contains information about practical AWS cloud projects and is deployed to Amazon S3.

Whenever a change is pushed to the `main` branch:

1. AWS CodePipeline detects the GitHub change.
2. CodeBuild downloads the source code.
3. Automated Python tests run using pytest.
4. The frontend is prepared for deployment.
5. CodePipeline deploys the build output to Amazon S3.
6. The updated website becomes available through the S3 static website endpoint.

This demonstrates an automated development-to-deployment workflow.

---

## Architecture

```text
Developer
    |
    | Edit / Commit
    v
GitHub Repository
    |
    | Source Change
    v
AWS CodePipeline
    |
    v
AWS CodeBuild
    |
    +--> pytest automated tests
    |
    +--> Build frontend
    |
    v
Amazon S3
    |
    v
Live Portfolio Website
