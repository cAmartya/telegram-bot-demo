# f = open("./input.txt", "r")
# text = f.read()
# f.close()

# terminal = "#"
# # print(text.split(terminal))
# items=[]
# for t in text.split(terminal):
#   if len(t)>0:
#     items.append(t.strip())

# print(items)
# items.sort()
# print(items)

# import re
# # t1 = "West Bengal 01:"
# # t1 = "bihar 01:"
# t1 = "bihar:"
# first_line_items = re.findall(r"\w*\d*", t1)
# print(first_line_items)

# first_line_items = [items for items in first_line_items if len(items)>0]
# state_name = ""
# state_idx = ""
# if(first_line_items[-1].isdigit()):
#   state_name = ' '.join(first_line_items[:-1])
#   state_idx = first_line_items[-1]
# else:
#   state_name = ' '.join(first_line_items)

# print(state_name, state_idx)

# from datetime import date

# today = date.today()
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

import re
# s1 = "[27/03, 23:09] Some(more): bihar \n ========== \n nbfc = gg\n======\n"
# s2 = "bihar"
# pattern = r'\[[^\]]*\]\s[^\:]*:\s*'

# s1 = re.sub(r'==+', "#", s1)
# print(re.sub(pattern=pattern, string=s1, repl=""))
# print(re.sub(pattern=pattern, string=s2, repl=""))

line = "bd collection 999/77"
line = "bd collection= 999/77"
t = re.split("=|-|:|;|>|collection", maxsplit=1, string=line)

print(t)

print(re.findall("\w+", t[1]))