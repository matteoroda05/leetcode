class Solution:
    def canFinishQUadratic(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for a in range(numCourses):
            req = set()
            i = 0
            while i < len(prerequisites):
                a1, b1 = prerequisites[i]
                # print(f"a, a1, b1: {a}, {a1}, {b1}")
                if a1 == a or a1 in req:
                    if b1 == a:
                        return False  
                    elif b1 not in req:
                        # print(f"adding b1: {b1}")
                        req.add(b1)
                        i = -1
                i+=1

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre = defaultdict(list)

        for course, p in prerequisites:
            pre[course].append(p)
        
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in pre[course]:
                if not dfs(p): return False
            
            pre[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True