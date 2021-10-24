def iq_test(numbers):
    buffer = numbers.split()
    buffer = [int(x) for x in buffer]
    
    odd = [y for y in buffer if y%2 != 0]
    even = [z for z in buffer if z%2 == 0]
    return buffer.index(min(odd) if len(odd) < len(even) else min(even)) + 1
    
print(iq_test("1 2 2"))
    
    