class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 10 - 4 = 6 / 2 = 3
        # 10 - 1 = 9 / 2 = 4.5 -> 5
        # 10 - 0 = 10 / 1 = 10
        # 10 - 7 = 3 / 1 = 3

        cars = []
        for i, pos in enumerate(position):
            cars.append([pos, speed[i]])
        
        cars = list(sorted(cars, reverse=True, key=lambda x: x[0]))
        
        time_stack = []
        for i, car in enumerate(cars):
            time = (target - car[0]) / car[1]
            if len(time_stack):
                if time > time_stack[-1]:
                    time_stack.append(time)
            else:
                time_stack.append(time)
        
        return len(time_stack)