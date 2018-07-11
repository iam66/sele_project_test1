
class Student():
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if 0<gender<=100:
            self.__gender=gender
        else:
            print('wrong gender')
        

