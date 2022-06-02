num = [1, 4, 45, 6, 10, 8]
target = 16
def sum(num, target):
    map_dict = {}
    for i, num in enumerate(num):
        if target-num in map_dict:
            return [map_dict[target-num], i]
        map_dict[num] = i
        return "false"
    







