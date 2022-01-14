from itertools import zip_longest, islice


def suffix_matrix_smart(to_int_keys, s):
    n = len(s)
    k = 1
    line = to_int_keys(s)
    ans = [line]
    while max(line) < n - 1:
        line = to_int_keys(
            list(zip_longest(line, islice(line, k, None),
                             fillvalue=-1)))
        ans.append(line)
        k <<= 1
    return ans


def to_int_keys(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    index = {v: i for i, v in enumerate(sorted(set(l)))}
    return [index[v] for v in l]


def suffix_matrix(to_int_keys, s):
    n = len(s)
    k = 1
    line = to_int_keys(s)
    ans = [line]
    while k < n:
        line = to_int_keys(
            list(zip_longest(line, islice(line, k, None),
                             fillvalue=-1)))
        ans.append(line)
        k <<= 1
    return ans


def lcp(sm, i, j):
    """
    longest common prefix
    O(log(n))

    sm: suffix matrix
    """
    n = len(sm[-1])
    if i == j:
        return n - i
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


print(lcp(suffix_matrix(to_int_keys, 'banana'), 2, 4))
print(lcp(suffix_matrix_smart(to_int_keys, 'banana'), 2, 4))

