import json

f1 = open("D:/bird_Data/bird_data_indonesia.json")
f2 = open("D:/bird_Data/bird_data_indonesia.csv", 'w')
l = f1.readline()
response = json.loads(l)
headers = [i for i in response['recordings'][0].keys() if not(i in ["also", "sono"])]
ans = []
for bird in response['recordings']:
    temp = []
    for i in headers:
        if i in bird:
            temp += [str(bird[i]).replace(",", ";")]
        else: temp += [""]
    ans += [",".join(temp)]
ans = [",".join(headers)] + ans
f2.write("\n".join(ans))