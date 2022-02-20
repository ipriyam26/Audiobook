
# coding=utf-8

from pytube import YouTube,Channel,Playlist
import re
import csv

class UploadYoutube:
    def __init__(self,link) -> None:
        link =  input("Please input link: ") if link == None else link
        self.source_processor(link)  

    def clean(self,text):
        text = text.replace("Greatest🌟AudioBooks","").replace("🎧📖","").replace("|","").replace("-","").replace("AudioBook","").strip()
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        title= regrex_pattern.sub(r'',text)
        return title

    def add_all(self,f,object):
        i,j=0,0
        writer = csv.writer(f)
        for video in object.videos:
            print(f"seen {j}")
            j+=1
            if(video.length < 3000):
                continue
            title = video.title.replace("/","").strip()
            writer.writerow([title, video.watch_url])
            print(f"{title} added to the list {i}")
            i+=1

    def add_video(self,f,video_link):
        video = YouTube(video_link)
        writer = csv.writer(f)
        title = video.title.replace("/","").strip()
        writer.writerow([title,video.watch_url])
        print(f"{title} added to the list")
        

    def source_processor(self,source):
        with open('ytbooklist.csv', 'a') as f:
            selector = source.replace("https://www.youtube.com/","")[0]
            if "p" == selector:
                obj = Playlist(source)
                self.add_all(f,obj)
            elif  "c" == selector:
                obj = Channel(source)
                self.add_all(f,obj) 
            else:
                self.add_video(f,source)       


                  
