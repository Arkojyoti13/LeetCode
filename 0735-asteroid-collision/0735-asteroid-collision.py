class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if not stack or stack[-1] < 0 or n > 0:
                stack.append(n)
                continue
            while stack and stack[-1] > 0:
                if stack[-1] > abs(n):
                    break
                x = stack.pop()
                if x + n == 0:
                    break
            else:
                stack.append(n)
        return stack