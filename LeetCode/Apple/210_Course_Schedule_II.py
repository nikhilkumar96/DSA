from header import *
def detect_cycle(dep_course, a, visited, seen, res):
    if dep_course == []:
        return True
    temp = True
    for course in dep_course:
        if course in visited:
            return False
        if course in seen:
            continue

        visited.append(course)
        temp = temp and detect_cycle(a[course], a, visited, seen, res)
        visited.pop()
        seen.add(course)
        if course not in res:
            res.append(course)

    return temp



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        a = {}
        for i in range(numCourses):
            a[i] = []
        seen = set()
        res = []
        for pair in prerequisites:
            a[pair[0]].append(pair[1])
        for k,v in a.items():
            if not detect_cycle(v, a, [k], seen, res):
                return []
            if k not in res:
                res.append(k)

            seen.add(k)
        return res


print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))