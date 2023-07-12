# def main():
#     a = [2, 3, 4, 5, 6, 6]
#     ans = isSorted(a, len(a))
#     if ans == True:
#         print("Sorted array")
#     else:
#         print("Not sorted")

# def isSorted(a, size):
#     if (size == 0 or size == 1):
#         return True
    
#     if a[0] > a[1]:
#         return False

#     else:
#         a = a[1:]
#         size -= 1
#         return isSorted(a, size)
# main()
    


# BINARY SEARCH USING RECURSION
# def main():
#     a = [-6, -5, -1, 0, 1, 2, 3, 4, 6, 8, 11, 13, 17, 19, 20]
#     s = 0
#     e = len(a)
#     k = 20
#     print(a)
#     ans = binarySearch(a, s, e, k)
#     if ans == True:
#         print("present")
#     else:
#         print("absent")

# def binarySearch(a, s, e, k):
#     if s > e :
#         return False
    
#     mid = int((s+e)/2)
#     print("mid : ", a[mid])

#     if a[mid] == k:
#         return True
#     else:
#         if a[mid] < k:
#             s = mid + 1
#             print("\n", a[s : e])
#             return binarySearch(a, s, e, k)
#         elif a[mid] > k:
#             e = mid - 1
#             print("\n", a[s : e])
#             return binarySearch(a, s, e, k)
    

# main()



# REVERSING A STRING USING RECURSION
# def main():
#     string = 'abcdefg'
#     new = list(string)
#     print(string)
#     s = 0
#     e = len(string) - 1
#     reverse_string(new, s, e)
#     string = ''.join(new)
#     print(string)

# def reverse_string(new, s, e):
#     if s > e:
#         return 
#     else:
#         new[s], new[e] = new[e], new[s]
#         print("..")
#         return reverse_string(new, s + 1, e - 1)
    
# main()


# FINDING BASE TO THE POWER
# def main():
#     b = int(input("Base : "))
#     pow = int(input("Power : "))
#     ans = power(b, pow)
#     print(ans)

# def power(b, pow):
#     if pow == 0:
#         return 1
#     if pow == 1:
#         return b
    
#     ans = power(b, pow//2)

#     if pow & 1 == 0:
#         return ans * ans
#     else:
#         return b * ans * ans

#     return ans 
# main()



# PEAK OF A MOUNTAIN
# def main():
#     a = [ 5, 3, 3, 2, 1]
#     r = peak_graph(a)
#     print(a[r])

# def peak_graph(a):
#     s = 0
#     e = len(a) - 1
#     mid = s + (e - s)//2
#     while s < e:
#         if a[mid] >= a[mid + 1]:
#             e = mid
#         elif a[mid] < a[mid + 1]:
#             s = mid + 1
#         mid = s + (e - s)//2
#     return mid

# main()


# def main():
#     a = [ 12, 5, 7, 8, 9, 10]
#     r = pivot_index(a)
#     print(r)

# def pivot_index(a):
#     s = 0 
#     e = len(a) - 1
#     mid = (e + s)//2
#     while s < e:
#         if a[mid] >= a[0]:
#             s = mid + 1
#         else:
#             e = mid
#         mid = (s + e)//2
#     return s

# main()

# def sqrtInteger(x):                 # finding square root of a number
#     s = int(0)
#     e = int(x)
#     mid = (s + e)//2
#     ans = int(-1)
#     while s <= e:
#         if mid * mid == x:
#             ans = mid
#             return ans
#         if mid * mid < x:
#             ans = mid
#             s = int(mid + 1)
#         else:
#             e = int(mid - 1)
#         mid = (s + e)//2

#     factor = 0.1
#     while factor > 0.0001:
#         for i in range(0, 10):
#             if ans * ans > x:
#                 factor = factor/10
#                 break
#             if ans * ans < x:
#                 ans = ans + factor 
#     return ans

# ans = sqrtInteger(30)
# print(ans)



def isPossible(a, m, mid):
    count = 0
    studentCount = 1
    # print(mid)
    for i in range(len(a)):
        if count + a[i] <= mid:
            # print(f"\t count : {count}")
            count += a[i]
            # print(f"\tcount + a[i] : {count}")
        else:
            studentCount += 1
            # print("\t", studentCount)
            if studentCount > m or a[i] > mid:
                return False
            count = a[i]

    return True

def bookAllocation(a, sum, m):
    s = 0
    e = sum
    mid = (s + e)//2
    ans = -1
    while s <= e:
        if (isPossible(a, m, mid) is True):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
        mid = (s + e)//2
    return ans

def main():
    a = [10, 20, 30, 40, 50]
    sum = 0
    m = 2
    for i in a:
        sum = sum + i
    e = bookAllocation(a, sum, m)
    return e
m = main()
print(m)