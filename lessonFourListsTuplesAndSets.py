#Lesson 4 lists tuples and sets

#list format
name = ['', '',...]
ex. courses = ['History', 'Math', 'CompSci']

print(len(courses)) #prints the length of list
:3

print(list[x]) prints out the list variable of a said position
ex.
print(courses[2])
:Math
if you put [-1] outputs always last item in list


print(courses[0:2])
:['History', 'Math']
Compsci no included because number after : is not inclusive


#to add to a list but not inside the list
listName.append('additional variable')
ex. course.append('Art')
:['History', 'Math', 'CompSci', ['Art']]

#to insert to a list
listName.insert(location#, 'variable')
ex. courses.insert(0, courses_2)
:['Course1', 'Course 2'] , ['History', 'Math', 'CompSci']

#Adding variables from another list to another
list1.extend(list2)
:[list1 + list 2]

#To remove from a list
list1.remove('variable')
ex.courses.remove('Math')

#To remove last value from a list
list1.pop()
You can view popped value if you assigned it a variable
ex. popped = courses.pop()

#To reverse list
list1.reverse()

#To sort in alphabetical order
list1.sort()

#To sort in numerical ascending order(increasing)
numericallist1.sort()
ex. nums = [1,5,2,4,3]
nums.sort()
print(nums)
:[1,2,3,4,5]

#To sort but in reverse order
list1.sort(reverse=True)

#If you dont want to alter your original list but want to sort it
#then you make a new variable and use
sorted_list1 = sorted(list1)
This sorts the list alphabetical/ascending numerical then you print variable sorted_list1


#Min, max, sum ... shows minium value, max value or sum value
print(min(listofnums))
print(max(listofnums))
print(sum(listofnums))


#To index meaning find where located
print(list1.index('variable'))
ex. print(courses.index('CompSci'))
:3 (aka position 3 in the list counting from 0)

#To see if variable is in list use
print('variable' in list1)
:true or false


#To go through each value in a list with a loop
#use for in loop

for x in list1:    doesn't have to b called x can be anything you want
    print(x)
:all values of list on new lines

#with enumeration index
for index, x in enumerate(list1):
    print(index, x)
:all values of index, list values on new lines

... you can add a different start value after list1
i.e. enumerate(list1, start=1)  instead of 0 it'll start at 1.


#To turn list into string(str)
list_str = ', '.join(list1)
this outputs a str separated by a , and space

Vice versa str to list
new_list = course_str.split(', ')


#Tuples

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
:printed out same values for both

 list_1[0] = 'Art' #replaced history with art

print(list_1)
print(list_2)
:History becomes art and rest of both lists are same

# Immutable must be ( ) instead of [] ...useful if you just need access to data but not wanna change it
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2) #prints out same tuple aka list unmutable

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)
:error because immutable means its not mutatable meaning no append, insert, etc.

# Sets use { } brackets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)
:The list but in differing orders each time due to not caring for order
It also gets rid of duplicate values
It also is optimized for searching if a variable is in the list

#comparing sets for intersections
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
:{'History', 'Math'}

#differences
print(cs_courses.difference(art_courses))
:{'Physics', 'CompSci'}

#union combines the sets
.union()

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
