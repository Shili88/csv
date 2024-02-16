import sys 
import os
import pickle
import json
import csv

data = []

class BaseFileHandler:
    def __init__(self, file_path=None, file_save=None):
        self.file_path = file_path
        self.file_save = file_save

#Pickle file handle 
class PickleFileHandler(BaseFileHandler):
    def read(self):
        with open(self.file_path, "rb") as f:
            data = pickle.load(f)
            return data
    def save(self, data):
        with open(self.file_save, "wb") as f:
            pickle.dump(data, f)

#json file handle 
class JsonFileHandler(BaseFileHandler):
    def read(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
            return data
    def save(self, data):
        with open(self.file_save, "w", newline="") as f:
            json.dump(data, f)
            return data

#csv file handle 
class CsvFileHandler(BaseFileHandler):
    def read(self):
        with open(self.file_path, "r") as f:
            reader = csv.reader(f)
            for r in reader:
                data.append(r)
            return data
    def save(self, data):
        with open(self.file_save, "w", newline="") as f: 
            writer = csv.writer(f)
            writer.writerows(data)


file_path = sys.argv[1]
file_save = sys.argv[2]
changes = sys.argv[3:]

if len(sys.argv) < 3:
    print("Please provide the file path for us to work with.")
    sys. exit()
    
   
# file_save_handler
if file_path.endswith('.json'):
    file_read_handler = JsonFileHandler
elif file_path.endswith('.pickle'):
    file_read_handler = PickleFileHandler
elif file_path.endswith('.csv'):
    file_read_handler = CsvFileHandler
else:
    raise Exception(f"File type not supprted: {file_path}. Supported file as per following: pickle , csv and json.")
        

# file save  
if file_save.endswith('.json'):
    file_save_handler = JsonFileHandler
elif file_save.endswith('.pickle'):
    file_save_handler = PickleFileHandler
elif file_save.endswith('.csv'):
    file_save_handler = CsvFileHandler
else:
    raise Exception(f"File type not supprted: {file_path}. Supported file as per following: pickle , csv and json.")


#File not exist 
if not os.path.exists(file_path) or not os.path.isfile(file_path):
    print(f"The path does not lead to the a file: {file_path}")
    print(f"Available files:")
    for fn in os.listdir():
        if fn.endswith(".py") or os.path.isdir(fn):
            continue
        print(f" - {fn}")

def validate_field_selection(rdx,cdx,table):
    if len(table)-1 < rdx:
        print(f"Not enough rows. Asked for: {rdx}, available: {len(table)-1}")
        sys.exit()
    if len(table[rdx])-1 < cdx:
        print(f"Not enough rows. Asked for: {cdx}, available: {len(table[rdx])-1}")
        sys.exit()

reader = file_read_handler(file_path=file_path)
writer = file_save_handler(file_save=file_save)
data = reader.read()
print(data)

if not changes:
    print("No changes to be made were provided, try again.")
    sys.exit()
        
print()

for chg in changes:
    rdx, cdx, val = chg.split(',')
    rdx = int(rdx)
    cdx = int(cdx)
    #validate the input data
    validate_field_selection(rdx, cdx, data)
    # Do the change
    data[rdx][cdx] = val

writer.save(data)



