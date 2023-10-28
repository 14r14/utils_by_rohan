import os

def rename(dir, pattern):
    for file in os.listdir(dir):
        f = os.path.join(dir, file)

        if os.path.isfile(f):
            f_name, f_ext = os.path.splitext(f)
            f_name = f_name.replace(pattern, '')
            res = f_name + f_ext
            os.rename(f, res)

dir = str(input("Enter the directory: "))
pattern = str(input("Enter the pattern to replace: "))
rename(dir, pattern)