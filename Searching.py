# BINARY SEARCHING 
# O(logn)
# def main():
#     a = [1, 3, 4, 5, 7, 12, 13]
#     k = int(input("Ele : "))
#     s = 0
#     e = len(a) - 1
#     ind = binarySearch(a, s, e, k)
#     if ind is None:
#         print("Not present")
#     else:
#         print("Index : ", ind)

# def binarySearch(a, s, e, k):
#     while s <= e:
#         mid = s + (e-s)//2
#         if a[mid] == k:
#             return mid
#         else:
#             if a[mid] < k:
#                 s = mid + 1
#             elif a[mid] > k:
#                 e = mid - 1
#     else:
#         return None
    
# main()


# FINDING THE FIRST AND LAST OCCURENCE
def main():
    a = [0, 1, 2, 2, 2, 3, 3, 5]
    s = 0
    e = len(a) - 1
    k = int(input("Ele : "))
    res = find_occ(a, s, e, k)
    if res[0] == -1 and res[1] == -1:
        print("No such element present")
    else:
        print(res)

def find_occ(a, s, e, k):
    ans = [-1, -1]
    S = s
    E = e

    # for finding the first occurence 
    while s <= e:
        mid = (s+e)//2
        if a[mid] == k:
            ans[0] = mid
            e = mid - 1

        elif a[mid] > k:
            e = mid - 1

        else:
            s = mid + 1

    # for finding the last occurence
    while S <= E:
        mid = (S+E)//2
        if a[mid] == k:
            ans[1] = mid
            S = mid + 1

        elif a[mid] > k:
            E = mid - 1

        else:
            S = mid + 1
    return ans

main()