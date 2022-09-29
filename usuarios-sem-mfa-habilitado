import json
import boto3

def lambda_handler(event, context):
    sns_resource = boto3.resource('sns')
    TOPIC_ARN = 'ARN TOPIC'
    sns_topic = sns_resource.Topic(TOPIC_ARN)
    
    iam = boto3.resource('iam')
    users = iam.users.all()
    

    users_list = []
    for user in users:
        has_any = any(user.mfa_devices.all())
        if not has_any:
            users_list.append(user.name)
            
    sns_topic.publish(Message="Usuários sem MFA habilitado: \n{}".format("\n".join(users_list)))
