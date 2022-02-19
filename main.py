#pip install pydrive
#import Googleauth and Googledrive modules from pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# Download single file using file_id from GoogleDrive
#
# file = drive.CreateFile({'id' : '<enter the file_id here>'})
#
# mention the file format like jpeg for images, .pdf for pdf files etc
#
# file.GetContentFile('filename.pdf')

#You can get the id of a file or folder by right clicking on it and copying the link

id = input('enter the folder_id here: ')

#list out the files in the folder

FileList = drive.ListFile({'q': f"'{id}' in parents"}).GetList()

#Downloading the files from a folder
for file in FileList:
    print(file['title'])
    file.GetContentFile(file['title'])





