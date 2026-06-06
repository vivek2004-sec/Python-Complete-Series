# Keyword_variable length argument:
def std_info(**info):
    print(type(info))
    print("student: ", info['name'], info['age'], info['branch'])
    

std_info(name="vivek", age='22', branch='cse')


