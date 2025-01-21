#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    result = []
    for i in range(2):
        result.append(tuple_a[i] + tuple_b[i])
    return tuple(result)
