import subprocess

with open('../Documents/dot_files', 'r') as f:
    text = f.read().split('\n')
    print(text)
    f.close()

for i in text:
    if i != '':
        try:
            subprocess.call(['cp', '-r', f'/home/jazzar/{i}', '.'])
            subprocess.call(['cp', '-r', f'/home/jazzar/{i}', '/home/jazzar/dot_files_backup/{i}.bak'])
        except:
            next
