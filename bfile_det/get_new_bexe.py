import os

fp = './additional_bexe'

g_files = []

for file in os.listdir(fp):
    ext = file[-3:]
    if ext == 'exe':
        g_files.append(file)

print(g_files)
print(len(g_files))
print(len(os.listdir(fp)))

with open('g_files.txt', 'w') as f:
    f.write('\n'.join(g_files))