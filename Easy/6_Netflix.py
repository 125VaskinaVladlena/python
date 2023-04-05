def netflix(x, y, z, cost):
    if x + y + z <= cost:
        return "impossible"
    
    pos_comb = [(x+y, z), (x+z, y), (y+z, x)]
    best_comb = min(pos_comb, key=lambda comb: abs(comb[0] + comb[1] - cost))
    
    if best_comb[0] == x:
        return "Alice", "Bob"
    elif best_comb[0] == y:
        return "Bob", "Charlie"
    else:
        return "Alice", "Charlie"

x = int(input("Alice's money: "))
y = int(input("Bob's money: "))
z = int(input("Charlie's money: "))
cost = int(input("Price: "))

n = netflix(x, y, z, cost)
print(n)