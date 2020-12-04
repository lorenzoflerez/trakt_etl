#Trakt_ETL

-----------------


| **`Documentation`** |
|-----------------|
| [![Documentation](https://img.shields.io/badge/api-reference-blue.svg)](https://trakt.docs.apiary.io/#reference) |


## Ejecucion



#### 
```shell
$ ./pandemia.sh
```

## Descripcion
Trackt es un servicio gratuito que te permite llevar un control de tus series y películas y llevar un registro de lo que has visto.
En este proyecto se realiza la extracción, transformacion y carga de algunos datos pcomo practica educativa

## Herramientas usadas en este repo:

![iam](/images/iam.png)
#### IAM
- **[iam-create-s3-users.sh](iam-create-s3-users.sh)** Create the S3 IAM user, generate IAM keys, add to IAM group, generate user policy

![ec2](/images/ec2.png)
#### EC2
- **[ec2-ami-encrypted-ebs-boot-volume.sh](ec2-ami-encrypted-ebs-boot-volume.sh)** Create an AMI with an encrypted EBS boot volume from the latest Amazon Linux AMI
- **[ec2-associate-elastic-ip.sh](ec2-associate-elastic-ip.sh)** Reassign a previously allocated Elastic IP to the instance which runs this script
- **[ec2-classic-import-network-acl.sh](ec2-classic-import-network-acl.sh)** Import CIDR IP list to AWS EC2 Classic ACL rules and deny access
- **[ec2-ebs-create-snapshots.sh](ec2-ebs-create-snapshots.sh)** Create a snapshot of each EC2 EBS volume that is tagged with the backup flag
- **[ec2-ebs-delete-snapshots.sh](ec2-ebs-delete-snapshots.sh)** Deletes snapshots for each EC2 EBS volume that is tagged with the backup flag and matches the specified date
- **[ec2-elb-export-template.sh](ec2-elb-export-template.sh)** Export an ELB to a JSON template file for version control, duplication or recreation
- **[ec2-elb-upload-ssl-cert.sh](ec2-elb-upload-ssl-cert.sh)** Upload an SSL Certificate to AWS for use in setting up an ELB


![s3](/images/s3.png)
#### S3
- **[s3-buckets-local-backup.sh](s3-buckets-local-backup.sh)** Backup all contents of all S3 buckets in AWS account locally
- **[s3-buckets-security-audit.sh](s3-buckets-security-audit.sh)** Export S3 bucket ACL, CORS, Policy and Website as JSON for auditing security of all buckets
- **[s3-buckets-total-file-size.sh](s3-buckets-file-size-s3api.sh)** Count total size of all data stored in all S3 buckets using [s3api](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
- **[s3-fix-content-type-metadata.sh](s3-fix-content-type-metadata.sh)** Safely fix invalid content-type metadata on AWS S3 bucket website assets for some common filetypes
- **[s3-open-bucket-policy.sh](s3-open-bucket-policy.sh)** Set an S3 bucket policy to allow GetObject requests from any IP address (publicly accessible website)
- **[s3-remove-glacier-objects.sh](s3-remove-glacier-objects.sh)** Delete all Glacier storage type objects in a single S3 bucket
- **[s3-restrict-bucket-policy.sh](s3-restrict-bucket-policy.sh)** Set an S3 bucket policy to only allow GetObject requests from an IP whitelist file named iplist
- **[s3-set-cache-control-max-age.sh](s3-set-cache-control-max-age.sh)** Set Cache-Control max-age value on AWS S3 bucket website assets for all filetypes
- **[s3-setup-buckets.sh](s3-setup-buckets.sh)** Create S3 buckets, set CORS config and tag bucket with client name

![cloudwatch](/images/cw.png)
#### CloudWatch
- **[cloudwatch-create-alarms.sh](cloudwatch-create-alarms.sh)** Create CloudWatch alarms for EC2, RDS, Load Balancer environments
- **[cloudwatch-create-alarms-statuscheckfailed.sh](cloudwatch-create-alarms-statuscheckfailed.sh)** Create CloudWatch StatusCheckFailed Alarms with Recovery Action for all running EC2 Instances in all regions available
- **[cloudwatch-create-alarms-unhealthyhost.sh](cloudwatch-create-alarms-unhealthyhost.sh)** Create CloudWatch UnhealthyHost Alarms for all ALB and ELB Elastic Load Balancers in all regions available
- **[cloudwatch-logs-cleanup.sh](cloudwatch-logs-cleanup.sh)** Delete all CloudWatch Log Groups with a Last Event that is older than the Retention Policy
- **[cloudwatch-logs-delete-groups.sh](cloudwatch-logs-delete-groups.sh)** Quickly delete all CloudWatch Log Groups with a specified prefix in all regions available
- **[cloudwatch-logs-search.sh](cloudwatch-logs-search.sh)** Search CloudWatch Logs for any string across all regions and log groups
- **[cloudwatch-logs-retention-policy.sh](cloudwatch-logs-retention-policy.sh)** Set CloudWatch Logs Retention Policy for all log groups in all regions available


## Modelo
![Base de Datos](/images/trakt_model.png)
