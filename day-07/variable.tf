variable "vpc_id" {
  type = string
  //fake
  default = "vpc-084959df874dd8c4a"
}
variable "private_subnets" {
  type = list(any)
  //fake
  default = [
      "subnet-05076a8ea9e3d76c4",
      "subnet-066399e659957deb8"
  ]
}