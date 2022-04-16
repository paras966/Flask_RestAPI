import requests
Base = "http://localhost:5000/"
datas = [
    {'name':'paras','likes':200,'views':4000},
    {'name':'praveen','likes':2000,'views':3400},
    {'name':'vinayak','likes':1789,'views':5000}
]

for i in range(len(datas)):
    response = requests.put(Base+"video/"+str(i),datas[i])
    print(response.json())

input()

response = requests.delete(Base+"video/1")
print(response)

input()

response = requests.get(Base+"video/2")
print(response.json())
