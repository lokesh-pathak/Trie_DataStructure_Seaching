from flask import Flask, render_template
import json
from data_structure import Trie

trie = Trie()
def CreateDataStructure(file_name):
    # open the data.csv file in read mode
    file = open(file_name,'r')
    count = 0
    # read each line in file
    for line in file:
        try:
            if not count:
                count+=1
                continue
            # romove , & ,, with single space
            line = line.replace(',,',' ').replace(',',' ').strip()
            if not line:
                pass
            else:
                # add line in data structure
                trie.add(line)
            count+=1
        except Exception as err:
            print(err)
    file.close()

print("Creating Trie Data Structure....")
CreateDataStructure('data.csv')
print("Data Structured Created Successfully.")

application=Flask(__name__)

@application.route('/search/<string:name>')
def autocomplete(name):
    print(name)
    try:
        resultList = trie.start_with_prefix(name)
        if resultList != None and not isinstance(resultList, bool):
            return json.dumps(resultList),200
        else:
            return [],200
    except Exception as e:
        return e,404

@application.route('/')
def home():
    return render_template('index.html'),200

if __name__ == '__main__':
    print("Please Wait Loading Server...")
    # run the app
    application.run(debug=True,host='0.0.0.0',port=8888) 
