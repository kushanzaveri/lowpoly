
class Wow:
    def __init__(self, num):
        self.num = num

    def do(self):
        try:
            from .tools.wew import foo
            print (foo())
            import sys
            print (sys.path)
        except:
            import sys
            print (sys.path)
            print ("error!!")
        