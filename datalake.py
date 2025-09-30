from minio import Minio
from minio.error import S3Error
import os 

#connexio minio
MINIO_ENDPOINT = '127.0.0.1:9000'
MINIO_ACCESSKEY = 'monuser'
MINIO_SECRETKEY = 'monmotdepasse'
MINIO_BUCKET = 'datalake'
LOCAL_FOLDER = '/Users/qasmichaymaeqasmi/Documents/projets/Project-Python-S3/data'

# créate a minio client 

client = Minio(
    MINIO_ENDPOINT, 
    access_key=MINIO_ACCESSKEY,
    secret_key= MINIO_SECRETKEY, 
    secure=False

)

#check if bucket exist :
if not client.bucket_exists(MINIO_BUCKET):
    client.make_bucket(MINIO_BUCKET)
    print(f"Bucket '{MINIO_BUCKET}' created!")

for filename in os.listdir(LOCAL_FOLDER) : 
    if filename.endswith('.csv'):
        file_path = os.path.join(LOCAL_FOLDER, filename)
    try : 
        client.fput_object(MINIO_BUCKET, filename, file_path)
    except S3Error as e:
                    print(f"Error uploading {filename}: {e}")
 


