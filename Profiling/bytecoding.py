import dis
def fn_expressive(upper= 1_000_000):
    total=0
    for n in range(upper):
        total += n
    return total

def fn_slim(upper=1_000_000):
    return sum(range(upper))


dis.dis(fn_expressive)
print("\n\n\n")
dis.dis(fn_slim)

