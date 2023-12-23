import json
import random


BATCH = 2
LIMIT = 5
ALPHA = 2

data = []
export = []


if __name__ == "__main__":
    print("[01] starting ...")
    
    with open("files/map.txt", "r") as file:
        for line in file:
            tmp = line.rstrip()
            parts = tmp.split("=>")
            
            print(f"[02] loading {parts[0]} batch.")
            
            data.append({
                "key": parts[0],
                "list": [x.strip("\"") for x in parts[1].split(";")]
            })
    
    print("[03] data loaded.")
    
    for _ in range(0, BATCH):
        index = random.randint(0, len(data) - 2)
        
        item = data[index]['key']
        array = random.sample(data[index]['list'], k=random.randint(1,LIMIT))
        
        if random.randint(0, 10) < ALPHA:
            array += random.sample(data[len(data)-1], k=ALPHA)
        
        export.append({
            "attack": item,
            "vulenrabilities": array
        })

    print(json.dumps(export))
