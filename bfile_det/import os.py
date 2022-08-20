import os

fp = './additional_bexe'

for file in os.listdir(fp):
    ext = file.split('.')[-1]
    print(ext)