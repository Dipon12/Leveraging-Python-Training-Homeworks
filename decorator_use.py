def dec_htl(func):
    def htl(a,b):
        if a<b:
            a,b=b,a

        if func==div and b==0:
            return "Not Divisible"

        return func(a,b)

    return htl

def dec_nonzero(func):
    def new_div(a,b):
        if b==0:
            return "Not Divisible"
        else:
            return func(a,b)

    return new_div

@dec_htl
@dec_nonzero
def div(a,b):
    return a/b

@dec_htl
def subtract(a,b):
    return a-b


ans1 = div(4,2)
ans2 = subtract(3,8)

print(f"{ans1}    {ans2}")
