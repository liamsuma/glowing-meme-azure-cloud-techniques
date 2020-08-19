# List files under a designated virtual directory using name_starts_with 

import os
import glob
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
client = blob_service_client.get_container_client(container_name)

output_path = 'CSVComplete/' # output path or any path exists under container name 
blob_list = client.list_blobs(name_starts_with=output_path)
for blob in blob_list:
    print('Listing ... ' + blob.name + '\n')
