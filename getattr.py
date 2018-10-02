class Method:
    first = 1
    second = 'text'
    third = 'maybe a string'


print(getattr(Method, 'first'))
# 1
print(Method.second)
# text