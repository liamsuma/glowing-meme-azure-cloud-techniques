# Depending on project needs, sometimes we have to upload folders under a local directory into Blob Storage
# In the older verion of Blob Storage, we could use create_blob_from_path() function but it doesn't work in V12 SDK for Python
# The following script illustrates how to upload local folders into Blob Storage based on Azure Github source code 

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
import os 

base_file_path = '/path/to/your/local/directory/'
target_folder = 'xyz' # target_folder is the subfolder under container_name 
 
connect_str = '1q2w3e4r5t6y7u8i9o0p'
container_name = 'abc'

def upload_file(source, dest):
    
    print(f'Uploading {source} to {dest}')
    with open(source, 'rb') as data:
      client.upload_blob(name=dest, data=data)

def upload_dir(source, dest):

    prefix = '' if dest == '' else dest + '/'
    prefix += os.path.basename(source) + '/'
    for root, dirs, files in os.walk(source):
        for name in files:
            dir_part = os.path.relpath(root, source)
            dir_part = '' if dir_part == '.' else dir_part + '/'
            file_path = os.path.join(root, name)
            blob_path = prefix + dir_part + name
            upload_file(file_path, blob_path)
try:
    source = base_file_path + target_folder
    dest = '' # dest is the target folder name  
    service_client = BlobServiceClient.from_connection_string(connect_str)
    client = service_client.get_container_client(container_name)
except Exception as ex:
    print('Exception:')
    print(ex)

if __name__ == '__main__':
    upload_dir(source=source, dest=dest)
