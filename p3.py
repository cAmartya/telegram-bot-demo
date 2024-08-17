import re
import json

shorthand = json.load(open("./shorthand.json"))

t1 = "collection report for west bengal 01 on 6/03/21"
t1 = t1.upper()
s1 = "west bengal"
y = re.sub(r"\d+\W\d+\W\d+", "", t1)
# y = re.sub()
for k in shorthand.keys():
  if k in y:
    print(k, shorthand[k])

digit = re.findall(r"\d+", y)[0]
# digit = re.find
# digit = re.match(r"\d+", y)
print(digit)
print(y)
print("end")