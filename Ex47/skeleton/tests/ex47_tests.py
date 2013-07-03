from nose.tools import*
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. there's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    assert_equal(gold.e, False)
    
def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "test room in the north.")
    south = Room("south", "test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():

    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")



    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})


    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_add_enemy():
    a=Room('test','Nothing to see here')
    b=Room('NO!','Just No')
    a.add_paths({"no": b})
    a.add_enemy("there is a testenemy here")
    c=a.description
    assert_equal(c,"""Nothing to see here\nthere is a testenemy here""")
    assert_equal(a.go(b),"can't go there")

def test_Enemy():
    a=Room('test','no')
    a.add_enemy("testenemy")
    assert_equal(a.enemy.health,100)
    a.enemy.attack()
    assert(a.enemy.health<100)
                  
