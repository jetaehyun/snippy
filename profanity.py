
class filterManager:
    
    bannedWords = {}
    textFile = ''

    def __init__(self, textFile):
        self.textFile = textFile
        self.__generateList()


    def __generateList(self):
        try:
            # open and add words to dictionary
            words = open(self.textFile, 'r').readlines()
            for i in words:
                self.bannedWords[i.rstrip()] = 1

        except OSError as err:
            print("OS error: {0}".format(err))
    
    def addWord(self, word):

        # check if word exists, if not then add to dictionary and textfile
        if(self.bannedWords.get(word) == None):
            self.bannedWords[word] = 1
            
            words = open(self.textFile, 'a')
            words.write(word + '\n')
            words.close()

            return True
        else:
            return False

    def printWords(self):
        print(self.bannedWords)


