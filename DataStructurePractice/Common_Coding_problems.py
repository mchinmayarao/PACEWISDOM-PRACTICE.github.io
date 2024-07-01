def checkAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # return ''.join(sorted(s1)) == ''.join(sorted(s2))
    
    # freq1 = {}
    # freq2 = {}

    # for ch in s1:
    #     if ch in freq1:freq1[ch] += 1
    #     else: freq1[ch] = 1

    # for ch in s2:
    #     if ch in freq2:freq2[ch] += 1
    #     else: freq2[ch] = 1

    freq1 = {i: s1.count(i) for i in set(s1)}
    freq2 = {i: s2.count(i) for i in set(s2)}
    return freq1 == freq2

# print(checkAnagrams('hello','lloeh'))

def firstAndLast(arr,target):
     
     def findStart(arr,target):
         if arr[0] == target:
             return 0
         
         left,right = 0, len(arr)-1

         while left<=right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1]<target:
                return mid
            elif arr[mid] <target:
                left = mid+1
            else:
                right = mid -1  
         return -1  
      
     def findEnd(arr,target):
         if arr[-1] == target:
             return len(arr)-1 
         left,right = 0, len(arr)-1

         while left<=right:
             mid = (left+right)//2
             if arr[mid] == target and arr[mid+1]>target:
                 return mid
             elif arr[mid] > target:
                 right = mid -1
             else:
                 left = mid +1
         return -1
     
     if len(arr) == 0 or target <arr[0] or target >arr[-1]:
         return [-1,-1]
     return [findStart(arr,target) , findEnd(arr,target)]
          

# print(firstAndLast([2,4,5,5,5,5,5,7,9,9],5))


import heapq
def kth_largest(arr,k):
    arr = [ -ele for ele in arr]
    heapq.heapify(arr)
    print(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

# print(kth_largest([2,4,5,5,5,5,5,7,9,9],3))

def symetric_tree(root1,root2):
    #base case when we reach the end of the leaf
    if root1 is None and root2 is None:
        return True
    # one of them exits but other doesnt or root values are different
    elif ((root1 is None) != (root2 is None)) or root1.data != root2.data:
        return False
    # recursively checking for the next subtrees
    else:
        return symetric_tree(root1.left , root2.right) and symetric_tree(root1.right , root2.left)
class Tree:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

     # Insert Node
    def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Tree(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Tree(data)
            else:
               self.right.insert(data)
      else:
         self.data = data

# tree = Tree(3)
# tree.left = Tree(1)
# tree.right = Tree(1)
# print(symetric_tree(tree.left,tree.right))


def gen_parantheses(n):
    def rec(n,diff,comb,combs):
        if diff < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n-1,diff+1,comb,combs)
            comb.pop()
            comb.append(')')
            rec(n-1,diff-1,comb,combs)
            comb.pop()
    combs = []
    rec(2*n,0,[],combs)
    return combs

# print(gen_parantheses(3))

def gas_station(gas,cost):
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] -cost[i]
        if remaining <0:
            candidate = i+1
            remaining = 0
    prev_remaining = sum(gas[:candidate]) - sum(cost[:candidate])

    if candidate == len(gas) or remaining + prev_remaining <0:
        return -1
    else:
        return candidate
    
# gas = [1,5,3,3,5,3,1,3,4,5]
# cost = [5,2,2,8,2,4,2,5,1,2]

# print(gas_station(gas,cost))
from collections import deque
def course_schedule(n, prerequisites):

    graph = [ [] for i in range(n)]
    indegree = [0 for i in range(n)]

    #creating the adjacency matrix
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1

    order = []
    # intiatlizing the queue with all vertex which have indegree = 0
    queue = deque([i for i in range(n) if indegree[i] == 0])

    while queue:
        # poping the first from the queue
        vertex = queue.popleft()
        # since its inorder is 0 we are appending it to the order 
        order.append(vertex)
        # decreasing the inorder of neighbors of the vertex we just removed
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            # whenever the indegree of any of the neighbor becomes 0
            # we are adding it to the queue
            if indegree[neighbor] ==0:
                queue.append(neighbor)
    # if there is a loop in the graph then at a point there will be no vertex with inorder 0 
    # which tells us that no.of courses will be not equal to the order            
    return [len(order) == n , order]

# print(course_schedule(2,[[1,0]]))

def kth_permutation(n,k):
    permutation = []
    unused = list(range(1,n+1))
    fact = [1]*(n+1)

    for i in range(1,n+1):
        fact[i] = i * fact[i-1]

    k -=1

    while n>0:
        part_length = fact[n]//n
        i = k//part_length
        permutation.append(unused[i])
        unused.pop(i)
        n-= 1
        k %= part_length

    return ''.join(map(str,permutation))

print(kth_permutation(4,16))