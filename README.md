# RedHatTest  --  Downloading the files from GoogleDrive using Python



#pydrive 

PyDrive is a wrapper library of google-api-python-client that simplifies many common Google Drive API tasks.

#google-api-python-client 

Google API Client Library for Python



#Installation

Use the package manager pip to install pydrive and Google API Client

pip install pydrive

pip install google-api-python-client



#Setting up googledrive oauth authentication

Go to https://console.cloud.google.com/ and login with the same account of your google drive

create a new project and open that project


#Downloading google drive api and creating credentials

Open the project and click on as shown below

![image](https://user-images.githubusercontent.com/100018055/154794566-f2038b6a-2792-47b5-bb30-c610eb493d95.png)

Enable api and services and select Google drive api

After enabling gdrive api, create the credentials and follow the steps and proceed to setup the OAuth 2.0 Client IDs

Download the json file of oAuth 2.0 client ID and save it in your project directory

![image](https://user-images.githubusercontent.com/100018055/154796079-6c419a58-4dc3-408a-9039-19f01e251614.png)


#OAuth consent screen


open the OAuth onsent screen and click on publish to publish your app and provide authentication.

![image](https://user-images.githubusercontent.com/100018055/154796403-b2d9620c-e957-48d1-aa6f-b84418334891.png)




#updating the settings.yaml file


After creating the outh client ID, edit the "OAuth 2.0 Client IDs" and copy the Client id and client secret 

Open the settings.yaml file and update those IDs and save it.



#Running the main.py program


Open the terminal and go to project directory

Make sure python is installed and pydrive package is installed and run the program using "python main.py"

If it redirects you to the authentication page, make sure to select the correct account and provide authentication.

The files from the google drive will get downloaded to your local disk.






