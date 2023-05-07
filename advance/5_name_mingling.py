class test:
    a = 10
    _b = 20    # single underscore variable can be accessed like [print(test._b)]
    __c = 30   # doble underscore variable ---can not be accessed using double __ [print(test.__c) ]
print(test.a)
print(test._b)
print(test._test__c)

