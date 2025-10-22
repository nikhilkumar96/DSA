
# def find_data(arr):
#     for i in range(len(arr)-1,0,-1):
#         if arr[i] - arr[0] <=100:
#             return arr[0:i+1]


def check_irregularity(arr):
    if len(arr)<3:
        return False
    for i in range(len(arr)-2):
        if arr[i+2] -arr[i] <100:
            return True
    return False

def badge(badge_times):
    a = {}
    for name, time in badge_times:
        if name not in a:
            a[name] = [int(time)]
        else:
            flag = False
            for t in range(len(a[name])):
                if int(a[name][t]) >= int(time):
                    a[name].insert(t, int(time))
                    flag=True
                    break
            if not flag:
                a[name].append(int(time))
    result = []
    for name, times in a.items():
        res = check_irregularity(times)
        if res:
            result.append(name)
    return result












badge_times = [
["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
["Jennifer", "5"], ["Chloe", "1909"], ["Zhang", "1"],
["Zhang", "10"], ["Zhang", "109"], ["Zhang", "110"],
["Amos", "1"], ["Amos", "2"], ["Amos", "400"],
["Amos", "500"], ["Amos", "503"], ["Amos", "504"],
["Amos", "601"], ["Amos", "602"], ["Paul", "1416"],
];
print(badge(badge_times))