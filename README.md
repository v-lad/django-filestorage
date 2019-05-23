# django-filestorage
Simple Django application for storage files. Writted with help Filepond JS file upload library.
Files encode to Base64 string format after form submitting and decode back on server.
Authenticated users can browse their files on main page under upload form. Every file has its own detail page where the file information, such as file size, upload date, delete date, days to deleting, is located. Everyone who has link this page can delete file from server or download it.
___
### App is deployed on heroku:
https://filestorage-evotask.herokuapp.com/