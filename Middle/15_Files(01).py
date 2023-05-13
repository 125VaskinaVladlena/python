import os

def print_docs(directory):
    for item in os.listdir(directory):
        f = os.path.join(directory, item)
        if os.path.isfile(f):
            print(item)
        elif os.path.isdir(f):
            print_docs(f)
            print('*  inside  *', item)
print_docs(r"C:\\Users\\User\\Desktop\\доки мама")