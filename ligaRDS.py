import json
import boto3

def lambda_handler(event, context):
    region = 'region'
    rdsInstance = ['RDS-DB-Name']   
    rds = boto3.client('rds', region_name=region) 
    
    for i in rdsInstance:
        rds.start_db_instance(DBInstanceIdentifier=i)
