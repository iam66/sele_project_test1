from time import ctime,sleep
#说
def talk():
	print('Strat talk:%s'%ctime())
	sleep(2)
#写
def write():
	print('Start write:%s'%ctime())
	sleep(3)

if __name__=='__main__':
	talk()
	write()
	print('All end! %s'%ctime())