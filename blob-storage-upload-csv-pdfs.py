# Script to upload csv files into Blob Storage 
# Current script is using BlobServiceClient with changes made by Azure since May 2019 and going forward 

import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings

try: 
    # Please do not change connect_str unless stated otherwise 
    connect_str = '<connection string>'
    container_name = 'ocr' # already created in Azure 
    upload_file_path = '/path/to/your/input/files' # input file path 
    output_blob_name = 'output_blob.csv' # what we view in container 

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=output_blob_name)
    
    print("\nUploading to Azure Storage as blob:\n\t" + output_blob_name)

    with open(upload_file_path, 'rb') as data:
        blob_client.upload_blob(data=data)
        # Or we could change content_type here to ignore Octet Stream 
        # blob_client.upload_blob(data=data, content_settings=ContentSettings(content_type='application/csv')

    
except Exception as ex:
    print('Exception:')
    print(ex)
