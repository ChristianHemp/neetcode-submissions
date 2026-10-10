class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0

        for detail in details:
            substr = detail[-4:-2]
            if int(substr) > 60:
                count += 1
        
        return count