class Test:
    one = 'First one'
    sec = 'Second One'
    thi = 'Third One'

run = Test()
print(run.one, run.sec, run.thi)
# First one Second One Third One

delattr(Test, 'thi') 
# OR del Test.thi 

print(run.one)
# First one
print(run.sec)
# Second one
print(run.thi)
# Traceback (most recent call last):
#   File "delattr.py", line 12, in <module>
    # print(run.thi)
# AttributeError: 'Test' object has no attribute 'thi'