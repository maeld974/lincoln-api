from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from loguru import logger
import json
import os
import time

with open(os.path.join("static", "key.json")) as json_file:
    key = json.load(json_file)

def refresh_csv(id_mission):
    file_name = f"mission_{id_mission}_person_score.csv"
    service = BlobServiceClient(account_url="https://lincolnlonglist.blob.core.windows.net/", credential=key['value'])
    client = service.get_blob_client("longlist", f"DB_prep_result/v0/v0_live_demo/{file_name}", snapshot=None)
    try:
        with open(os.path.join("static", "mission_candidates", f"{file_name}"), "wb") as blob:
            t1=time.time()
            download_stream = client.download_blob()
            blob.write(download_stream.readall())
            t2=time.time()            
            response = {'success' : True, 'message': f"CSV Refreshed {file_name} in {t2 - t1} seconds"}
    except ResourceNotFoundError:
            os.remove(os.path.join("static", "mission_candidates", f"{file_name}"))
            response = {'success' : False, 'message': f"No file found for {file_name}"}
    return response