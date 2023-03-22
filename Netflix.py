def netflix(x, y, z, cost):
    pos_comb = [(x+y, z), (x+z, y), (y+z, x)]
    best_comb = min(pos_comb, key=lambda comb: abs(comb[0]+comb[1]-cost))
    if best_comb[0] in [x, y]:
        return "Alice", "Bob"
    elif best_comb[0] in [x, z]:
        return "Alice", "Charlie"
    else:
        return "Bob", "Charlie"

x = int(input("Alice's money: "))
y = int(input("Bob's money: "))
z = int(input("Charlie's money: "))
cost = int(input("Netflix subscription price: "))
buyers = netflix(x, y, z, cost)
print("{} and {} should buy the Netflix subscription".format(buyers[0], buyers[1]))