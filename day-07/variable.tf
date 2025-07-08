variable "vpc_id" {
  type = string
  //fake
  default = "vpc-084959df874dd8c4a"
}
variable "private_subnets" {
  type = list(any)
  //fake
  default = [
      "subnet-0c4236993bfd9c343",
      "subnet-066399e659957deb8"
  ]
}