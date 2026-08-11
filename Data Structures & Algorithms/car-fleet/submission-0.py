class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        fleets = [cars[0]]
        for idx in range(1, len(cars)):
            car = cars[idx]
            top = fleets[-1]
            time_top = (target - top[0]) / top[1]
            time_car = (target - car[0]) / car[1]

            if time_car > time_top:
                fleets.append(car)
        
        return len(fleets)