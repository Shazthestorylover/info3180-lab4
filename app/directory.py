import os

def get_uploaded_images():
    rootdir = os.getcwd()
    filenames = []
    print(rootdir)
    path = r'\static\uploads'
    for subdir,dirs,files in os.walk(rootdir + path):
        for file in files:    
            print(subdir,file)
            print(os.path.join(subdir,file))
            filenames.append(file)

    return filenames[1:]