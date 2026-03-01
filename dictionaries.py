'''1. Create a dictionary of 5 students with their marks and print the student with the highest marks.
Test Case 1:
•
Input: {'A':85, 'B':90, 'C':78, 'D':92, 'E':88}
•
Expected Output: D
Test Case 2:
•
Input: {'Tom':67, 'Jerry':89, 'Mickey':95, 'Donald':80}
•
Expected Output: Mickey
Test Case 3:
•
Input: {'Raj':60, 'Simran':60, 'Aman':59}
•
Expected Output: Raj or Simran'''

def high(dic):
    for key, element in dic.items():
        if element == max(dic.values()):
            return key
    
   
print(high({'A':85, 'B':90, 'C':78, 'D':92, 'E':88}))
import operator
'''2. Write a Python code to sort a dictionary by its values.
Test Case 1:
•
Input: {'a':3, 'b':1, 'c':2}
•
Expected Output: {'b':1, 'c':2, 'a':3}
Test Case 2:
•
Input: {'x':10, 'y':5, 'z':7}
•
Expected Output: {'y':5, 'z':7, 'x':10}
Test Case 3:
•
Input: {'p':100, 'q':50}
•
Expected Output: {'q':50, 'p':100}'''

def sorting(s1):
    s1 = dict(sorted(s1.items(), key=operator.itemgetter(1)))
    s2 = dict(sorted(s1.items(), key = lambda item: item[1]))
    return s1,s2
print(sorting({'a':3, 'b':1, 'c':2}))


'''3. Write a Python program to merge two dictionaries.
Test Case 1:
•
Input: {'a':1}, {'b':2}
•
Expected Output: {'a':1, 'b':2}
Test Case 2:
•
Input: {'x':10, 'y':20}, {'y':25, 'z':30}
•
Expected Output: {'x':10, 'y':25, 'z':30}
Test Case 3:
•
Input: {}, {'a':5}
•
Expected Output: {'a':5}'''

def merge(d1,d2):
    k2 = {}
    
    k2.update()
    for key,value in d1.items():
        for k2,v2 in d2.items():
            if key == k2:
                d1[key] = v2
    d1.setdefault(k2,v2)
    return d1
print(merge({'x':10, 'y':20}, {'y':25, 'z':30}))

'''4. Write a Python program to remove a key from a dictionary.
Test Case 1:
•
Input: {'a':1, 'b':2, 'c':3}, key='b'
•
Expected Output: {'a':1, 'c':3}
Test Case 2:
•
Input: {'x':10}, key='x'
•
Expected Output: {}
Test Case 3:
•
Input: {'p':5, 'q':6}, key='z'
•
Expected Output: Key not found'''

def rem(d,k):
    d.pop(k)

    return d

print(rem({'a':1, 'b':2, 'c':3},'b'))

'''5. Write a Python code to check whether a key exists in a dictionary.
Test Case 1:
•
Input: {'a':1, 'b':2}, key='a'
•
Expected Output: True
Test Case 2:
•
Input: {'x':5}, key='y'
•
Expected Output: False
Test Case 3:
•
Input: {}, key='a'
•
Expected Output: False'''

def exist(d,k):
    if k in d:
        return True
    else:
        return False
print(exist({'a':1, 'b':2},'z'))

'''6. Write a program to find the sum of all values in a dictionary.
Test Case 1:
•
Input: {'a':10, 'b':20, 'c':30}
•
Expected Output: 60
Test Case 2:
•
Input: {'x':1, 'y':2}
•
Expected Output: 3
Test Case 3:
•
Input: {}
•
Expected Output: 0'''

def sums(d):
    return sum(d.values())
print(sums({'x':1, 'y':2}))

'''7. Write a Python code to invert a dictionary (swap keys and values).
Test Case 1:
•
Input: {'a':1, 'b':2}
•
Expected Output: {1:'a', 2:'b'}
Test Case 2:
•
Input: {'x':5, 'y':5}
•
Expected Output: {5:'y'} (last key kept)
Test Case 3:
•
Input: {'p':True, 'q':False}
•
Expected Output: {True:'p', False:'q'}'''

def swap(d):
    d2 = {}
    for key,value in d.items():
        d2[value] = key
    return d2
print(swap({'x':5, 'y':5}))

'''8. Write a program to find common keys between two dictionaries.
Test Case 1:
•
Input: {'a':1, 'b':2}, {'b':3, 'c':4}
•
Expected Output: {'b'}
Test Case 2:
•
Input: {'x':1}, {'y':2}
•
Expected Output: set()
Test Case 3:
•
Input: {'p':10, 'q':20}, {'q':25, 'p':15}
•
Expected Output: {'p', 'q'}'''

def common(d1,d2):
    d3 = set()
    
    for key , value in d1.items():
        if key in d2:
            d3.add(key)
    return d3
print(common({'p':10, 'q':20}, {'q':25, 'p':15}))

'''9. Write a Python code to convert two lists into a dictionary (keys from list1, values from list2).
Test Case 1:
•
Input: ['a','b','c'], [1,2,3]
•
Expected Output: {'a':1, 'b':2, 'c':3}
Test Case 2:
•
Input: ['x','y'], [10]
•
Expected Output: {'x':10}
Test Case 3:
•
Input: [], []
•
Expected Output: {}'''

def lists(ls,ls2):
    return {x:y for x,y in zip(ls,ls2)}
print(lists(['a','b','c'], [1,2,3]))

'''10. Write a Python code to count frequency of elements in a list using dictionary.
Test Case 1:
•
Input: [1,2,2,3,3,3]
•
Expected Output: {1:1, 2:2, 3:3}
Test Case 2:
•
Input: ['a','b','a']
•
Expected Output: {'a':2, 'b':1}
Test Case 3:
•
Input: []
•
Expected Output: {}'''

def counter(l1):
    d = {}
    for i in l1:
        d.setdefault(i, sum(1 for temp in l1 if temp == i))
    return d
print(counter([1,2,2,2,3,3,3]))
        
'''11. Write a Python code to find keys having a specific value in a dictionary.
Test Case 1:
•
Input: {'a':10, 'b':20, 'c':10}, value=10
•
Expected Output: ['a','c']
Test Case 2:
•
Input: {'x':1, 'y':2}, value=3
•
Expected Output: []
Test Case 3:
•
Input: {'m':5, 'n':5, 'o':6}, value=5
•
Expected Output: ['m','n']'''

def finds(d,v):
    return [key for key,value in d.items() if value == v]
print(finds({'a':10, 'b':20, 'c':10}, 10))

'''12. Write a Python code to create a dictionary from a list of keys with default value 0.
Test Case 1:
•
Input: ['a','b','c']
•
Expected Output: {'a':0, 'b':0, 'c':0}
Test Case 2:
•
Input: []
•
Expected Output: {}
Test Case 3:
•
Input: ['x']
•
Expected Output: {'x':0}'''

def create(ls):
    d = {}
    for i in ls:
        d.setdefault(i,0)
    return d
print(create(['a','b','c']))

'''13. Write a Python code to remove duplicate dictionaries from a list.
Test Case 1:
•
Input: [{'a':1}, {'a':1}, {'b':2}]
•
Expected Output: [{'a':1}, {'b':2}]
Test Case 2:
•
Input: [{'x':10}, {'x':10}]
•
Expected Output: [{'x':10}]
Test Case 3:
•
Input: []
•
Expected Output: []'''

def dups(ls):
    d2 = {}
    lis = []
    for i in ls:
        if i in lis:
            continue
        else:
            lis.append(i)
    return lis
print(dups([{'a':1}, {'a':1}, {'b':2}]))

'''14. Write a Python program to convert a list of tuples into a dictionary.
Test Case 1:
•
Input: [('a',1),('b',2)]
•
Expected Output: {'a':1, 'b':2}
Test Case 2:
•
Input: [('x',10),('x',20)]
•
Expected Output: {'x':20}
Test Case 3:
•
Input: []
•
Expected Output: {}'''

def convert(ls):
    d = {}
    for key ,value in zip(*ls):
        d[key] = value
        
    return d
print(convert([('a',1),('b',2)]))

'''15. Write a Python program to display all key-value pairs in a dictionary using a loop.
Test Case 1:
•
Input: {'a':1, 'b':2}
•
Expected Output: a:1, b:2
Test Case 2:
•
Input: {'x':10}
•
Expected Output: x:10
Test Case 3:
•
Input: {}
•
Expected Output: No items'''

def pairs(dic):
    lis = []
    for key,value in dic.items():
        lis.append(f'{key}:{value}')
    lis = ','.join(lis)
    return lis
print(pairs({'a':1, 'b':2}))