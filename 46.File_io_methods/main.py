f = open("46.File_io_methods/myfile.txt", 'r')
while True: 
    line  = f.readline()
    if not line:
        break
    print(line)