# The script is used to download PDFs from Blob Storage 

import os 
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.storage.blob import generate_blob_sas, AccountSasPermissions, ResourceTypes
from urllib.request import urlopen
from datetime import datetime, timedelta

# Please do not change connect_str unless stated otherwise 
connect_str = '<connection sting>'
# de-compose blob connect_str
account_name = 'xyz'
account_key = 'abc'

base_file_path = '/path/to/save/pdfs'

try: 
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # persumably this is the container only for PDF files 
    container_name = 'ocr'
    container_client = blob_service_client.get_container_client(container_name)
    blobs_list_generator = container_client.list_blobs() # get access to blobs listed under container 
    
    for blob in blobs_list_generator:
        blob_name = blob.name # assign value to blob names 
        download_file_path = os.path.join(base_file_path, blob_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        print("\nDownloading blob to \n\t" + download_file_path)
        with open(download_file_path, 'wb') as download_file:
            download_file.write(blob_client.download_blob().readall())
            # or we can use readinto() method 
            # blob_client.download_blob().readinto(download_file)
        
except Exception as ex:
    print('Exception:')
    print(ex)
