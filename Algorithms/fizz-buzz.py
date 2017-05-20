class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(n):
            # print(i)
            if (i+1) % 3 == 0:
                print(i+1)
                if (i+1) % 5 == 0:
                    res.append("FizzBuzz")
                else:
                    res.append("Fizz")
            elif (i+1) % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i+1))
        return res
