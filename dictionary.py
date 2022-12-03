#ordered
#changeable

# ris = {
#     "age" : "18",
#     "name" :"Rishu",
#     "age" : 19,
# }
# ris.popitem()
# print(ris)

# print(ris)
# print(ris.get("age"))
# print(ris.get('age'))
# ris["reg no."] = 12219457
# # print(ris)
# ris.update({"age":33})
# print(ris)

# Dict = {'Dict1': {1: 'Geeks'},
#          'Dict2': {'Name': 'For'}}
  
# Accessing element using key
# print(Dict['Dict1'])
# print(Dict['Dict1'][1])
# print(Dict['Dict2']['Name'])
# Dict.popitem()
# print(Dict)

# dict1 = {"one":1, "two":2 , "three": 3}
# dict2 = {"four" : 4, "five" :5, "six":6}
# #Merge two dictionaries in one:
# #Method 1
# dict3 = dict1 | dict2
# print(dict3)
# #Method2
# dict1.update(dict2)
# print(dict1)

dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
print(dict1['class']['student']['marks']['web'])