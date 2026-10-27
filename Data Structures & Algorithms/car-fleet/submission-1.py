class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        fleets = []
        for car in cars:
            if not fleets:
                fleets.append(car)
                continue
            
            if self.getTime(car, target) > self.getTime(fleets[-1], target):
                fleets.append(car)
            
        return len(fleets)

    def getTime(self, car: tuple, target: int):
        return (target - car[0]) / car[1]