def detect_cycle(dep_course, a, visited):
    if dep_course == []:
        return True
    temp = True
    for course in dep_course:
        if course in visited:
            return False
        visited.append(course)
        temp = temp and detect_cycle(a[course], a, visited)
        visited.pop()
    return temp



def canFinish(numCourses, prerequisites):
    a = {}
    for i in range(numCourses):
        a[i] = []

    for pair in prerequisites:
        a[pair[0]].append(pair[1])
    for k,v in a.items():
        if not detect_cycle(v, a, [k]):
            return False
    return True


print(canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
