# import json

# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Thinh',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

import sys
import os
from source.modules.library.IO_support import *

a = 'Thinh'
data = {'people':[{'name': a, 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
jstr = json.dumps(data, sort_keys=True, indent=4)

with open('data.json', 'w') as outfile:
     json.dump(data, outfile)
