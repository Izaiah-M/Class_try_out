Array = ['a',['b',['c',['d']],'e'],'f']
def recurse(Array):
    if not(bool(Array)):
        return Array
    if isinstance(Array[0], list):
        return recurse(*Array[:1])+recurse(Array[1:])
    return Array[:1] + recurse(Array[1:])
print(recurse(Array))
