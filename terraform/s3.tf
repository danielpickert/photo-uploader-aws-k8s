resource "aws_s3_bucket" "uploads" {
bucket = "${var.project}-uploads-${random_id.suffix.hex}"
acl = "private"
force_destroy = true


tags = {
Name = "${var.project}-uploads"
Project = var.project
}
}


resource "random_id" "suffix" {
byte_length = 4
}