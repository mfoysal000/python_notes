#Lesson 6 conditionals and booleans
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

language = 'Python'; #a variable that is equal to a string

if language == 'Python': #An If-then conditional which tested the true/false value of the '==' (Comparison)
    print('The language is Python')
elif language == 'Java':    #A second conditional if first is not met (You can add multiple elifs ...similar to switch case statements in other langs.)
    print('The language is java')
elif language == 'JavaScript':
    print('The language is javascript')
else:                               #make sure else: is on most left side or else it will be part of if statement
    print('Nothing')    #prints this out if let's say language = 'C++'

#The Booleans
# and : both conditions met
# or :either conditions met
# not :opposite reaction

User = 'Admin'
Logged_in = True

if User == 'Admin' and Logged_in: #needs both conditions to be met
    print('Admin page accessed')
else:
    print('Bad credentials')

if not Logged_in: #if not 'true' then it must be false but in this case its true so it prints out the else part
    print('Admin page accessed')
else:
    print('Bad credentials')

#Object identity: is
a = [1,2,3] #same objects but different memories allocated
b = [1,2,3]

print(a==b) #outputs true
print(a is b) #false due to different memory allocation
print(id(a))
print(id(b))

b = a
print (a is b) #now true because they have same id now, same memory, same object...basically means (id(a) == id(b))

# Common False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False       #0 is always false

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

#practice from past lesson
student = {'race': 'black', };
race = student.pop('race')
print(race)
