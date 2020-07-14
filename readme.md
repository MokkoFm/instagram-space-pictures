# Space Instagram

The program helps you to get pictures of space from API of Hubble and SpaceX and download it to Instagram automatically. 

### How to install

You can put your login and password from Instagram in your own .env-file:
```
LOGIN = your login from instagram
PASSWORD = your password from instagram
```

If you want to do it with safety, you can use .env file. 

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

After that you can start:
```
python main.py
```
After downloading pictures to folders (collections, images) you will see:
```
2020-07-15 00:49:30,268 - INFO - LOGIN FLOW! Just logged-in: False
2020-07-15 00:49:46,154 - INFO - Logged-in successfully as 'python_project_space_pictures'!
FOUND: w:1080 h:811 r:1.3316892725030827
2020-07-15 00:50:07,515 - INFO - Photo 'images\hubble.jpg' is uploaded
```
If you see that it works successfully. 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).