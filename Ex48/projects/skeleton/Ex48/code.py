
class lexicon(object):
    def __init__(self):
        self.words=None
        self.directions=["north",'east','west','south','up','down','left','right']
        self.nouns=["bear","princess","cabinet","door"]
        self.verbs=["go","stop","kill",'eat']
        self.stop=["the","in",'from','at','it','of']
        self.keywords=['direction','verbs','nouns','stop']#also numbers is a keyword
        self.holder={'direction':self.directions,'nouns':self.nouns,'verbs':self.verbs,"stop":self.stop}#Has all of type_words variants to search in
    
    def scan(self,stuff): #stuff is/are the words to study
        stuff=stuff.lower()
        self.giver={}#dict to get tuples of word 1, 2,...
        self.sentence=[]
        self.words=stuff.split(' ')
        self.l=['1','2','3','4','5','6','7','8','9']
        for i in range(0,len(self.words)):
            self.giver[i]=None  #To reset what self.giver has in it
            for a in self.keywords: #To test each word on all keywords
                if (self.words[i] in self.holder[a]):
                    self.giver[i]=(a,self.words[i])
                    print(self.giver[i])
                    break
            if (self.giver[i] == None):
                for c in self.words[i]:
                    if c in self.l:
                        self.words[i]=int(self.words[i])
                        self.giver[i]=('numbers',self.words[i])
                        break
                    else:
                        self.giver[i]=('error',self.words[i])    
                        break
#                try:
#                    int(self.words[i])
#                    self.words[i]=int(self.words[i])
#                    self.giver[i]=('numbers',self.words[i])
#                    print(self.giver[i])
#                    continue
#                except ValueError:        
#                    self.giver[i]=('error',self.words[i])
#                    print(self.giver[i])
#                    continue    

        for i in range(0,len(self.words)):
            self.sentence.append(self.giver[i])
        print(self.sentence)
        return (self.sentence)                        
            




