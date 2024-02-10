from flask import Flask
import json

app = Flask("autoComplete")

@app.route('/<path:query>', methods=['GET'])
def autoComplete(query):
    d=structureData()
    r=find(str(query),d)
    result={
        "q":query,
        "d":r
    }
    return json.dumps(result)

def readData():
    filepath='medical-questions'
    with open(filepath,encoding="utf8") as file:
        data=file.readlines()
    return data

def find(query,data):
    match=[t for t in data if t[0].startswith(query)]
    sortedMatch = sorted(match, key=lambda x: x[1], reverse=True)
    if len(sortedMatch) > 4:
        return [t[0] for t in sortedMatch[:4]]
    else:
        return [t[0] for t in sortedMatch[:4]]


def structureData():
    data=readData()
    sData=[]
    for sentence in data:
        words=sentence.split()
        query=' '.join(words[:-1])
        number=int(words[-1])
        sData.append((query,number))
    return sData

if __name__ == '__main__':
    #d=structureData()
    app.run(debug=True)
