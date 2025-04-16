import boto3

glue = boto3.client('glue')

crawler_name = 'customers-crawler'

response = glue.create_crawler(
    Name=crawler_name,
    Role='AWSGlueServiceRoleDefault',  # Replace with your IAM role
    DatabaseName='ml_customers_db',
    Targets={'S3Targets': [{'Path': f's3://{'ml-AWS-Glue-customers-bucket'}/datasets/'}]},
    TablePrefix='customers_',
)
print(f"Created crawler: {crawler_name}")


glue.start_crawler(Name=crawler_name)
print("Crawler started.")

