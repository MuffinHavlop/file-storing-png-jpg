import os
 
dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
       
        if file.endswith('.jpg') or file.endswith('.png'):
            destination = f'D:\\Downloadpics\\{str(file)}'
            source = f'D:\\{str(file)}'
            os.replace(source, destination)
            print("The file was moved")
