import json
import boto3

def lambda_handler(event, context):
    region = 'region'
    rdsInstance = ['DB-Instance_Name']   
    rds = boto3.client('rds', region_name=region) 
    
    for i in rdsInstance:
        rds.stop_db_instance(DBInstanceIdentifier=i)
