# Week 1 Lab

# Write a method that combines two strings, by taking one character from the first string, then one from the second string and so on. Once one string has no characters left it should carry on with the other string.

def merge(l, m):
    result = []
    i = j = 0
    total = len(l) + len(m)
    while len(result) != total:
        if len(l) == i:
            result += m[j:]
            break
        elif len(m) == j:
            result += l[i:]
            break
        elif l[i] < m[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(m[j])
            j += 1
    return result


extendedString()


