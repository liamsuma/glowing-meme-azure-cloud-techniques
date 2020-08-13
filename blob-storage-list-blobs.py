from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
import os 

def ls_files(client, path, recursive=False):

    if not path == '' and not path.endswith('/'):
      path += '/'

    blob_iter = client.list_blobs(name_starts_with=path)
    files = []
    for blob in blob_iter:
      relative_path = os.path.relpath(blob.name, path)
      if recursive or not '/' in relative_path:
        files.append(relative_path)
    return files

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
client = blob_service_client.get_container_client(container_name)

files = ls_files(client, '', recursive=True)

print(files)
