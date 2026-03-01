'''1. Create a set with numbers input by the user between 1 to 10 and remove even numbers.
Test Case 1:
•
Input: set(range(1,11))
•
Expected Output: {1, 3, 5, 7, 9}
Test Case 2:
•
Input: {2,4,6,8,10}
•
Expected Output: set()
Test Case 3:
•
Input: {1,2,3,4,5}
•
Expected Output: {1,3,5}'''

def odd(n):
    return {i for i in range(1,n+1) if i % 2 !=0}
print(odd(10))

'''2. Write a program to find union, intersection, and difference of two sets.
Test Case 1:
•
Input: A={1,2,3}, B={3,4,5}
•
Expected Output: Union={1,2,3,4,5}, Intersection={3}, Difference(A-B)={1,2}
Test Case 2:
•
Input: A={10,20}, B={20,30}
•
Expected Output: Union={10,20,30}, Intersection={20}, Difference(A-B)={10}
Test Case 3:
•
Input: A={1}, B={1}
•
Expected Output: Union={1}, Intersection={1}, Difference(A-B)=set()'''

def sets(s1,s2):
    s3 = set()
    dif = {sum(s1)- sum(s2)}
    for i in s1:
        s3.add(i)
        if i in s2:
            intersection = {i}
    for i in s2:
        s3.add(i)        
    return s3,intersection,dif
print(sets({1,2,3}, {3,4,5}))
    
    
'''Write a Python code to check if two sets are disjoint.
Test Case 1:
•
Input: A={1,2}, B={3,4}
•
Expected Output: True
Test Case 2:
•
Input: A={1,2}, B={2,3}
•
Expected Output: False
Test Case 3:
•
Input: A=set(), B={1}
•
Expected Output: True'''
def disjoint(s1,s2):
    s1v = 0
    s2v = 0
    
    for i in s1:
        s1v = i
    for i in s2:
        s2v = i
        break
    if s1v+1 == s2v:
        return True
    else:
        return False
print(disjoint({1,2},{4,4}))

'''4. Write a Python program to add and remove elements from a set.
Test Case 1:
•
Input: s={1,2}; add(3); remove(2)
•
Expected Output: {1,3}
Test Case 2:
•
Input: s=set(); add(5)
•
Expected Output: {5}
Test Case 3:
•
Input: s={10,20}; remove(30)
•
Expected Output: KeyError or Handle Missing Element'''

def rr(s,rm,rp):
    if not s:
        s.add(rp)
    else:
        s.remove(rm)
        s.add(rp)
    return s
print(rr(set(),2,3))

'''5. Write a program to find the maximum and minimum value in a set.
Test Case 1:
•
Input: {1,2,3,4}
•
Expected Output: max=4, min=1
Test Case 2:
•
Input: {10,20,5}
•
Expected Output: max=20, min=5
Test Case 3:
•
Input: {7}
•
Expected Output: max=7, min=7'''

def minmax(s):
    return min(s),max(s)
print(minmax({1,2,3,4}))

'''Write a Python code to convert a list with duplicate values into a set.
Test Case 1:
•
Input: [1,2,2,3]
•
Expected Output: {1,2,3}
Test Case 2:
•
Input: ['a','a','b']
•
Expected Output: {'a','b'}
Test Case 3:
•
Input: []
•
Expected Output: set()'''

def listset(ls):
    return set(ls)
print(listset(['a','a','b']))

'''7. Write a program to check if a given element exists in a set.
Test Case 1:
•
Input: s={1,2,3}, x=2
•
Expected Output: True
Test Case 2:
•
Input: s={'a','b'}, x='c'
•
Expected Output: False
Test Case 3:
•
Input: s=set(), x=5
•
Expected Output: False'''

def setlook(s,x):
    if x in s:
        return True
    else:
        return False
print(setlook({1,2,3},3))

'''Write a Python program to find symmetric difference between two sets.
Test Case 1:
•
Input: A={1,2,3}, B={3,4,5}
•
Expected Output: {1,2,4,5}
Test Case 2:
•
Input: A={10,20}, B={20,30}
•
Expected Output: {10,30}
Test Case 3:
•
Input: A={1,2}, B={1,2}
•
Expected Output: set()'''

def remove(s1,s2):
    s3 = set()
    ls = []
    for i in s1:
        if i in s2:
            ls.append(i)
    for i in ls:
        if i in s2 and i in s1:
            s1.remove(i)
            s2.remove(i)
    for i in s2:
        s1.add(i)
    return s1
print(remove({1,2,3}, {3,4,5}))

'''9. Write a program to check if a set is a subset of another set.
Test Case 1:
•
Input: A={1,2}, B={1,2,3}
•
Expected Output: True
Test Case 2:
•
Input: A={4,5}, B={1,2,3}
•
Expected Output: False
Test Case 3:
•
Input: A=set(), B={1}
•
Expected Output: True'''

def subset(s1,s2):
    for i in s1:
        if i not in s2:
            return False
    return True
print(subset({1,2},{1,2,3}))
'''10. Write a Python code to remove an arbitrary element from a set using pop().
Test Case 1:
•
Input: s={1,2,3}
•
Expected Output: Removes random element; remaining 2 elements
Test Case 2:
•
Input: s={10}
•
Expected Output: set()
Test Case 3:
•
Input: s=set()
•
Expected Output: KeyError'''

def rand(s1):
    s1.pop()
    return s1
print(rand({1,2,3}))
 
'''11. Write a Python code to check if two sets are equal.
Test Case 1:
•
Input: A={1,2}, B={2,1}
•
Expected Output: True
Test Case 2:
•
Input: A={1,2}, B={1,3}
•
Expected Output: False
Test Case 3:
•
Input: A=set(), B=set()
•
Expected Output: True'''

def equal(s1,s2):
    return True if sum(s1)==sum(s2) else False
print(equal({1,3},{3,1}))

'''12. Write a Python program to clear all elements from a set.
Test Case 1:
•
Input: s={1,2,3}
•
Expected Output: set()
Test Case 2:
•
Input: s={'x','y'}
•
Expected Output: set()
Test Case 3:
•
Input: s=set()
•
Expected Output: set()'''

def clear(s1):
    s1 = set()
    return s1
print(clear({1,2,3}))

'''13. Write a Python program to find the difference between two sets using difference() method.
Test Case 1:
•
Input: A={1,2,3}, B={2}
•
Expected Output: {1,3}
Test Case 2:
•
Input: A={5,6}, B={5,6}
•
Expected Output: set()
Test Case 3:
•
Input: A={10,20}, B={30,40}
•
Expected Output: {10,20}'''

def dif(s1,s2):
    s3 = s1.difference(s2)
    return s3
print(dif({10,20},{20,40}))

'''14. Write a Python code to create a frozen set and try to add elements to it.
Test Case 1:
•
Input: fs=frozenset({1,2,3}); fs.add(4)
•
Expected Output: AttributeError
Test Case 2:
•
Input: fs=frozenset()
•
Expected Output: frozenset()
Test Case 3:
•
Input: type(fs)
•
Expected Output: <class 'frozenset'>'''

# def fs(s1):
#     s1 = frozenset(s1)
#     s1.add(4)
#     return s1
# print(fs({1,2,3}))

'''15. Write a Python program to find elements that are common in two sets and also divisible by a given number.
Test Case 1:
•
Input: A = {2, 4, 6, 8} B = {3, 4, 6, 9} n = 2
•
Expected Output: {4, 6}
Test Case 2:
•
Input: A = {10, 15, 20}
B = {5, 10, 25}
n = 5
•
Expected Output: {10}
Test Case 3:
•
Input: A = {1, 3, 5} B = {2, 4, 6} n = 2
•
Expected Output: set()'''

def common(s1,s2, n):
    s3 = set()
    for i in s1:
        for j in s2:
            if i % n == 0 and j%n == 0:
                s3.add(j)
    return s3
print(common({2, 4, 6, 8},{3, 4, 6, 9},2))