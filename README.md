# Photo Uploader w/ AWS, Kubernetes, Python, Terraform, and CI/CD
# A Cloud-Native Showcase

Demo app: FastAPI image uploader. Images stored in S3. Deployed to AWS EKS using Terraform and GitHub Actions.


## What this demonstrates
- **Python (FastAPI)** — lightweight API for image uploads.  
- **Docker** — containerization of the application.  
- **Kubernetes (EKS)** — orchestrated deployment on AWS.  
- **Terraform** — infrastructure as code (EKS cluster, S3 bucket, ECR repo).  
- **AWS** — managed cloud services (EKS, S3, ECR, IAM, CloudWatch).  
- **CI/CD (GitHub Actions)** — automated build, push, and deploy pipeline. 


## Quickstart (high-level)
1. Clone repo
2. Edit terraform/variables.tf as needed
3. `cd terraform && terraform init && terraform apply` (review plan and approve)
4. Note outputs: ECR repo URL, S3 bucket name, EKS cluster name
5. Create GitHub Secrets: AWS credentials or role, S3_BUCKET (value from Terraform), ECR_REPO_NAME, EKS_CLUSTER_NAME, AWS_REGION
6. Push to `main` on GitHub -> Actions will build and deploy
7. Use `kubectl get svc -n showcase` to find LoadBalancer IP/hostname

## Architecture
```mermaid
flowchart TD
    A[User Uploads Image] --> B[FastAPI App on EKS]
    B -->|Store File| C[S3 Bucket]
    B -->|Logs| D[CloudWatch]
    ECR[(ECR Repo)] --> B
    Terraform[Terraform IaC] --> EKS[(EKS Cluster)]
    Terraform --> S3[(S3 Bucket)]
    Terraform --> ECR