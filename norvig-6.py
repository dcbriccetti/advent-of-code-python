from typing import List

def data(day: int, parser=str, sep='\n') -> list:
    "Split the day's input file into sections separated by `sep`, and apply `parser` to each."
    with open(f'data/advent2020/input{day}.txt') as f:
        sections = f.read().rstrip().split(sep)
        return list(map(parser, sections))

def do(day, *answers) -> List[int]:
    "E.g., do(3) returns [day3_1(in3), day3_2(in3)]. Verifies `answers` if given."
    g = globals()
    got = []
    for part in (1, 2):
        fname = f'day{day}_{part}'
        if fname in g:
            got.append(g[fname](g[f'in{day}']))
            if len(answers) >= part:
                assert got[-1] == answers[part - 1], (
                    f'{fname}(in{day}) got {got[-1]}; expected {answers[part - 1]}')
        else:
            got.append(None)
    return got

cat = ''.join

def lines(text: str) -> List[str]:
    "Split the text into a list of lines."
    return text.strip().splitlines()

Group = List[str]

in6: List[Group] = data(6, lines, sep='\n\n')


def day6_1(groups):
    "For each group, compute the number of letters that ANYONE got. Sum them."
    return sum(len(set(cat(group)))
               for group in groups)


def day6_2(groups):
    "For each group, compute the number of letters that EVERYONE got. Sum them."
    return sum(len(set.intersection(*map(set, group)))
               for group in groups)


do(6, 11)
