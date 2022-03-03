# Lesson 8 Functions
#Functions are important because they are a global type of data that can be changed for all uses of it without having to alter each case
#rather just change the function and it will change all use case...Called being "DRY" aka don't repeat code

def a_function():   #Structure of function def function_name():  ...pass just allows it to exist without any error as a placeholder
    pass

print(a_function())
#output: None



def hello():     #A function that prints hello
    print('Hello Function!')

hello() #to execute a function just type the name of the function then empty ()



def goodbye():
    return('Goodbye Function')  #function, goodbye, holds the str value 'Goodbye Function' and you can print that out if you want to
                                #similar to how function, len works. len('word') ...output: is a returned 4 but we can't see it unless we print

print(goodbye().upper())    #changing functions! goodbye() prints out the returned value of goodbye function str


def hello_func(greeting, name='You'):           #function has two arguments, it returns a str with empty braces filled with arguments
    return('{}, {}').format(greeting, name)

print(hello_func('Hi', 'Moh')) #if you left Moh out it would say You as a default message



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='Moh', age=22)
#prints out tuple ('Math', 'Art') and below is a dictionary {'name': 'Moh', 'age':22}
courses = ['Math', 'Art']
info = {'name':'Moh', 'age':22} #if we set these are variables we can input these into the function as arguments with *, and **

student_info(*courses, **info) #does same thing as previous function with student info except more clean
