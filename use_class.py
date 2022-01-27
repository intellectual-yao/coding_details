class Man:
    def __init__(self, name):	#构造函数
        self.name = name
        print('Initialized!')

    def hello(self):			#方法1
        print('hello' + self.name + '!')

    def goodbye(self):			#方法2
        print('Good-bye' + self.name + '!')
        
m = Man('TOM')		#传入参数
m.hello()			#调用方法
m.goodbye()			#调用方法



#running result:

#Initialized!
#helloTOM!
#Good-byeTOM!

#Process finished with exit code 0
