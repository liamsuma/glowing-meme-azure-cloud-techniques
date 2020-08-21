# Download PDF files as streams and pass them as input directory for other programs  

import os 
from io import BytesIO # stream processing 
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.blob import generate_blob_sas, AccountSasPermissions, ResourceTypes
from urllib.request import urlopen
from datetime import datetime, timedelta

# Please do not change connect_str unless stated otherwise 
connect_str = '<connection string>'
# de-compose blob connect_str
account_name = 'xyz'
account_key = '1q2w3e4r5t6y7u8i9o0p'

base_file_path = '/path/to/local/dir'

try: 
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # persumably this is the container only for PDF files 
    container_name = 'ocr'
    # same container but different input folder and output folder
    container_client = blob_service_client.get_container_client(container_name)
    blobs_list_generator = container_client.list_blobs() # get access to blobs listed under container 
    
    for blob in blobs_list_generator:
        blob_name = blob.name # assign value to blob names 
        download_file_path = os.path.join(base_file_path, blob_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        print("\nDownloading blob to \n\t" + download_file_path)
        stream_buffer = BytesIO()
        with stream_buffer as download_stream:
            blob_client.download_blob(max_concurrency=3).readinto(download_stream)
            # or we could use built-in properties from Azure 
            # both ways should work 
            # blob_client.download_blob(max_concurrency=3).download_to_stream(download_stream)
        
except Exception as ex:
    print('Exception:')
    print(ex)
