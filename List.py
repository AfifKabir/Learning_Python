#array in c/c++ works as list in python
topics=["C","C++","Python","Java","CSS"]
print(topics)
print(topics[3])
print(topics[1:])
print(topics[-2])
print(topics + ["HTML","Base64"])
#How to check a object in list by 'in' or 'not in'
print("Python" in topics)
print("Python" not in topics)
print(topics * 3)
numbers=[10,34,23,456]
print(len(numbers))
numbers.append(24)
print(numbers)
numbers.insert(2,13)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.remove(10)
print(numbers)
numbers.pop()
num2=numbers.copy()
print(num2)
print(numbers.index(24))
p=[3,4,4,4,3,1]
print(p.count(3))
