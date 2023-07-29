def prog(s):
    counter = 0
    syms = {}
    for sym in s:
        syms[sym] = syms.get(sym, 0) + 1
        counter += 1

    for sym, counters in syms.items():
        print(f'кол-во "{sym}" = {counters}')
    print(f'{counter= }')

prog('wefFWEWFE')