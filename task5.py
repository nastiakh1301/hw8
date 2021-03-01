"""
    Реверс подстроки в ()
    Таким образом, чтоб:
    [in]    "(bar)"
    [out]   "rab"

    [in]    "foo(bar)baz"
    [out]   "foorabbaz"

    [in]    "foo(bar)baz(blim)"
    [out]   "foorabbazmilb"

    [in]    "foo(bar(baz))blim"
    [out]   "foobazrabblim"

    так как "foo(bar(baz))blim" -> "foo(barzab)blim" -> "foobazrabblim"
    Данные примеры можете использовать для написания тестов.
"""

s = input()


def reverse_brackets(s):
    i = 0
    se = ""
    while i < (len(s)):
        ch = 1
        if s[i] == ')':
            return s[i-1::-1], i
        if s[i] == '(':
            sd, n = reverse_brackets(s[i+1:])
            se += sd
            i += n + 2
            ch = 0
        if ch == 1:
            se += s[i]
            i += 1
    return se


print(reverse_brackets(s))




t_1 = "(bar)"
assert reverse_brackets(t_1) == "rab"

t_2 = "foo(bar)baz"
assert reverse_brackets(t_2) == "foorabbaz"

t_3 = "foo(bar)baz(blim)"
assert reverse_brackets(t_3) == "foorabbazmilb"

t_4 = "foo(bar(baz))blim"
assert reverse_brackets(t_3) == "foobazrabblim"

