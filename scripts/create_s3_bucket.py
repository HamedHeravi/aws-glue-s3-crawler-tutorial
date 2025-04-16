import boto3

s3 = boto3.client('s3')
bucket_name = 'ml-AWS-Glue-customers-bucket'

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'}  # adjust to your region
)
print(f"Bucket created: {bucket_name}")


filename = 'customers.csv'
s3.upload_file(Filename=filename, Bucket=bucket_name, Key='datasets/customers.csv')
print("Uploaded customers.csv to S3.")