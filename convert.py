import os
import re

os.makedirs('termite', exist_ok = True)

def getData(text):
    ret = {}
    for i in text.split("\n"):
        if i.strip():
            try:
                ret[i.split()[1]] = i.split()[2]
            except:
                print(i.split())
    return ret

def mkColor(data):
    b = data['Background_Color'][1:]
    return "rgba({},{},{},0.8)".format(*[int(i, 16) for i in re.findall('..', b)])

temp = open("temp").read()

for i in os.listdir('xrdb'):
    f = open(os.path.join('xrdb',i )).read()
    data = getData(f)
    data['color'] = mkColor(data)
    if "Bold_Color" not in data:
        data['Bold_Color'] = ""
    with open(os.path.join('termite', os.path.splitext(i)[0]), "w") as fp:
        fp.write(temp.format(**data))
