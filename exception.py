''' FileNotFoundError
try:
    fileName=input('Please input fileName:')
    open('%s.mtb'%fileName)
except FileNotFoundError:
    print('%s.mtb file not found'%fileName)
'''

'''try:
# stu='Jack'
    print(stu)
except NameError:
    print('stu not defined !')
'''

try:
# stu='Jack'
    print(stu)
except BaseException:
    print('stu not defined !')
