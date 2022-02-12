# Azure Blob Storage file upload
This script allows to upload any file in an Azure Blob Storage

**Before running this script, please copy your credentials from the Azure Portal as follow :**

1. Sign in to the *Azure portal*.
2. Create a *Storage Account*.
3. Create a *Blob* and a *Container*.
4. In the storage account menu pane, under *Security + networking*, select *Access keys*.
5. In the *Access keys* pane, select *Show key*
6. Copy the **Connection string** value and past it in your code or as environment variable for more security.

**So if you use the incorrect installation order for these packages, you must have to uninstall `azure-storage` first and install `azure-storage-blob` again to avoid the potential error later.**

> You can find more information on <a href="https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python#upload-blobs-to-a-container" target="_blank">Azure's Documentation</a>
