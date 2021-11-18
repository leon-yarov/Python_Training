def geometric_progression(a,q,n):
    """
    Question 1
    Prints a geometric progression based on the parameters
    a - first progression item
    q - multiplicator
    n - number of items
    No return value
    """
    if n < 0: return
    i,v = 0,a
    while i != n:
        print(f'{v * q**i}', end = ', ')
        i += 1




def reverse(n):
    """
    Question 2
    Reverses the number
    n - the number to reverse
    returns the reversed number
    """
    if n < 0: return
    v,ans = n,0
    while v > 0:
        ans = ans * 10 + v % 10
        v //= 10
    return ans



def removeDigit(n,d):
    """
        Question 3
        Removes every instance of a digit from the number
        n - input number
        d - digit to remove
        Return the number without the digit(s)
    """
    if n < 0: return
    v, ans = n, 0
    while v > 0:
        if v % 10 == d: v //= 10
        ans = ans * 10 + v % 10
        v //= 10
    return reverse(ans)



def figure(n):
    """
    Question 4
    Draws a triangle using digits from 1 to n
    n - input number
    Return nothing
    """
    if n < 0: return
    i,s = 1, n*2-2
    while i <= n:
        print(' '*s, end = ' ')
        j, s = 1, s - 2
        while j <= i:
            print(j, end=' ')
            j += 1
        i += 1
        print()


def printEvenDigits(n):
    """
    Question 5
    Prints the even digits out the the number
    n - input number
    Return nothing
    """
    if n <= 0:
        return
    printEvenDigits(n//10)
    if n % 2 == 0:
        print(n%10,end='')



def mulPrimeNumbers(n):
    """
        Question 6
        Calculates the multiplication of all the prime numbers inside the number
        n - input number
        Return the multiplication of prime numbers
    """
    v,ans,mul = n, 1,0
    while v > 0:
        a = v % 10
        if a == 2 or a == 3 or a == 5 or a == 7:
            ans,mul = ans * (a % 10), mul + 1
        v //= 10
    return ans if mul > 0 else 0



def luckyNumber(n):
    """
      Question 7
      Checks is the input number is a lucky number
      n - 6 digit input number
      Return True if number is lucky, False otherwise
    """
    v, i, num1, num2 = n, 0, 0, 1
    while v > 0:
        if i >= 3: num2 *= v % 10
        if i < 3: num1 += v % 10
        v,i = v//10, i + 1
    return num1 == num2

