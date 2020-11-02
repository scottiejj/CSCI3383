# Homework 3, problem 2

inf = float("inf")
ninf = float("-inf")

def findMax(exp):
    # construt lists of operators and numbers
    ops = []
    nums = []
    
    readingNum = False
    negate = False
    for i in exp:
        if i=="(" or i==")":
            continue
        elif i=="*" or i=="+":
            ops.append(i)
            readingNum = False
        elif i == "-":
            negate = True
        else:
            if readingNum == False:
                if negate == True:
                    nums.append(-int(i))
                    negate = False
                else:
                    nums.append(int(i))
                readingNum = True
            else:
                num = nums[len(nums)-1]
                if num < 0:
                    nums[len(nums)-1] = num*10 - int(i)
                else:
                    nums[len(nums)-1] = num*10 + int(i)

    print(ops,nums)
    
    # 2-dim array to store the maximum value
    # [begin][end]
    maxVal = [[ninf for i in range(len(nums))] for j in range(len(nums))]
    for i in range(len(nums)):
        maxVal[i][i] = nums[i]

    # main section
    # runs in O(n^3) time
    for diff in range(2,len(nums)+1):
        for i in range(len(nums)-diff+1):
            j = i+diff-1
            for k in range(i,j):
                temp = ninf
                if ops[k] == "*":
                    temp = maxVal[i][k] * maxVal[k+1][j]
                elif ops[k] == "+":
                    temp = maxVal[i][k] + maxVal[k+1][j]
                if (temp>maxVal[i][j]):
                    maxVal[i][j] = temp

    print(maxVal)
    
    return maxVal[0][len(nums)-1]
    

print(findMax("1+2*3+4*5"))
