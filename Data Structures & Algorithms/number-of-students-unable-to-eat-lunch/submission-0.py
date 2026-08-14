class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        reps = 0

        while reps < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                reps = 0
            else:
                students.append(students.pop(0))
                reps += 1
        
        return len(students)
