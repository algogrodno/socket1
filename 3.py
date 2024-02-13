import json
import pprint
with open("victorina.json", 'r') as f:
    jf = json.load(f)
    pprint.pprint(jf)