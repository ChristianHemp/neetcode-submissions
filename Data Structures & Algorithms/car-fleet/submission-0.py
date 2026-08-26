class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []
        for car in cars:
            if not stack:
                stack.append(car)
                continue
            
            # new fleet starts if car cannot catch up to previous fleet
            if self.getTime(car, target) > self.getTime(stack[-1], target):
                stack.append(car)
        
        return len(stack)
    
    def getTime(self, car: tuple, target: int) -> int:
        return (target - car[0]) / car[1]
