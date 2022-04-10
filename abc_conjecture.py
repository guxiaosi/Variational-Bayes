#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 14:12:19 2017

@author: guxiaosi
"""
import math
#abc_conjecture
#find the number wether it is a prime number,
def is_prime_num(i):
    num = 0 #counting collection
    for idx in range(1,i+1):
        if i % idx == 0: #whether it only be divided by 1 or itself,
            num += 1
    if num == 2 or num == 1:
        #print("This Number: " + str(i) +" is Prime Number")
        return i
    else:
        #print("This Number: " + str(i) +" is Not Prime Number")
        return False
#testing
#print(is_prime_num(5))
#print(is_prime_num(26))
        
#define find the range number which is prime number,
def find_prime_num(x, y):
    prime_number = [] #prime numbers collection list,
    cal_prime = 0 #counting prime numbers,
    for idx in range(x, y): #from x to y, search the prime number if it is,
        if is_prime_num(idx):
            prime_number.append(is_prime_num(idx))
            cal_prime += 1
    return prime_number#, cal_prime
#testing
#print(find_prime_num(1,100))
        
#define find the prime factor in int(i).
def find_prime_factor(i):
    prime_number = find_prime_num(1,i) #collection the each prime number in itself,
    prime_factor = [] #collection factor list,
    factor_times = [] #collection factor times,
    factor_idx = 0 #factor address
    times = 0 #power
    flag = True
    if i is is_prime_num(i): #whether number be prime number,
        prime_factor.append(i)
        factor_idx += 1
        factor = i
        times += 1
        factor_times.append([factor_idx, factor, times]) #if yes, collected,
        #print("get the No." + str(factor_idx)+ 
             #" factor: " + str(factor) + " and the times is: " + str(times))
    else: #e.g. 20 = 2*2*5, 25 = 5*5, 30 = 2*3*5, 1024 = 2^10, 1054 = 2*17*31
        for factor in prime_number[1:-1]: #whether the number could be devide by it's factors,
            while flag:
                if i%factor == 0:
                    i = i//factor
                    times += 1
                    #print("i am factor:" + str(factor))
                else:
                    if times >= 1:
                        prime_factor.append(factor)
                        factor_idx += 1
                        factor_times.append([factor_idx, factor, times])
                        #print("get the No." + str(factor_idx)+ 
                              #" factor: " + str(factor) + " and the times is: " + str(times))
                        times = 0 #reset times
                        flag = False #reset flag
                    else:
                        flag = False
            flag = True
            if i is is_prime_num(i) and i != 1:
                prime_factor.append(i)
                factor_idx += 1
                factor = i
                times = 1
                factor_times.append([factor_idx, factor, times])
                #print("get the No." + str(factor_idx)+ 
                      #" factor: " + str(factor) + " and the times is: " + str(times))
                break
            elif i == 1:
                break
            else:
                #print("search times")
                continue

    return prime_factor#, factor_times  
#testing
#print(find_prime_factor(6285))

#define random number's factor product,
def rad_all_factor(i):
    rad_all_product = 1
    factor_collection = find_prime_factor(i)
    #print(factor_collection)
    for idx in factor_collection:
        rad_all_product = rad_all_product * idx
    return rad_all_product
#testing
#print(rad_all_factor(6285))
#print(rad_all_factor(30))

#define find two int whether they are relatively prime.
def is_relatively_prime(a,b):
   relatively_prime = []
   prime_factor_a_list = set(find_prime_factor(a))
   prime_factor_b_list = set(find_prime_factor(b))
   if a is is_prime_num(a) and b is is_prime_num(b):
       relatively_prime.extend([a,b])
       return relatively_prime
   elif prime_factor_a_list & prime_factor_b_list == set():
       relatively_prime.extend([a,b])
       return relatively_prime
   else:
       return False    
#testing
#print(is_relatively_prime(2,9))
#print(is_relatively_prime(3,6))

# a + b = c guessing problem.
def find_c_prime(i):
    cal_find_c_prime = 0
    find_c_prime_number = []
    for idxa in range(1,i+1):
        for idxb in range(1,i+1):
            if is_relatively_prime(idxa,idxb):
                idxc = idxa + idxb
                if is_relatively_prime(idxa,idxc) and is_relatively_prime(idxb,idxc):
                    if idxa < idxb and idxc < i:
                        find_c_prime_number.extend([[idxa,idxb,idxc]])
                        cal_find_c_prime +=1
                    else:
                        continue
                else:
                    continue
            else:
                continue
    return find_c_prime_number#, cal_find_c_prime
#testing
#print(find_c_prime(100))

#define q_list return rad(abc) compare with c
def q_list(c_list):
    rad_abc = 1
    for idx in range(len(c_list)):
        rad = rad_all_factor(c_list[idx])
        rad_abc = rad_abc * rad
    q_abc = math.log(c_list[2])/math.log(rad_abc)
    return q_abc
#testing
#print(q_list([1,4374,4375]))
#print(q_list([4,127,131]))
#print(q_list([3,125,128]))

#define a method to check whether q >= 1's result
def q_method(i):
    find_c_prime_number = find_c_prime(i)
    #print(find_c_prime(i))
    q_method_collection = []
    cal = 0
    abc_prime = []
    for c_list in find_c_prime_number:
        #print(c_list)
        if q_list(c_list) >= 1:
            cal += 1
            q_method_collection.append(q_list(c_list))
            abc_prime.append(c_list)
        else:
            continue
    return q_method_collection, cal, abc_prime
#testing
print(q_method(100))


