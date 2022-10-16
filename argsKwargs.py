
def kwrgsExample(**kw):
    for ch in kw.values():
        print(ch)
dict={'a':'A','b':'2','c':'3'}
kwrgsExample(**dict)