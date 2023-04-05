S=input("Your text: ")
w=S.split()
uw = {} 
for word in w:
    if word not in uw:
         uw[word] = 1 
    else: 
        uw[word] += 1 
the_biggest_uw = max(uw, key=uw.get) 
lw = max(w, key=len) 
print("The most common word: ", the_biggest_uw) 
print("The longies word: ", lw)