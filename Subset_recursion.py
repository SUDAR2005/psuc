#Python script to find the subsets of given seets using recursion
def find_subsets(s):
    if not s:
        return [[]]
    m = find_subsets(s[1:])
    return(sorted( m + [[s[0]] + n for n in m]))

s = [1, 2, 3]
print(find_subsets(s))