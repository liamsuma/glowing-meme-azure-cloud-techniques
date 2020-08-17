# This script is a similar approach when using older version of Python SDK 

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
import os 

base_file_path = '/path/to/local/directory/'
# target_folder is the subfolder under container_name 
target_folder = 'abc' 

# de-compose connect_str
account_name = 'xyz'
account_key = '1q2w3e4r5t6y7u8i9o0p'

def run_upload():
    try:
        # Please do not change connect_str unless stated otherwise 
        connect_str = '<connection string>'
        container_name = 'qaz'

        local_path_to_remove = '/path/to/local/directory/'
        local_folder = '/path/to/local/folder/to/upload/'

        client = BlobServiceClient.from_connection_string(connect_str)
        container_client = client.get_container_client(container_name)

        for root, dirs, files in os.walk(local_folder):
            if files:
                for name in files:
                    file_path_on_azure = os.path.join(root, name).replace(local_path_to_remove, '')
                    file_path_on_local = os.path.join(root, name)

                    blob_client = container_client.get_blob_client(file_path_on_azure)

                    with open(file_path_on_local, 'rb') as data:
                        blob_client.upload_blob(data=data)
    except Exception as ex:
        print('Exception:')
        print(ex)

if __name__ == '__main__':
    run_upload()
    print('============ Upload Completed ====================')
