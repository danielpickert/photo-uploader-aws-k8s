# This uses the official AWS EKS module. You can change configuration as needed.
module "eks" {
source = "terraform-aws-modules/eks/aws"
version = "~> 20.0"


cluster_name = "${var.project}-eks"
cluster_version = "1.27"
subnets = [] # If empty, module creates default subnets in the default VPC. For production, pass explicit VPC/subnets.


node_groups = {
on_demand = {
desired_capacity = 2
max_capacity = 3
min_capacity = 1


instance_types = ["t3.medium"]
}
}
}


output "cluster_endpoint" {
value = module.eks.cluster_endpoint
}


output "cluster_certificate_authority_data" {
value = module.eks.cluster_certificate_authority_data
}


output "kubeconfig" {
value = module.eks.kubeconfig
}