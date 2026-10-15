class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        time_stack = []
        
        for pzn, spd in cars:
            time = (target - pzn) / spd

            if not time_stack or time > time_stack[-1]:
                time_stack.append(time)
        
        return len(time_stack)


        

        