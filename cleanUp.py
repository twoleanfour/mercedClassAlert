import json

def write(jData):
	with open("jsonLayout.json", "w") as r:
		r.write(json.dumps(jData, sort_keys=True, indent=4, separators=(',', ':')))

def cleanUp():
    deleteQueue = []
    with open("jsonLayout.json", "r") as r:
	    jsonData = json.load(r)
    for entry in jsonData["classes"]:
        if not entry["usesCRN"]:
            if len(entry["code"]) != 3:
                deleteQueue.append(entry)
                continue
                #checking for valid code should go here
        else:
            if len(entry["crn"])!=5:
                deleteQueue.append(entry)
                continue
        if "@" not in entry["email"]:
            deleteQueue.append(entry)
            continue
        if "." not in entry["email"]:
            deleteQueue.append(entry)
            continue
        if entry["sent"]:
            deleteQueue.append(entry)
            continue
    for obj in deleteQueue:
        jsonData["classes"].remove(obj)
        del deleteQueue[:]
    write(jsonData)