class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #Optimal solutionT(C(n))==(O(log(n))) and S(C(n))==O(1) as it requires non addition space
        while n>=3:#iterating number till eqaul to 3
            if n%3!=0:return False#checking if number divisbilty by 3  true and printing false
            n=n/3#dividing numebr by 3
        return n==1#printing true and false
