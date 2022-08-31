import search.search as search
import search.searchyt as searchyt
import youtube
import sys

try:
    args = sys.argv[1]
    if args in ['-yt', '-o']:
        searchyt.SearchYT(flag=args)
    elif args == '-u':
        youtube.UploadYoutube()
    else:
        print("No such flag")          


except Exception:
    search.IndexSearch()       

    
        