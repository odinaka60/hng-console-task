import csv
import json
import hashlib
 
def csv_to_json(csv_file_path, new_csv_file_path):
    
    hash_list = []
 
    
    #open the csv file 
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
 
        #convert each row into a dictionary and get hash of each row
        
        count = 0
        for rows in csv_reader:
            if count == 0:
                hash_list.append('Hash Value')
            else:
                the_result = json.dumps(rows, indent = 4)
                the_hash = hashlib.sha256(the_result.encode("utf-8")).hexdigest()
                hash_list.append(the_hash)
            count = count+1
    # open the input csv file in read mode
    # and open output csv file in write mode
    with open(csv_file_path, 'r') as old_file_handler, open(new_csv_file_path, 'w', newline='') as new_file_handler:
        
        old_file = csv.reader(old_file_handler)
        new_file = csv.writer(new_file_handler)
        index = 0
        #add the hash value to each row of the csv file
        for row in old_file:
            if index<len(hash_list):
                row.append(hash_list[index])
                new_file.writerow(row)
                index = index+1
        print("succesful")
    
 
csv_file = 'HNGi9 CSV FILE - Sheet1.csv'
modified_csv_file = 'HNGi9 CSV FILE - Sheet1.output.csv'
 
if __name__ == '__main__':
    
 
    csv_to_json(csv_file, modified_csv_file)