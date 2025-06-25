## Day-01

```
## change .pem type 
Rename-Item "Two-Tier_Key-Pair" "Two_Tier_Key_Pair.pem"

## Fix state
- change rds sg ingress 0.0.0.0/0
- nc -zv endpoint.us-east-1.rds.amazonaws.com 3306
- mysql -h endpoint.us-east-1.rds.amazonaws.com -u admin -p
- check password in aws secret manager

```
