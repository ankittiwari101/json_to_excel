import json
import pandas as pd

file_path = "file.json"    #Path of the JSON data file.

def searchJson(data,path):
    if path=="" or path is None:
        print("Invalid path")
        return
    arr = path.split(".")
    obj = data
    for token in arr:
        if token.lower() == "object" or token.lower() == "array":
            continue
        if token.isnumeric():
            obj = obj[int(token)]
            continue
        else:
            obj = obj[token]
    return obj

def is_all_scalar(data):
    if type(data) is list:
        return False
    elif type(data) is dict:
        for value in data.values():
            if value is dict or value is list:
                return False
    return True

f = open("file.json")
try:
    data = json.load(f)
    print("Json File successfully imported.")
    #print(data[0]['name'])
    str = input("Enter node path : ")
    str.strip()
    print(searchJson(data,str))
    try:
        val = searchJson(data,str)
        
        if val == None:
            print("Invalid String.Please try again.")
            exit()
        
        if is_all_scalar(val):
            print("Debug: All Scalar Values found!")
            val = [val]
        #val = json.loads(val)
    
        pd.DataFrame(val).to_excel("logs/"+str+".xlsx")
        print("Excel file generated successfully. Check logs folder")
        
    except Exception as e:
        print("Incorrect node path. ")
        print(e)
        
    #print(str)
except json.JSONDecodeError:
    print("Not a JSON file.")

#pd.read_json("file.json").to_excel("logs/output.xlsx")

