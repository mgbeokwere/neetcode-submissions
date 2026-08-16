class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        result = len(students)
        preference_count = Counter(students)

        for s in sandwiches:
            if  preference_count[s] > 0:
                result -=1
                preference_count[s] -=1
            
            else:
                return result

        return result


        