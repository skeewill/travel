

def union(set1, set2):
    return set(set1) & set(set2)


def possible(set1, set2, set3):
    s1 = union(set1, set2)
    print(s1)
    s2 = union(set2, set3)
    if len(s1) > 0 and len(s2) > 0:
        return(True)
    else:
        return(False)
