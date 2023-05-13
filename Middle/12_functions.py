def sum_range(start, end):
    if start > end:
        start, end = end, start
start=int(input("Start: "))
end=int(input("End: "))
result = sum(range(start, end+1))
print("sum= ", result)