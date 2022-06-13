

def lswd(string):
    last_seen = { }
    longest = [0, 1]
    start_idx = 0
    for i, char in enumerate(string):
        if char in last_seen:
            start_idx = max(start_idx, last_seen[char] + 1)
            if longest[1] - longest[0] < i+1 - start_idx:
                longest = [start_idx, i+1]
                last_seen[char] = i
                return string[longest[0] : longest[i]]


string = "clement is a cap"
lswd(string)

