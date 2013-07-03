from nose.tools import*
from gothonweb.map02 import*

def test_Player():
    assert_equal(Player.inventory,{})
    assert_equal((Player.health),(100))
    Player.reduce_health(100)
    assert_equal(Player.health,0)
    assert_equal(Player.room.name,'death room')

def test_Enemy():
    dony=Enemy('don',100,100)
    assert_equal([dony.name,dony.health,dony.attack],['don',100,100])

    
def test_RoomWar_enemies():
    #test the basic stuff
    test_room=RoomWar('test room','yellow')
    test_room2=RoomWar('test room2','yellow')
    #assert the enemies
    test_room.add_enemy('don2',100,100)
    its_stuff=test_room.enemies['don2']
    assert_equal([its_stuff.name,its_stuff.health,its_stuff.attack],['don2',100,100])

def test_RoomWar():
    #test the basic stuff
    test_room=RoomWar('test room','yellow')
    test_room2=RoomWar('test room2','yellow')
    #assert the paths
    test_room.add_paths({test_room2.name:test_room2})
    assert_equal(test_room.paths,{'yellow':test_room2})
    test_room.go('yellow')
    room=Player.room
    assert_equal(room.name,test_room2.name)
    #assert the objects
    test_room.add_objects({'mask':'mask wich allows you to breathe in mars'})
    assert_equal(test_room.objects,{'mask':'mask wich allows you to breathe in mars'})
    assert_equal(test_room.take_objects('mask'),('mask wich allows you to breathe in mars','mask'))
    ##Testing roomwar go
    a='objects for test'
    test_room.add_objects({'objects for test':'testing thing using whatever'})
    assert a in test_room.objects,'expected %s in test_room.objects'%a
    test_room.add_paths({'take the test':test_room.take_objects('objects for test')})
    #print(test_room.paths)
    #assert test_room.paths['objects for test']=='testing thing using whatever'
  
    test_room.go('take the test')    
    assert a not in test_room.objects,'did not expect %s in test_room.objects'%a
    assert_equal(test_room.description,'testing thing using whatever')
    
def test_kill_enemy():
    test_room=RoomWar('test room','yellow')
    test_room.add_enemy('Motherload',100,1)
    test_room.add_paths({'shoot Motherload':test_room.enemies['Motherload'].attack_enemy()})
    test_room.go('shoot Motherload')
    print(test_room.paths.get('shoot Motherload',None))
    print(test_room.enemies)
    assert_equal(test_room.enemies['Motherload'].health,90)    


def test_the_enemies_attack():
    test_room=RoomWar('test room','yellow')
    Player.room=test_room
    test_room2=RoomWar('test room2','hello')
    test_room.add_paths({'go to room2':test_room2})
    test_room.add_enemy('Motherload',100,1)

    test_room.enemies['Motherload'].enemy_attack_player()
    assert Player.health < 100,"Player was not attacked" 
    test_room.go('go to room2')
    assert 'there are still enemies in the room can\'t do that!!' in Player.room.description 

def test_enemies_turn():
    test_room=RoomWar('test room','yellow')
    test_room.add_enemy('Motherload',100,1)
    test_room.add_objects({'mask':'whatever'})
    test_room.add_paths({'take the mask':test_room.take_objects('mask')})
    Player.room=test_room
    Player.room.go('take the mask')
    assert Player.health <100
    #assert "the enemies have attacked you" in Player.room.description,"did not find keyphrase in %s"%Player.room.description

def test_description():
    test_room=RoomWar('test room','yellow')
    test_room.add_objects({'nothing':'nothing'})
    Player.room=test_room
    assert_equal(test_room.description,'test room')
    test_room2=RoomWar('test room2','bellow')
    test_room.add_paths({'player go room2':test_room2})
    test_room.go('player go room2')
    assert_equal(test_room.description,'test room You still need to use some objects in the area!!')
    test_room.go('blahb')
    assert_equal(test_room.description,'test room')    

       
