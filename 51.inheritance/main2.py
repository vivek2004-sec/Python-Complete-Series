class school:
    def name_of_the_school(self):
        print("shraddha Modern School, kagal.")
        
class classroom:
    def std(self ):
        print(10)
        
class student(school, classroom):
    pass

boy = student()
boy.name_of_the_school()
boy.std()