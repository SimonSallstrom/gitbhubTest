# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pandas as pd
import numpy as np


endpoint = "https://taxonomy.api.jobtechdev.se/v1/taxonomy/graphql?query="

graphql_query = """query MyQuery {
  concepts(type: "occupation-name", version: "1") {
    id
    preferred_label
    deprecated_legacy_id
    broader(type: "ssyk-level-4") {
      id
      ssyk_code_2012
    }
  }
}
"""

response = requests.get(endpoint + graphql_query).json()["data"]["concepts"]

L= [0]

for i in np.arange(1,len(response),1):
    L.append(0) 


for i in range(0,len(response)):
    L[i] = response[i]["preferred_label"]
    
d = {'occupation-name': L,"ssyk-code-2012": np.zeros(len(response),),"Ams-taxonomy": np.zeros(len(response))}

for j in range(0,len(response)):
    d['ssyk-code-2012'][j] = int(response[j]["broader"][0]["ssyk_code_2012"])
    d['Ams-taxonomy'][j] = int(response[j]["deprecated_legacy_id"])
    

df = pd.DataFrame(data = d)

print(df)

df.to_csv(r'c:\Users\simon.sallstrom\converted.csv', index = False,columns = ['ssyk-code-2012', 'Ams-taxonomy'])
