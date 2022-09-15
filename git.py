import subprocess
from urllib import response
import requests
import time
def gitfund(url):
    print(url)
    response = requests. get(url)
    print("response\n",url)
    file = open("image.png", "wb")
    file. write(response. content)
    file. close()
    subprocess.run("git add .")
    subprocess.run("git commit -m  'commited'")
    subprocess.run("git push")
    time.sleep(5)
    return "executed"
#gitfund("https://firebasestorage.googleapis.com/v0/b/facedetection-91462.appspot.com/o/Photos%2FJPEG_20220915_084418.jpg?alt=media&token=674030f2-6d04-438a-9069-51980e0d8c06")
