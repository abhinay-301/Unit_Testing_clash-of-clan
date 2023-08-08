import unittest
import king
import village
import buildings
import map 
import points as pt

class TestKing(unittest.TestCase):

    def setUp(self):
        self.kings = king.spawnKing([6,9])
        self.v = village.createVillage(1)
        self.map = self.v.map
        self.hut = buildings.Hut((6,11),self.v)

#  check kings attribute does not change
    def test_attribute(self):
        self.kings.speed = 1
        self.kings.health = 100
        self.kings.max_health = 100
        self.kings.attack = 30
        self.kings.AoE = 10
        self.kings.facing = 'up'
        self.kings.attack_radius = 3
        self.kings.alive = True
        self.position = [6,9]
        self.kings.attack_target(self.hut, self.kings.attack)
        self.assertEqual(self.kings.speed,1)
        self.assertEqual(self.kings.health,100)
        self.assertEqual(self.kings.max_health,100)
        self.assertEqual(self.kings.attack,30)
        self.assertEqual(self.kings.AoE,10)
        self.assertEqual(self.kings.facing,'up')
        self.assertEqual(self.kings.attack_radius,3)
        self.assertEqual(self.kings.alive,True)
        self.assertEqual(self.kings.position,[6,9])


    def test_attack_target(self):
        # Test that the target's health is reduced by the attack value
        health = self.hut.health
        self.kings.attack_target(self.hut, self.kings.attack)
        self.assertEqual(self.hut.health, health-self.kings.attack) 

    def test_attack_target_dead_target(self):
        # Test that the target's health remains at 0 after it has been destroyed
        self.hut.destroyed = True
        self.kings.attack_target(self.hut, self.kings.attack)
        self.assertEqual(self.hut.health, 10)


    # Test that the method returns immediately if the king is dead
    def test_health_dead(self):
        health = self.hut.health
        self.kings.alive = False
        self.kings.attack_target(self.hut, self.kings.attack)
        self.assertEqual(self.hut.health, health)
        self.assertEqual(self.hut.destroyed, False)
    

    def test_negative_attack(self):
        # Test that the method works correctly when given a negative attack value
        health = self.hut.health
        self.kings.attack_target(self.hut, -5)
        self.assertEqual(self.hut.health,health+5)

    def test_zero_health(self):
        # Test that the target is destroyed when its health reaches 0 or less than 0
        self.hut.health = self.kings.attack - 5
        self.kings.attack_target(self.hut, self.kings.attack)
        self.assertEqual(self.hut.destroyed, True)
        self.assertEqual(self.hut.health, 0)

    # check that target is not destroyed when health is grater than 0
    def test_target_not_destroyed(self):
        self.hut.health = 50  
        self.kings.attack = 10
        self.kings.attack_target(self.hut,self.kings.attack)
        self.assertEqual(self.hut.destroyed,False)




# run the test
# unittest.main()
test_cases = unittest.TestLoader().loadTestsFromTestCase(TestKing)
runner = unittest.TextTestRunner().run(test_cases)
if runner.wasSuccessful():
    f = open("output_bonus.txt","w")
    f.write("TRUE")
else:
    f = open("output_bonus.txt","w")
    f.write("FALSE")


