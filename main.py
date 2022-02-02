#!/usr/bin/env python3

"""
This script allows to upload a file to an Azure Blob Storage
"""
import os
import uuid
from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":   # linux
    from azure.storage.blob import BlobService, BlobServiceClient
elif _platform == "darwin": # OS X
    from azure.storage.blob import BlobServiceClient
elif _platform == "win32":  # Windows...
    from azure.storage.blob import BlobService, BlobServiceClient

# Create a local directory to hold blob data
local_path = "./data"

# Get the Storage Connection String
blob_service_client = BlobServiceClient.from_connection_string(os.environ['AZURE_STORAGE_CONNECTION_STRING'])

# Container name must match with an existing one
container_name = "myfirstcontainer"

# Create a file in the local data directory to upload and download
local_file_name = str(uuid.uuid4()) + ".txt"
upload_file_path = os.path.join(local_path, local_file_name)

# Write text to the file
file = open(upload_file_path, 'w')
file.write("Hello, World!")
file.close()

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
