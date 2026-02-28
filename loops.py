'''1.
1. Write a Python code to find all elements that appear more than once in a list.
•
Test Cases:
•
Input: [1, 2, 3, 1, 2, 4] → Output: [1, 2]
•
Input: [5, 5, 5, 2, 3] → Output: [5]
•
Input: [1, 2, 3] → Output: []'''

def repeated(ls):
    lis = []
    
    for i in ls:
        s = i
        num = sum(1 if s == j else 0 for j in ls)
        if num >1:
            lis.append(s)
        lis=list(set(lis))
            
    return lis
print(repeated([1, 2, 3]))

'''2.
2. Write a Python code to remove all occurrences of a specific element from a list.
•
Test Cases:
•
Input: ([1, 2, 3, 2, 4], 2) → Output: [1, 3, 4]
•
Input: (['a', 'b', 'a', 'c'], 'a') → Output: ['b', 'c']
•
Input: ([10, 10, 10], 10) → Output: []'''

def removal(lis,alf):
    return [i for i in lis if i != alf]
print(removal([1, 2, 3, 2, 4], 2))

'''3.
3. Write a Python program to reverse a list without using the reverse() method.
•
Test Cases:
•
Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]
•
Input: ['a', 'b', 'c'] → Output: ['c', 'b', 'a']'''

def rev(ls):
    return ls[::-1]
print(rev(['a', 'b', 'c']))

'''4.
4. Write a Python program to count the number of occurrences of a given element in a list.
•
Test Cases:
•
Input: ([1, 2, 3, 1, 1], 1) → Output: 3
•
Input: (['a', 'b', 'a'], 'a') → Output: 2'''

def count(ls,item):
    return sum(1 for i in ls if i == item)
print(count(['a', 'b', 'a'], 'a'))

'''5.
5. Write a Python program to remove duplicates from a list while maintaining order.
•
Test Cases:
•
Input: [1, 2, 2, 3, 1] → Output: [1, 2, 3]
•
Input: ['a', 'b', 'a'] → Output: ['a', 'b']'''

def sets(ls):
    return list(set(ls))
print(sets([ 'b', 'a','a']))

'''6. Write a Python program to find the second largest number in a list.
•
Test Cases:
•
Input: [10, 20, 4, 45, 99] → Output: 45
•
Input: [1, 2, 3] → Output: 2'''

def sl(ls):
    ls = sorted(ls)
    return ls[-2]
print(sl([1, 2,4, 3]))

'''7. Write a Python program to check if a list is sorted or not.
•
Test Cases:
•
Input: [1, 2, 3, 4] → Output: True
•
Input: [3, 2, 1] → Output: False'''

def sort_true(ls):
    lis = sorted(ls)
    return True if ls == lis else False
print(sort_true([1, 5, 3, 4]))

'''8. Write a Python program to merge two lists and remove duplicates.
•
Test Cases:
•
Input: [1, 2, 3], [3, 4, 5] → Output: [1, 2, 3, 4, 5]
•
Input: ['a', 'b'], ['b', 'c'] → Output: ['a', 'b', 'c']'''

def merge(ls1,ls2):
    ls1.extend(ls2)
    return list(set(ls1))
print(merge([1, 2, 3], [3, 4, 5]))

'''9. Write a Python program to rotate a list to the right by k positions.
•
Test Cases:
•
Input: [1, 2, 3, 4, 5], k=2 → Output: [4, 5, 1, 2, 3]
•
Input: [10, 20, 30], k=1 → Output: [30, 10, 20]'''
def rotate(ls,k):
    pass

'''10.
10. Write a Python program to get the common elements between two lists.
•
Test Cases:
•
Input: [1, 2, 3], [2, 3, 4] → Output: [2, 3]
•
Input: ['x', 'y'], ['y', 'z'] → Output: ['y']'''

def common(ls1,ls2):
    lis = []
    for i in ls1:
        for j in ls2:
            if i == j:
                lis.append(i)
    return lis
print(common([1, 2, 3], [2, 3, 4]))


'''11. Write a Python program to flatten a nested list.
•
Test Cases:
•
Input: [[1, 2], [3, 4]] → Output: [1, 2, 3, 4]
•
Input: [[['a']], ['b', 'c']] → Output: ['a', 'b', 'c']'''

def extend(ls):
    lis = []
    
    for i in ls:
        for j in i:
            if isinstance(i,list):
                lis.extend(j)
            else:
                lis.append(j)
    return lis
print(extend( [[['a']], ['b', 'c']]))

'''12. Write a Python program to square every element in a numeric list.
•
Test Cases:
•
Input: [1, 2, 3, 4] → Output: [1, 4, 9, 16]
•
Input: [5, -2, 0] → Output: [25, 4, 0]
•
Input: [] → Output: []'''

def square(ls):
    return [i*i for i in ls]
print(square([5, -2, 0]))

'''13. Write a Python program to split a list into chunks of given size n.
•
Test Cases:
•
Input: ([1, 2, 3, 4, 5], n=2) → Output: [[1, 2], [3, 4], [5]]
•
Input: ([1, 2, 3], n=3) → Output: [[1, 2, 3]]'''

def chunks(ls,size):
    lis = []
    for i in range(0,len(ls),size):
        lis.append(ls[i:i+size])
    return lis
print(chunks([1, 2, 3, 4, 5], 2))

'''14.
14. Write a Python program to find the index of the first occurrence of an element in a list.
•
Test Cases:
•
Input: ([1, 2, 3, 2], 2) → Output: 1
•
Input: (['a', 'b', 'c'], 'c') → Output: 2'''

def ind(ls,item):
    
    for index,element in enumerate(ls):
        if item == element:
            return index
print(ind(['a', 'b', 'c'], 'c'))

'''15.
15. Write a Python program to check if one list is a subset of another list.
•
Test Cases:
•
Input: ([1, 2], [1, 2, 3, 4]) → Output: True
•
Input: ([5, 6], [1, 2, 3]) → Output: False
•
Input: (['a'], ['a', 'b', 'c']) → Output: True'''

def subset(ls1,ls2):
    for i in ls1:
        if i not in ls2:
            return False
        break
    return True
print(subset(['a'], ['a', 'b', 'c']))