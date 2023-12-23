data = {}


if __name__ == "__main__":
    print("[01] starting ...")
    
    with open("files/map.txt", "r") as file:
        for line in file:
            tmp = line.rstrip()
            parts = tmp.split("=>")
            
            print(f"[02] loading {parts[0]} batch.")
            
            data[parts[0]] = [x.strip("\"") for x in parts[1].split(";")]
    
    print("[03] data loaded.")

    print(data)
