"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution:
    @staticmethod
    def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numOfDigit=len(digits)
        if(digits[numOfDigit-1]==9):
            for i in range(numOfDigit-1, -1, -1):
                if (digits[i] == 9 and i == 0):
                    digits[i] = 1
                    digits.append(0)
                elif(digits[i]==9):
                    digits[i]=0
                else:
                    digits[i]=digits[i]+1
                    break
        else:
            digits[numOfDigit-1] = digits[numOfDigit-1]+1
        return digits
        """
        if(digits[len(digits)-1]==9):
            for i in range((len(digits)-1), -1, -1):
                if(digits[i])==9:
                    if(-1<i-1 and digits[i-1]==9):
                        digits[i]=0
                    elif(digits[i-1]<9):
                        digits[i] = 0
                        digits[i-1]=digits[i-1]+1
                        break
                    else:
                        digits[i]=1
                        digits.append(0)
                else:
                    break

        else:
            digits[len(digits) - 1]=digits[len(digits)-1]+1
        return digits
        """
        #------------------------------------------------------------------------------------------
        """
        decNum=0
        for i in range(len(digits)):
            decNum=decNum*10+digits[i]
        decNum=decNum+1
        newDigit=[]
        while(decNum!=0):
            newDigit.append(decNum%10)
            decNum=int(decNum/10)
        newDigit=newDigit[::-1]
        return(newDigit)
        """
nums=[9,0]
print(Solution.plusOne(nums))