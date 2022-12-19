from typing import List, Tuple


def mod(a: int, b: int) -> int:
    if a < b:
        return a
    return mod(a - b, b)


def secondary(seq: List[str]) -> int:
    if len(seq) < 3:
        return int(seq[-1])
    if int(seq[1]) > int(seq[0]):
        seq[0], seq[1] = seq[1], seq[0]
    if int(seq[0]) != int(seq[2]):
        if int(seq[2]) > int(seq[0]):
            if seq[0] > seq[1]:
                seq[1] = seq[0]
            seq[0] = seq[2]
        elif int(seq[2]) > int(seq[1]):
            seq[1] = seq[2]
    seq.pop(2)
    return secondary(seq)


print(mod(8, 3))
print(mod(9, 3))
print(mod(10, 3))
print(mod(11, 3))
print(mod(12, 3))

print(secondary(list("4579513890")))
print(secondary(list("4579513840")))
print(secondary(list("4587513840")))