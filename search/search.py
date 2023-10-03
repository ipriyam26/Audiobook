from thefuzz import process, fuzz
import search.utils as utils
import threading
import requests
import os
import re
from bs4 import BeautifulSoup
import search.searchyt as YT

class IndexSearch:
    
    def __init__(self) -> None:
        self.search = input("Enter book name: ")
        self.full_length_audiobook()

    def get_link(self):
        titles = []
        titles_and_paths = utils.get_dictonary('data.csv')
        titles = list(titles_and_paths.values())
        titles.pop(0)
        matches = list(process.extract(self.search, titles, limit=10, scorer=fuzz.token_set_ratio))

        if matches.__len__() == 0:
            print("No match found")
            return "No match found"
        for i, match in enumerate(matches, start=1):
            print(f"[{i}] {match[0]}")
        n = int(input("Please Pick one to download \nor 0 to search other index: ")) - 1

        while n > 11 or n < -1:
            n = int(input("Please Pick one to download: ")) - 1
        return "No match found" if n < 0 else utils.get_key(matches[n][0], titles_and_paths)


    def download(self,filename,downLink,path):
        p = os.path.join(path,filename)
        print(f"Downloading.... {filename}")
        doc = requests.get(downLink)
        with open(p, 'wb') as f:
            f.write(doc.content)
        print("Downloaded.... ",filename)

    def full_length_audiobook(self):
        link = self.get_link()
        if(link=="No match found"):
           YT.SearchYT(search=self.search,flag='-yt')
        else:   
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'html.parser')
            bookName = link.split('/')[3]
            parent_path = os.getcwd()
            path = os.path.join(parent_path,bookName)
            os.makedirs(path)
            for a in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
                filename = a['href'][a['href'].rfind("/")+1:]
                downLink = a['href'] 
                threading.Thread(target=self.download,args=(filename,downLink,path)).start()
                

            # print("Downloaded all the files")
        # os.system(f"gupload {bookName}")
