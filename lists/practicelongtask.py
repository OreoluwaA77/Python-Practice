#task 1
fruits=["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])
print(fruits[-1])

#task 2 
print(fruits[1])
print(fruits[3])
print(fruits[1:4:])
print(fruits[::-1])

#task 3
fruits.remove("banana")
fruits.insert(1,"blueberry")
fruits.append("fig")
fruits.append("grapes")
fruits.insert(0,"apricot")
fruits.remove("cherry")
print(fruits)

#task 4
for i in range(len(fruits)):
    print(fruits[i])

#task 5
numbers= [10, 20, 30, 40, 50, 60]
numbers.append(70)
numbers.append(80)
more_numbers=[90,100]
new_list=numbers+more_numbers
new_list.remove(30)
new_list.sort()
new_list.sort(reverse=True)
print(new_list.index(50))
count=0
for i in range (len(numbers)):
    if 20==numbers[i]:
        count=count + 1
print(count)
new_list.reverse()
numbers_copy=new_list.copy()
new_list.clear()
print(new_list)
print(numbers_copy)

#task 6
random=["pen", "book", "bottle", "phone", "laptop", "charger"]
random.remove("bottle")
random.pop(-1)
random.pop(2)
print(random)