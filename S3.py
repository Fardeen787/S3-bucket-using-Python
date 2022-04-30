import io
import boto3

AWS_REGION = "us-east-2"

client = boto3.client("s3", region_name=AWS_REGION)
client = boto3.client("s3", region_name=AWS_REGION)


def create_bucket():
    n=input("Enter the bucket name = ")
    bucket_name = n
    location = {'LocationConstraint': AWS_REGION}

    response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    print("Amazon S3 bucket has been created")

def list_all_bucket():
    response = client.list_buckets()
    print("Listing Amazon S3 Buckets:")
    for bucket in response['Buckets']:
     print(f"-- {bucket['Name']}")

def delete_bucket():
    list_all_bucket()
    n=input("Enter your bucket name to delete")
    bucket_name = n
    client.delete_bucket(Bucket=bucket_name)
    print("Amazon S3 Bucket has been deleted")


def cleanup_s3_bucket():
    # Deleting objects
    list_all_bucket()
    n=input("Enter your bucket name to delete")
    S3_BUCKET_NAME = n
    s3_resource = boto3.resource("s3", region_name=AWS_REGION)
    s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)

    for s3_object in s3_bucket.objects.all():
        s3_object.delete()
    # Deleting objects versions if S3 versioning enabled
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()
    print("S3 Bucket cleaned up")
    client.delete_bucket(Bucket=n)
    print("Amazon S3 Bucket has been deleted")

def list_bucket_files():
  list_all_bucket()
  n=input("Enter your bucket name to display its files = ")
  S3_BUCKET_NAME =n
  s3_resource = boto3.resource("s3", region_name=AWS_REGION)
  s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)
  print('Listing Amazon S3 Bucket objects/files:')
  for obj in s3_bucket.objects.all():
    print(f'-- {obj.key}')



def gen_signed_url(bucket_name, object_name):
    s3_client = boto3.client("s3", region_name=AWS_REGION)
    url = s3_client.generate_presigned_url(ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=3600)
    print(url)



def generateurl():
    list_all_bucket()
    n=input("Enter the name of bucket")
    S3_BUCKET_NAME = n
    list_bucket_files()
    a=input("Enter the name of file")
    gen_signed_url('n','a')




def versioning_enable():
    list_all_bucket()
    
    n=input("Enter the bucket names = ")
    s3_resource = boto3.resource("s3", region_name=AWS_REGION)
    versioning = s3_resource.BucketVersioning(n)
    versioning.enable()
    print(f'S3 Bucket versioning: {versioning.status}')








def numbers_to_strings(arg):
    if(arg==1):
        create_bucket()
    elif(arg==2):
        list_all_bucket()
    elif(arg==3):
        delete_bucket()
    elif(arg==4):
        cleanup_s3_bucket()
    elif(arg==5):
        list_bucket_files()
    elif(arg==6):
        generateurl()
    elif(arg==7):
        versioning_enable()
    

   
    


if __name__ == "__main__":

   while(True):
    print("1.Create bucket")
    print("2.List bucket")
    print("3.Delete Empty bucket")
    print("4.Delete  NON Empty bucket")
    print("5.List of bucket files")
    print("6.Generate URL")
    print("7.Versioning enable")



    


   

    argument=int(input("Enter your choice="))
    if(argument==0):
        break;
    else:
      print (numbers_to_strings(argument))
