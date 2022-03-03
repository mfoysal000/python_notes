# Lesson 7 loops and interations

#for loop
nums = [1,2,3,4,5] #list of numbers

for num in nums:    # to traverse the list, nums, we assign variable, num, the value in nums each time until its depleted
    print(num)



for num in nums:    #traverse the list but stop at 4 using break
    if num == 4:
        print('Found!')
        break     #if break is replaced by continue it would show found! but then continue to print 5
    print(num)


#nested for loop

nums2= [2,4,6,8,10]     #a list of numbers

for num in nums2:         #traversing nums2 for a number then traversing abc for a letter then printing out nums2 num, one letter from 'abc' string
    for letter in 'abc':
        print(num, letter)


#looping for a finite amount of time

for i in range(10):     #prints from 0-9 because last digit is non inclusive due to it starting at 0. so if you put range(1,11) its gonna do 1-10
    print(i)


#while loop --goes infinitely until it meets our condition

x = 0

while x < 15:
    if x == 5:
        break
    print(x)
    x += 1            # once it reaches 15 it wont show it because 15<15 is not true so it doesn't output and breaks free
                        # you can apply a earlier break with a boolean comparison such as if x == 5
                                                                                        #    break


