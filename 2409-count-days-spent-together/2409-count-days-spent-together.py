class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        Monthdays = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def getDay(monthAndDate):
            month,days=map(int,monthAndDate.split('-'))
            return sum(Monthdays[0:month-1])+days

        aliceStart = getDay(arriveAlice)
        aliceEnd = getDay(leaveAlice)

        bobStart = getDay(arriveBob)
        bobEnd = getDay(leaveBob)

        start = max(aliceStart, bobStart)
        end = min(aliceEnd, bobEnd)

        return max(0, end - start + 1)