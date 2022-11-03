import csv
import json
import hashlib
 
def csv_to_json(csv_file_path, new_csv_file_path):
    
    data_dict = {}
 
    
    #open the csv file 
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
 
        #convert each row into a dictionary
        #and add the converted data to the data_variable
 
        for rows in csv_reader:
 
            
            key = rows['Serial Number']
            data_dict[key] = rows
    #convert the dictionary to json file and create a sha256 of json file
    the_result = json.dumps(data_dict, indent = 4)
    the_hash = hashlib.sha256(the_result.encode("utf-8")).hexdigest()
    print(the_hash)
    # open the input csv file in read mode
    # and open output csv file in write mode
    with open(csv_file_path, 'r') as old_file_handler, open(new_csv_file_path, 'w', newline='') as new_file_handler:
        
        old_file = csv.reader(old_file_handler)
        new_file = csv.writer(new_file_handler)
        count = 0
        #add the hash value to each row of the csv file
        for row in old_file:
            if count == 0:
                row.append('hash Value')
                new_file.writerow(row)
            else:
                row.append(the_hash)
                new_file.writerow(row)
            count = count+1
    
 
csv_file = 'NFT Naming csv - All Teams.csv'
modified_csv_file = 'NFT Naming csv - All Teams.output.csv'
 
if __name__ == '__main__':
    
 
    csv_to_json(csv_file, modified_csv_file)