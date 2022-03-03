#Lesson 5 dictionaries
student = {'name':'Moh', 'age':24, 'courses':['Math', 'CompSci']}; #Key:value, key:value ...notice it's a set with strings, integers, and lists
#the keys can be any immutable datatypes but are generally strings,integers

print(student); #prints out key and values... you can type student['key'] to show a specific value you wanna check i.e. student['name'] to output Moh


#print(student['phone']) vs print(student.get('phone')) ; it's better to do 2nd method b/c 1st produces an error while second produces 'None' as feedback
print(student.get('phone')) #You can pass a 2nd argument after 'phone' to change negative message i.e. ('phone', 'Not found')

student['phone'] = {'555-5555'}; #updates dictionary(student) to include phone number

print(student.get('phone'));

student.update({'name': 'Moh Foy', 'age':25, 'gender':'male'}); #efficient way to add multiple key:values and update old ones

print(student);

del student['gender']; #deletes a key and value
print(student);

age = student.pop('age'); #another way to delete but also retain the value if we want to
print(student);
print(age); #returns 25


print(len(student));  #prints 3 due to 3 keys and values
print(student.keys()) #prints keys
print(student.values()) #prints values
print (student.items()) #prints both

for key,value in student.items(): #To loop through a whole dictionary use for-in loop with items for both key and value
    print(key,value);
