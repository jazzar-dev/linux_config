import subprocess

with open('../Documents/dot_files', 'r') as f:
    text = f.read().split('\n')
    print(text)
    f.close()

for i in text:
    if i != '':
        try:
            subprocess.call(['rm', '-r', f'/home/jazzar/{i}'])
        except:
            next
