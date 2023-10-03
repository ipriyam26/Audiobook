

import os
from re import I
from thefuzz import process, fuzz
import search.utils as utils
from pytube import YouTube,Search
import time

from youtube import UploadYoutube

class SearchYT:
    
    def __init__(self, search, flag) -> None:
        self.search = search
        if flag == '-yt' or flag is None:
            self.youtube()
        else:
            self.yt_search()    
    
    def download(self, link):
        yt = YouTube(link)
        try:
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path='.')
            base, ext = os.path.splitext(out_file)
            new_file = f'{base}.mp3'
            os.rename(out_file, new_file)
            print(f"{yt.title} has been successfully downloaded.")
        except Exception:
            print("Unsuccessful")    
        
        # result of success
      
    
    def get_link(self):
        titles_and_paths = utils.get_dictonary('ytbooklist.csv')
        titles = list(titles_and_paths.values())
        matches = list(process.extract(self.search, titles, limit=10, scorer=fuzz.token_set_ratio))

        i = 1
        if matches.__len__() == 0 or matches[0][1] < 75:
            print("No match found")
            return "No match found"
        if matches[0][1] == 100:
            for match in matches:
                if match[1] < 90:
                    break
                print(f"[{i}] {match[0]}")
                i += 1
        else:
            for match in matches:
                if match[1] < 75:
                    break
                print(f"[{i}] {match[0]}")
                i += 1
        n = int(input("Please Pick one to download Enter 0 for other index")) - 1
        while n < 0 or n > i:
            n = int(input("Please Pick one to download: ")) - 1
        if n == 0:
            self.yt_search()
        else:
            return utils.get_key(matches[n][0], titles_and_paths)       


    def youtube(self):
        print("Trying to locate in youtube....")
        link = self.get_link()
        if(link == "No match found"):
            self.yt_search()
        else:
            self.download(link)

    
    

 
    def yt_search(self):
        print("Looking online...")
        yt = Search(f'{self.search}*full audiobook*')
        len(yt.results)
        results = [result for result in yt.results if result.length > 3600]
        title_length = {video.title: video.length for video in results}
        link = [video.watch_url for video in results]
        i = 1
        for title in title_length:
            length = time.strftime("%Hh %Mm", time.gmtime(int(title_length[title])))
            print(f"[{i}] {title} - {length}")
            i += 1
        n = int(input(f"Enter Selection: [1-{i}] Enter 0 to quit: "))
        while n > i or n < 0:
            n = int(input(f"Please enter a number between [1-{i}] Enter Selection again: "))

        if n == 0:
            return
        n -= 1
        self.download(link[n])
        UploadYoutube(link=link[n])     
