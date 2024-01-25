import csv


def read_csv_file(file_path):
    table = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            table.append(row)
    return table

def display_table(table, sep="-"):
    print_tpl = "{:^10.10s} | {:^15.10s} | {:^15.10s} | {:^15.10s} |"
    print(65* sep)
    print(print_tpl.format(table[0][0], table[0][1], table[0][2], table [0][3]))
    print(65* sep)
    for row in table[1:]:
        print(print_tpl.format(row[0], row[1], row[2], row[3]))
    print(65 * sep)  

def validate_field_selection(rdx,cdx,table):
    if len(table)-1 < rdx:
        print(f"Not enough rows. Asked for: {rdx}, available: {len(table)-1}")
        sys.exit()
    if len(table[rdx])-1 < cdx:
        print(f"Not enough rows. Asked for: {cdx}, available: {len(table[rdx])-1}")
        sys.exit()

def save_csv_file(table,save_file_path): 
    with open(save_file_path, "w", newline="") as f: 
        writer = csv.writer(f)
        writer.writerows(table)