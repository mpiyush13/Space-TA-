import os
import shutil


# f=os.listdir("../train")
# print(f)
# for i in f:
#     os.mkdir(i)

f=os.listdir("../train")
c=0
for i in f:
    print(len(os.listdir(f"../train/{i}")))
   
#val copy
# f=os.listdir("../train")
# # print(f)
# c=0
# y=0
# for i in f:
#     c=0
#     t=os.listdir(f"../train/{i}")
#     t=int(len(t)/4.0)
#     #print(i)
#     print(f"{y} is starting transfering ....")
#     for j in os.listdir(f"../train/{i}"):
#       shutil.move(f'../train/{i}/{j}', f'{i}/{j}')
#     #   print(j)
#       if c==t:
#           break;
#       c=c+1
#     print(f"{y} is complited")
#     y=y+1
# print(c)   