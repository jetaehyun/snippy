
class filterManager:

    bannedWords = {}
    textFile = ''
    position = 0

    def __init__(self, textFile):
        self.textFile = textFile
        self.__generateList()


    def __generateList(self):
        try:
            # open and add words to dictionary
            file = open(self.textFile, 'r+')
            words = file.readlines()
            for i in range(len(words)):
                if i == len(words) - 1: self.position = i + 1

                self.bannedWords[words[i].rstrip().lower()] = i + 1

            file.close()

        except OSError as err:
            print("OS error: {0}".format(err))

    def addWord(self, word):
        wordLower = word.lower()

        # check if word exists, if not then add to dictionary and textfile
        if(self.bannedWords.get(wordLower) == None):
            self.position += 1
            self.bannedWords[wordLower] = self.position

            words = open(self.textFile, 'a')
            words.write(wordLower + '\n')
            words.close()

            return True
        else:
            return False

    def removeWord(self, word):

        curr = self.bannedWords.get(word.lower())
        words = []

        if curr == None: 
            return False

        with open(self.textFile, 'r') as file:
            words = file.readlines()
            
        with open(self.textFile, 'w') as file:
            for i in range(len(words)):

                if i == len(words) - 1:
                    self.position = i + 1

                if i == curr - 1:
                    self.bannedWords.pop(word)
                    continue
                else:
                    file.write(words[i])
                    self.bannedWords[words[i].strip('\n')] = i + 1

        return True


    def checkSentence(self, sentence):
        
        # break sentence and check each word
        for word in sentence.split():
            if bannedWords.get(word.lower()) == 1:
                return True

        return False

    def printWords(self):
        print(self.bannedWords)


