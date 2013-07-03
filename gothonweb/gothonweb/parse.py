class ParseError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object,num):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]
        if num:
            self.num= num[1]
        else:
            self.num=None        
        
    @staticmethod
    def parse_number(word_list):
        skip(word_list,'stop')
        word_list2=[]
        word_list2.extend(word_list)

        print(len(word_list))
        for i in range(0,len(word_list)):
            if peek(word_list2) == 'number':
                word_list.pop(i)
                return match(word_list2,'number')
            else:
                word_list2.pop(0)
                print(word_list2) 
                print(word_list)
        return None        
                
    @staticmethod 
    def parse_verb(word_list):
        skip(word_list,'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
             raise ParseError("Expected a verb next.")

    @staticmethod
    def parse_object(word_list):
        skip(word_list, 'stop')
        next = peek(word_list)
        while (len(word_list)>1):
        
            next = peek(word_list)
            print(next)
            if((next!='noun') and (next!='direction')):
                skip(word_list, next)
                next = peek(word_list)
            else:
                break

        if next == 'noun':
            return match(word_list, 'noun')
        if next == 'direction':
            return match(word_list, 'direction')
        else:
            
            raise ParseError("Expected a noun or direction next not %s."%next)
    @staticmethod
    def parse_subject(word_list, subj):
        num=None
        num = Sentence.parse_number(word_list)
        verb = Sentence.parse_verb(word_list)
        obj = Sentence.parse_object(word_list)

        return Sentence(subj, verb, obj,num)

    @staticmethod
    def parse_sentence(word_list):
        skip(word_list, 'stop')

        start = peek(word_list)

        if start == 'noun':
            subj = match(word_list, 'noun')
            return Sentence.parse_subject(word_list, subj)
        elif start == 'verb':
            # assume the subject is the player then
            return Sentence.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParseError("Must start with subject, object, or verb not: %s"%start)        


def peek(word_list): ##Function that sees the type of first word
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None          

def match(word_list, expecting):#Takes the word at position 0 if it is of correct type
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):#deletes all the word of the given word type
    while peek(word_list) == word_type:
        match(word_list, word_type)
    
              
              
                                                
