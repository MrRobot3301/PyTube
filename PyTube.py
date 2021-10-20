from pytube import YouTube
import time
from termcolor import colored



class video: # Class For Video
    def __init__(self,url):
        self.url = url 

    def downloadVdo(self): 
        url = input(colored("[+] Enter or Paste the Url to download video form YouTube : ",'green'))
        try:
            yt_obj = YouTube(url) #Getting Url
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
 
    # download the highest quality video
            filters.get_highest_resolution().download()
            print(colored('  **  ** Your Video Downloaded Successfully ** ** ','green'))
        except Exception as e:
            print(colored(" !!!!  Error, Please Try Again !!!! ",'red'))




class audio: # Class For Audio
    def __init__(self,url):
        self.url = url
    
    def downloadAudio(self):
        url = input(colored("[+] Enter or Paste the Url to download Only Audio Form YouTube Video : ",'green'))
        try:
            yt_obj = YouTube(url)
            yt_obj.streams.get_audio_only().download(output_path='', filename='Your_Audio.mp3') #Downloading Audio 
            print(colored(' ** ** ** YouTube Audio Downloaded Successfully ** ** ** ','green'))
        except Exception as e:
            print(colored(" !!!!  Error, Please Try Again !!!! ", 'red'))




v= video('') # Object For Video Class
a= audio('') # Object For Audio Class


while True:
    print(colored("****     -->>    ****    -->>    ****    -->>    ****    -->>    ****    -->>    ****    -->>    ****    -->>    ****",'blue'))
    time.sleep(0.7)
    print(colored("                    -->>    -->>    -->>    -->>    -->>    -->>   -->>    -->>   -->>",'blue'))
    
    time.sleep(0.7)

    time.sleep(0.7)
    print(colored("                   -->>   Welcome to YouTube Video/Audio Downloader by 'MrRobot3301'  <<--\n",'red'))

    break
time.sleep(0.5)
print("\n\n")


n=int(input(colored("[+] Enter Your Choice :\n\n[1] -> For Download YouTube Video  [2] -> For Download Only Audio of the Youtube Video : ",'green')))
if n==1:
    v.downloadVdo()
elif n == 2 :
    a.downloadAudio()
else:
    print(colored("    ->  ->  ->  Please Choose Between the Options  <- <- <-  \n",'red'))    