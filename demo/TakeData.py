import json

with open("vvvv.json",'r') as load_f:
    text = json.load(load_f)
    # print(text["all_students"])
    nt = text["all_students"]
    # print(nt[0])
    for i in nt:
        print(i)


