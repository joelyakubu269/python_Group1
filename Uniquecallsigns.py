def  unique_callsigns(log):
    if log == [] :
        return []
    new= set(log)
    new1= list(new)
    new1.sort()
    return new1
print(unique_callsigns([1,2,2,2,3,4]))
