class square:

    def __init__(self, x, y, ID):
        self.x = x
        self.y = y    
        self.possibleValues = [1,2,3,4,5,6,7,8,9]
        self.hasValue = False
        self.value = 0
        self.ID = ID

    def setPossibleValues(self, possibleValues):
        self.possibleValues = possibleValues

    def setXBlock(self, xblocks):
        xblock = [block for block in xblocks if block.id == self.x]       
        self.xblock = xblock[0]

    def setYBlock(self, yblocks):
        yblock = [block for block in yblocks if block.id == self.y]        
        self.yblock = yblock[0]

    def setSquareBlock(self, squareBlocks):       
        for block in squareBlocks:
            if  any(temp for temp in block.squares if temp.x == self.x and temp.y == self.y):
                self.squareBlock = block
    
    def setEntry(self, entry):
        self.entry = entry        
        
        if entry.get() or self.hasValue:
            if entry.get(): 
                self.hasValue = True
                self.value = int(entry.get())
        
            if self.hasValue:
                self.setEntryValue()

    def setEntryValue(self):
        self.entry.delete(0)
        self.entry.insert(0, str(self.value))

    def setValue(self, value):
        self.value = value
        self.possibleValues = []
        self.hasValue = True

    def updateBlocks(self):
        self.xblock.setPossibleValues()
        self.yblock.setPossibleValues()
        self.squareBlock.setPossibleValues()

    def solve(self):

        if(self.hasValue):
            print(str(self.ID) + 'O MEU VALOR É ' + str(self.value) )
            self.possibleValues = []
            return
        
        inter = set(self.xblock.possibleValues).intersection(self.yblock.possibleValues, self.squareBlock.possibleValues)
        inter = list(inter)
        
        if(len(inter) == 1):
            self.setValue(inter[0])
        
        self.setPossibleValues(inter)
        self.updateBlocks()
        
    
