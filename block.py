class block:

    def __init__(self, id, squares):
        self.id = id
        self.squares = squares
        self.possibleValues = self.setPossibleValues()

    def setPossibleValues(self):
        possibleValues = [1,2,3,4,5,6,7,8,9]
        
        for square in self.squares:
            if(square.hasValue and any(value for value in possibleValues if value == square.value)):
                possibleValues.remove(square.value)
        
        self.possibleValues = possibleValues
        return possibleValues

        