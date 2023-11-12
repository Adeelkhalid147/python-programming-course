from typing import Dict, Union,Optional
import pprint

key = Union[int,str] # create custom type
value = Union[int,str,list,dict,tuple,set]
# List
data : Dict[key,value] = {
                        "fname":"Muhammad Adeel",
                        "name":"Khalid",
                        "education":"MBA"
                        }

pprint.pprint(data)