
def merge(A,B):
    pA = 0
    pB = 0
    result = []
    lenA = len(A)
    lenB = len(B)
    A.append(float("inf"))
    B.append(float("inf"))
    while pA < lenA or pB < lenB:
        if A[pA] < B[pB]:
            result.append(A[pA])
            pA += 1
        else:
            result.append(B[pB])
            pB += 1
    return result

def sort(A):
    lenA = len(A)
    if lenA == 1:
        return A
    left = sort(A[:lenA//2])
    right = sort(A[lenA//2:])
    return merge(left,right)

def merge_sort(arrayin):
    if len(arrayin) == 0:
        print("Error, Empty array entered.")
        exit()

    array =[]
    for x in arrayin:
        try:
            array.append(int(x))
        except:
            print("Only integers are passed into array.")
            pass

    return sort(array)
