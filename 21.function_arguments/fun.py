# Keyword_variable length argument:
def std_info(**info):
    print(type(info))
    print("student: ", info['name'], info['age'], info['branch'])
    

std_info(name="vivek", age='22', branch='cse')

def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   