"""1. Get the file path from the user, load and display the data"""
import sys
import os
from functions import(
    read_csv_file,
    display_table, 
    save_csv_file, 
    validate_field_selection,
)

def reader(): 
    if len(sys.argv) < 2:
        print("Please provide the file path for us to work with.")
        sys. exit()

    file_path = sys.argv[1]
    save_file_path = sys.argv[2]

    # validate save_file_path
    if not save_file_path.endswith('.csv'):
        print(f"Target file path not valid: {save_file_path}")
        sys.exit()

    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print(f"The path does not lead to the a file: {file_path}")
        print(f"Available files:")
        for fn in os.listdir():
            if fn.endswith(".py") or os.path.isdir(fn):
                continue
        print(f" - {fn}")  
    else:
        # Read
        table = read_csv_file(file_path)
        # Display 
        display_table(table)

        #Load changes
        changes = sys.argv[3:]
        if not changes:
            print("No changes to be made were provided, try again.")
            sys.exit()
        
        print()

        for chg in changes:
            rdx, cdx, val = chg.split(',')
            rdx = int(rdx)
            cdx = int(cdx)
            #validate the input data
            validate_field_selection(rdx, cdx, table)
            # Do the change
            table[rdx][cdx] = val

        display_table(table)

        # save to the new file 
        save_csv_file(table, save_file_path)

if __name__=="__main__":
    reader()