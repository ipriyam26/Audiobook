import csv

def get_dictonary(file):
    titles_and_paths = {}
    with open(file,'r') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if(row[0] == " "):
                continue
            titles_and_paths[row[1]] = row[0].strip()
    return titles_and_paths

def get_key(val,dict):
    for key, value in dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"