import search.search as search
import search.searchyt as searchyt
import youtube
import sys

try:
    args = sys.argv[1]
    if args == '-yt':
        searchyt.SearchYT(flag=args)
    elif args == '-o':
        searchyt.SearchYT(flag=args)
    elif args == '-u':
        youtube.UploadYoutube()
    else:
        print("No such flag")          
        
    
except:
    search.IndexSearch()       
    
        