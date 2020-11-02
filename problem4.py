# Homework 3, problem 4

class envelop:
    width = None
    height = None

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return "envelop(" + str(self.width) + "x" + str(self.height) + ")"

    def __repr__(self):
        return self.__str__()

    def contain(self, e):
        # returns true if this envelop can contain envelop e
        if (self.width>e.width and self.height>e.height) or \
           (self.width>e.height and self.height>e.width):
            return True
        return False


def partition(arr, lo, hi):
    # expects an array of envelops
    i = lo-1
    pivot = arr[hi]
    
    for j in range(lo, hi):
        if not arr[j].contain(pivot):
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i+1

def sort_env(arr, lo, hi):
    # part (a)
    # use quicksort to sort the list of envelops
    if lo < hi:
        pi = partition(arr, lo, hi)
        sort_env(arr, lo, pi-1)
        sort_env(arr, pi+1, hi)

def max_nest(arr):
    # part (b)
    # returns the maximum number of nested envelops
    # runs in O(n^2) time
    sort_env(arr, 0, len(arr)-1)
    maxNest = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i].contain(arr[j]):
                if maxNest[i] < maxNest[j]+1:
                    maxNest[i] = maxNest[j]+1
    
    return max(maxNest)
        

print(max_nest([envelop(38,34), envelop(30,40), envelop(10,20), envelop(30,35)]))
