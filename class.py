#*class Classname:
	i=12345
	def f(self):
		return 'hello world'




#methods

class Snake:
    name="python"
    def change_name(self,new_name):
        self.name=new_name


#class
class MyClass:
    "this is my second class"
    a=10
    def func(self):
        print('Hello')
        print (MyClass.a)
        print(MyClass.func)
        #print(MyClass._doc_)
x=MyClass()
print(x.a)
print(x.func())

##
###second class
##class Myclass :
##    "this is my second class"
##    a=10
##    def func(self):
##        print('Hello')
##
##        #create a new class
##        ob=MyClass()
##        print(MyClass

