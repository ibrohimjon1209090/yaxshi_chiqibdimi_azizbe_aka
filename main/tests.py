from django.test import TestCase
for i in range(100,1001):
    if str(i)[::-1]==str(i):
        print(i)