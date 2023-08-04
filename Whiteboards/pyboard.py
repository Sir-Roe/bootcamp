'''
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
Example
For n = 240, the output should be
solution(n) = 4.
Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
For n = 808, the output should be
solution(n) = 14.
808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
'''
#Understand. starting from 00:00 return the military time based on the number of minutes passed


#Plan going to recieve time in minutes, so / by 60 % for the remaining minutes

def gettime(n):
    if n> 60:
         minr= n%60
    else:
         minr= n

    hour= n//60

    return sum([int(i) for i in str(minr)])+sum([int(i) for i in str(hour)])

print(gettime(808))
print(gettime(4))


def singlesol(n):
    return sum(map(int, str( n // 60 * 100 + n % 60)))

print(singlesol(808))
print(singlesol(4))