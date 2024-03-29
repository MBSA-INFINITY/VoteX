import os
import pymongo

ENVIRONMENT = os.environ["ENVIRONMENT"]
if ENVIRONMENT == "dev":
    connection_string = "mongodb://localhost:27017"
    DB_NAME = "votex"
else:    
    MONGO_CLUSTER = os.environ["MONGO_URI"]
    MONGO_USERNAME = os.environ["MONGO_USERNAME"]
    MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
    DB_NAME = os.environ["DB_NAME"]
    connection_string = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE&w=majority"


db_client = pymongo.MongoClient(connection_string)
db_client = db_client.get_database(DB_NAME)


users_collection = db_client['users']
voter_kyc_collection = db_client['voter_kyc']
candidate_kyc_collection = db_client['candidate_kyc']
voting_details_collection = db_client['voting_details']