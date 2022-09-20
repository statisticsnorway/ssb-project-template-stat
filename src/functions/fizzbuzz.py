def fizz(x:int) -> str:
    if x%3 == 0:
        return "fizz"
    return ""

def buzz(x:int) -> str:
    if x%5 == 0:
        return "buzz"
    return ""
    
def fizzbuzz(x:list) -> None:
    for y in x:
        r = ""
        r = fizz(y) + buzz(y)
        if not r:
            r = y
        print(r)