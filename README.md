# VoteX
A Digital Voting System

# Steps to setup the project
- Clone the repository
- Run `pip install -r requirements.txt`
# Firebase Setup for Backend
1. Create a firebase project and get all the configurations of the project from `Project Settings`.

2. Navigate to the **Authentication** section in your firebase project and enable the `Email and Password`
 authentication.

3. The Configuration is as follow :-
```python
config = {
  "apiKey": YOUR_API_KEY ,
  "authDomain": YOUR_AUTH_DOMAIN,
  "databaseURL": YOUR_DATABASEURL,
  "projectId": YOUR_PROJECT_ID,
  "storageBucket": YOUR_STORAGE_BUCKET,
  "messagingSenderId": YOUR_MESSAGING_SENDER_ID,
  "appId": YOUR_APP_ID,
  "measurementId": YOUR_MEASUREMENT_ID 
  }

```
4. Now in you `.env` file include the following parameters as it is :-
```bash
export FIREBASE_APIKEY=YOUR_API_KEY
export FIREBASE_AUTHDOMAIN=YOUR_AUTH_DOMAIN
export FIREBASE_DATABASEURL=YOUR_DATABASEURL
export FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
export FIREBASE_STORAGE_BUCKET=YOUR_STORAGE_BUCKET
export FIREBASE_MESSAGING_SENDER_ID=YOUR_MESSAGING_SENDER_ID
export FIREBASE_APP_ID=YOUR_APP_ID
```
# MonoDB Setup for Backend
1. Create a mongodb cluster in MonDB Atlas and the add the required configurations in the .env.

2. Now in you `.env` file include the following parameters as it is :-
```bash
export ENVIRONMENT=prod
export MONGO_URI=YOUR_MONGO_URI
export MONGO_USERNAME=YOUR_MONGO_USERNAME
export MONGO_PASSWORD=YOUR_MONGO_PASSWORD
export DB_NAME=YOUR_DB_NAME
```
3. If you wan tot use dev mode you can put the following in the .env :- 
```bash
export ENVIRONMENT=dev
```



