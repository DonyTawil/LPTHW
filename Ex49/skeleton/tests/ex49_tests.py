from nose.tools import*
#from Ex48.code import lexicon
from ex49.code import*


def test_init_sentence():
    a=Sentence([None,'subject'],[None,'verb'],[None,'object'],None)
    assert_equal(a.subject, 'subject')
    assert_equal(a.verb, 'verb')
    assert_equal(a.object, 'object')

def test_peek():
    assert_equal(peek([('verb','go')]),'verb')
    assert_equal(peek([]),None)

def test_match():
    assert_equal(match([('verb','go'),('stop','the')],'verb'),('verb','go'))
    assert_equal(match([],'word'),None)
    assert_equal(match([('verb','go')],'stop'),None)

def test_skip():
    fortest=[('stop','the'),('stop','of'),('verb','go')]
    fortest2=[('stop','the'),('stop','of'),('verb','go'),('stop','of')]
    skip(fortest,'stop')
    assert_equal(fortest,[('verb','go')])
    skip(fortest2,'stop')
    assert_equal(fortest2,[('verb','go'),('stop','of')])

def test_pverb():
    fortest=[('stop','at'),('verb','go'),('noun','princess')]
    fortest2=[('stop','at'),('noun','princess')]
    assert_equal(Sentence.parse_verb(fortest),('verb','go'))
    assert_raises(ParseError,Sentence.parse_verb,fortest2)

def test_pobject():
    fortest=[('stop','at'),('noun','princess'),('stop','the')]
    fortest2=[('stop','at'),('direction','up'),('noun','princess')]
    fortest3=[('stop','at'),('verb','go')]
    fortest4=[('stop','at'),('verb','go'),('noun','bear')]
    assert_equal(Sentence.parse_object(fortest),('noun','princess'))
    assert_equal(Sentence.parse_object(fortest2),('direction','up'))
    assert_equal(Sentence.parse_object(fortest4),('noun','bear'))
    assert_raises(ParseError,Sentence.parse_object,fortest3)
        

def test_psub():
    fortest=[('stop','when'),('verb','go'),('direction','up')]
    fortest2=[('stop','when'),('noun','bear')] #assert_raise
    fortest3=[('stop','at'),('verb','go'),('stop','to'),('direction','up')]
    fortest4=[('stop','at'),('verb','go'),('stop','to'),('verb','go')]#assert_raise
    sub=['sub','test']
    f=Sentence.parse_subject(fortest,sub)
    f2=Sentence.parse_subject(fortest3,sub)
    assert_equal([f.subject,f.verb,f.object],['test','go','up'])

    assert_raises(ParseError,Sentence.parse_subject,fortest2,sub)
    assert_equal([f2.subject,f2.verb,f2.object],['test','go','up'])
    assert_raises(ParseError,Sentence.parse_subject,fortest4,sub)

def test_psent():
    fortest=[('stop','at'),('noun','princess'),('verb','go'),('noun','bear')]
    f=Sentence.parse_sentence(fortest)
    assert_equal([f.subject,f.verb,f.object],['princess','go','bear'])
    fortest2=[('stop','at'),('verb','go'),('stop','to'),('noun','princess')]
    f2=Sentence.parse_sentence(fortest2)
    assert_equal([f2.subject,f2.verb,f2.object,f2.num],['player','go','princess',None])
    fortest3=[('stop','at'),('directions','south'),('noun','princess')]
    assert_raises(ParseError,Sentence.parse_sentence,fortest3)
    
def test_pnum():
    fortest=[('stop','the'),('noun','bear'),('verb','go'),('number',19)]
    fortest2=[('stop','the'),('noun','bear'),('verb','go')]
    assert_equal(Sentence.parse_number(fortest),('number',19))
    assert_equal(Sentence.parse_number(fortest2),None)
            
                    
