'''

https://leetcode.com/discuss/interview-question/1097692/swiggy-sde-2-hackerrank-oa-flexible-strings

Given a string abccc,
Given are below operations

b can be replaced by c
a can be replaced by b
Can the given string converted to all of the same charcters?
The string abccc can be converted to ccccc by following operations:

Convert b at index 1 to c
Convert a at index 0 to b
Convert b at index 0 to c
The given operations can be performed infinite number of times on the string. We need to find whether the string can be converted to a string containing all same characters.

Note : the operations can be performed in any order and any number of times.

Example 1:
Input :
String - abccc
Operations -

b --> c
a --> b
Output - YES

Example 2:
String - abcdc
Operations:

b --> c
a --> d
Output - NO


'''



from collections import deque


def flexi(stri, graph):
    visited = {i: 0 for i in set(stri)}
    myque = deque(stri[0])
    visited[stri[0]] = 1
    while myque:
        temp = myque.popleft()
        for child in graph[temp]:
            if visited[child] ==0:
                visited[child] =1
                myque.append(child)

    for k,v in visited.items():
        if v==0:
            return 'NO'
    return 'YES'

def main():
    t = int(input())
    for i in range(t):
        stri = input()
        stri = stri.strip()
        m = int(input())
        graph = {}
        for j in range(m):
            temp = input().split(' ')
            if temp[0] not in graph.keys():
                graph[temp[0]] = []
            if temp[1] not in graph.keys():
                graph[temp[1]] = []
            graph[temp[0]].append(temp[1])
            graph[temp[1]].append(temp[0])
        print(flexi(stri, graph))


main()
