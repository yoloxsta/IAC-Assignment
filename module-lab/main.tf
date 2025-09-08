module "my_ec2" {
  source         = "./modules/ec2_instance"
  ami            = var.ami
  instance_type  = var.instance_type
  name           = var.instance_name
}