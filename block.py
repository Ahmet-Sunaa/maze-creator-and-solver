class block:
    def __init__(self, definitly, changeable, value, cantreturn=0,blocksize=1,blur=0,blockcount=0,visited=0):
        self.definitly = definitly
        self.changeable = changeable
        self.value = value
        self.cantreturn = cantreturn
        self.blocksize = blocksize
        self.blur = blur
        self.blockcount = blockcount
        self.visited = visited

