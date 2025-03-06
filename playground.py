import pandas as pd
import numpy as np

#print('hello sree sir')

def add(n1: int, n2: int) -> int:
    n3 = n1 + n2
    return n3

#print(add(5,6))

'''Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
'''
# brute force 1
def target_tuple(lis, targ):
    n = len(lis)
    for i in range(n-1):
        for j in range(i+1, n):
            if lis[i]+lis[j] == targ:
                return i, j
    return []

nums = [3,2,4,6,12,1]
targe = 9
#print(target_tuple(nums, targe))

# brute force 2
def tester(lis, targe):
    for i in range(len(lis)-1):
        for j in range(i+1, len(lis[::-1])):
            if lis[i]+lis[j]==targe:
                return i, j
    return []
#print(tester(nums, targe))

# 1 pass hash table
def one_pass_hash(nums, targe):
    dict_repo={}
    n = len(nums)
    for i in range(n):
        complement = targe - nums[i]
        if complement in dict_repo:
            return  dict_repo[complement], i
        dict_repo[nums[i]] = i
    return []
#print(one_pass_hash(nums, targe))

# 2 pass hash table
def two_pass_hash(nums, targe):
    repo_dict={}
    n = len(nums)
    # build hash table
    for i in range(n):
        repo_dict[nums[i]] = i
    # find complement of above key
    for i in range(n):
        complement = targe-nums[i]
        if complement in repo_dict and repo_dict[complement] != i:
            return i, repo_dict[complement]
    return []
#print(two_pass_hash(nums, targe))

# Given an integer x, return true if x is a palindrome, and false otherwise
'''Input: x = 121 Output: true; input x = 195 output: false
x = 195
divide x by 10
store remainder 5 in a reverse variable
shift reverse variable by 1 place left by adding remainder to reverse variable
by multiplying with 10 to obtain like 5x10=50
update x by removing last digit by integer division with x//10
loop thru all the digits
compare input & reversed number and return result
'''
def num_palindrome(x):
    if x < 0:
        return False
    reverse_num = 0
    x_copy = x
    while x > 0:
        reverse_num = x % 10 + (reverse_num * 10)
        x //= 10
    return x_copy == reverse_num
#print(num_palindrome(64646))

# Roman to integer: https://www.geeksforgeeks.org/python-program-for-converting-roman-numerals-to-decimal-lying-between-1-to-3999/
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

1 - i
2 - ii
3 - iii
4 - iv
5 - v
6 - vi
7 - vii
8 - viii
9 - ix
10 - x
11 - xi
48 - XLVIII
49 - XLIX
50 - L
# symbols I, X, C, M can be repeated 3 times only
# symbols V, L, D are never repeated
'''
from collections import Counter
def roman_to_integer(rom_number):
    roman_map ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_num = list(rom_number.upper())
    integer = 0
    count = Counter(rom_num)
    if set(rom_num).issubset(list(roman_map.keys())):
        if count['i']<=3 and count['x']<=3 and count['c']<=3 and count['m']<=3 and count['v']<=1 and count['l']<=1 and count['d']<= 1:
            for i in range(len(rom_num)):
                integer += roman_map[rom_num[i]]
    return integer

#print(roman_to_integer('mdcl')) # for MCMXCIV, expected 1994

def reverse_adding():
    roman_map ={'I': 1, 'V': 5, 'X': 10, 'L': 50}
    lis = ['I','V','L','X'] #'m', 'd', c', 'x', 'i'
    keys = list(roman_map.keys())
    if any(lis) == all(keys[::]):
        return 'in good order'
    return 'not in good order'

#print(reverse_adding())

# find elements that are in same sequence of a list

# Longest common prefix string in a list of strings. If no common prefix, return empty string
# https://www.geeksforgeeks.org/python-program-to-find-longest-common-prefix-using-sorting/

def longest_common_prefix(str_list):
    common = []
    for i in range(len(str_list)):
        for j in range(1, len(str_list)):
            if str_list[i][0:i] == str_list[j][0:j]:
                common.append(str_list[i][0:i])
    return common

strs = ['flower','flew','flight','flaunt']
#print(longest_common_prefix(strs))

# Find the Length of the Longest Common Prefix

# check if it is valid parentheses: '(', ')', '{', '}', '[' and ']'
'''An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type'''

def valid_parenthesis(s):
    s_list = list(s)
    parenthesis = [ '(', ')', '[', ']', '{', '}']
    if len(s) % 2 != 0:
        return False
    else:
        for i in range(len(s_list)):
            if s_list[i] in parenthesis:
                continue
            return False
        return True

se = '()[]{}'
#print(valid_parenthesis(se))

# find common elements in 2 lists
l1 = [4,7,2,9,3]
l2 = [6,9,1,5,7]
def common_elements(l1, l2):
    common = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                common.append(l1[i])
    return common

#print(common_elements(l1, l2))

def common_elements2(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    if set1.intersection(set2):
        return True
    return False

#print(common_elements2(l1, l2))

#reverse order of a dictionary
sample_dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
def dict_reverse(d):
    new_dict = {}
    ls = list(d.keys())[::-1]
    for i in range(len(ls)):
        new_dict[ls[i]] = d[ls[i]]
    return new_dict

#print(dict_reverse(sample_dict))

'''Search: linear search, binary search, jump search, interpolation search except linear search rest all work for sorted list'''

ls = [336,93,217,520,246,111,468]

def linear_search_iterative(lis, target):
    for i in range(len(lis)):
        if lis[i] == target:
            return i
    return -1

#print(linear_search_iterative(ls, 520))

def linear_search_recursive(lis, target, index=0):
    if index == len(lis):
        return -1
    if lis[index] == target:
        return index
    else:
        return linear_search_recursive(lis, target, index+1)

#print(linear_search_recursive(ls, 520))

#https://www.geeksforgeeks.org/python-program-for-binary-search/
#https://github.com/kying18/beginner-projects/blob/master/binary_search.py

def binary_search_iterative(lis, target): #iterative
    lis = sorted(lis)
    low = 0
    high = len(lis)-1
    mid = 0
    while low <= high:
        mid = (high+low) // 2
        if lis[mid] < target:
            low = mid+1
        elif lis[mid] > target:
            high = mid-1
        else:
            return mid
    return -1

#print(binary_search_iterative(ls, 336))

def binary_search_recursive(lis, target, low=0, high=len(ls)-1): #recursive
    lis = sorted(lis)
    if low <= high:
        mid = (high+low) // 2
        if lis[mid] > target:
            return binary_search_recursive(lis, target, low, mid-1)
        elif lis[mid] < target:
            return binary_search_recursive(lis, target, mid+1, high)
        else:
            return mid
    return -1

#print(binary_search_recursive(ls, 336))

# https://www.geeksforgeeks.org/jump-search/
import math
def jump_search(lis, target):
    lis = sorted(lis)
    n = len(lis)
    block = math.sqrt(n)
    previous = 0
    #finding block where element is present (if it is present)
    while lis[int(min(block, n)-1)] < target:
        previous = block
        block += math.sqrt(n)
        if previous >= target:
            return -1
    #linear search for x in block beginning with previous
    while lis[int(previous)] < target:
        previous+=1
        #if we reached next block or end of array, element is not present
        if previous == min(block, n):
            return -1
    #if element is found
    if lis[int(previous)] == target:
        return int(previous)
    return -1

#print(jump_search(ls, 336))

#https://www.geeksforgeeks.org/interpolation-search/
def interpolation_search_recursive(lis, target, low, high):
    lis = sorted(lis)
    if (low <= high and target >= lis[low] and target <= lis[high]):
        position = low + (((target-lis[low])*(high-low))//(lis[high]-lis[low]))
        if lis[position] < target:
            return interpolation_search_recursive(lis, target, position+1, high)
        elif lis[position] > target:
            return interpolation_search_recursive(lis, target, low, position-1)
        else:
            return position
    return -1

#print(interpolation_search_recursive(ls, 336, 0, len(ls)-1))

def interpolation_search_iterative(lis, target):
    lis = sorted(lis)
    low = 0
    high = len(lis) -1
    while (low <= high and target >= lis[low] and target <= lis[high]):
        if low == high:
            if lis[low] == target:
                return low
            return -1
        # probing position of target element with block size
        position = low + (((target-lis[low])*(high-low))//(lis[high]-lis[low]))
        #if target found
        if lis[position] < target:
            low = position+1
        elif lis[position] > target:
            high = position-1
        else:
            return position
    return -1

#print(interpolation_search_iterative(ls, 336))

'''Sort: bubble sort, selection sort, insertion sort, merge sort, quick sort, heap sort, radix sort'''

# bubble sort: time complexity is O(n^2) space complexity is O(1) as no additional memory space needed
def bubble_sort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

#print(bubble_sort(ls))

# selection sort: time complexity is O(n^2) as there are two nested for loops, space complexity is O(1) as extra memory used for temp variables
def selection_sort(lis):
    for i in range(len(lis)):
        min_index = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_index]:
                min_index = j
        lis[i], lis[min_index] = lis[min_index], lis[i]
    return lis

print(selection_sort(ls))

# insertion sort: time complexity is O(n2) as there are two nested for loops, space complexity is O(1)
def insertion_sort(lis):
    return pass


# quick sort:

# merge sort: