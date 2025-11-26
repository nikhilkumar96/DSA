Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


class Solution:
    def reformatDate(self, date: str) -> str:
        data = date.split(" ")
        month = str(int(Month.index(data[1]) + 1))
        if len(month) == 1:
            month = "0" + month
        day = data[0][:-2]
        if len(day) == 1:
            day = "0" + day

        return data[2] + '-' + month + '-' + day


print(Solution().reformatDate("20th Oct 2052"))
