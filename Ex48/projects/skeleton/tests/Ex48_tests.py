from nose.tools import*
from Ex48.code import lexicon
lexicon1=lexicon()
def test_directions():    
    assert_equal(lexicon1.scan("north"), [('direction', 'north')])
    result = lexicon1.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon1.scan("go"), [('verbs', 'go')])
    result = lexicon1.scan("go kill eat")
    assert_equal(result, [('verbs', 'go'),
                          ('verbs', 'kill'),
                          ('verbs', 'eat')]) 

                          

def test_stops():
    assert_equal(lexicon1.scan("the"), [('stop', 'the')])
    result = lexicon1.scan("the in of from at it")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop','from'),
                          ('stop','at'),
                          ('stop','it'),
                          ])

def test_nouns():
    assert_equal(lexicon1.scan("bear"), [('nouns', 'bear')])
    result = lexicon1.scan("bear princess cabinet door")
    assert_equal(result, [('nouns', 'bear'),
                          ('nouns', 'princess')
                          ,('nouns','cabinet')
                          ,('nouns','door')])

def test_numbers():
    assert_equal(lexicon1.scan("1234"), [('numbers', 1234)])
    result = lexicon1.scan("3 91234")
    assert_equal(result, [('numbers', 3),
                          ('numbers', 91234)])

def test_errors():
    assert_equal(lexicon1.scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result =lexicon1.scan("bear IAS princess")
    assert_equal(result, [('nouns', 'bear'),
                           ('error', 'ias'),
                           ('nouns', 'princess')])
                                                     
                                                                                  
