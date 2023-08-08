import unittest
import king
import village
# import map 
import points as pt

class TestKing(unittest.TestCase):
    
    def setUp(self):
        self.kings = king.spawnKing([6,6])
        self.v = village.createVillage(1)
        self.map = self.v.map

# #  check kings attribute does not change on running funtion
    def test_attribute(self):
        self.kings.speed = 1
        self.kings.health = 100
        self.kings.max_health = 100
        self.kings.attack = 30
        self.kings.AoE = 10
        self.kings.attack_radius = 3
        self.kings.alive = True
        self.kings.move("up", self.v)
        self.assertEqual(self.kings.speed,1)
        self.assertEqual(self.kings.health,100)
        self.assertEqual(self.kings.max_health,100)
        self.assertEqual(self.kings.attack,30)
        self.assertEqual(self.kings.AoE,10)
        self.assertEqual(self.kings.attack_radius,3)
        self.assertEqual(self.kings.alive,True)


# checking position after movement
    def test_normal_up(self):
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.position,[5,6])

    def test_normal_down(self):
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.position,[7,6])
    
    def test_normal_left(self):
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.position,[6,5])

    def test_normal_right(self):
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.position,[6,7])
        
# checking face after movement
    def test_face_up(self):
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.facing,"up")

    def test_face_down(self):
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.facing,"down")
    
    def test_face_left(self):
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.facing,"left")

    def test_face_right(self):
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.facing,"right")

# King is not alive
    def test_king_alive(self):
        self.kings.alive = False
        self.kings.move('up', self.v)
        self.assertEqual(self.kings.position, [6, 6])

# function does not move the King when it reaches a non-blank and non-spawn tile
    def test_blank_down(self):
        self.kings.position = [5,11]
        self.kings.move('down', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [5, 11])

    def test_blank_up(self):
        self.kings.position = [7,11]
        self.kings.move('up', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [7, 11])

    def test_blank_left(self):
        self.kings.position = [6,12]
        self.kings.move('left', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [6, 12])

    def test_blank_right(self):
        self.kings.position = [6,10]
        self.kings.move('right', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [6, 10])

# function correctly handles the case when the King tries to move out of bounds in the 'up' direction.
    def test_boundry_up(self):
        self.kings.position = [0,5]
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.position,[0,5])

    def test_boundry_down(self):
        self.kings.position = [17,5]
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.position,[17,5])
    
    def test_boundry_left(self):
        self.kings.position = [5,0]
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.position,[5,0])

    def test_boundry_right(self):
        self.kings.position = [5,37]
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.position,[5,37])

#   # checking face after movement at boundry condition
    def test_boundry_face_up(self):
        self.kings.position = [0,5]
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.facing,"up")

    def test_boundry_face_down(self):
        self.kings.position = [17,5]
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.facing,"down")
    
    def test_boundry_face_left(self):
        self.kings.position = [5,0]
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.facing,"left")

    def test_boundry_face_right(self):
        self.kings.position = [5,37]
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.facing,"right")



# ------------------------------------------------------------------------------

class TestKing_speed(unittest.TestCase):
    
    def setUp(self):
        self.kings = king.spawnKing([6,6])
        self.v = village.createVillage(1)
        self.map = self.v.map
        self.kings.speed = 2
# checking position after movement
    def test_normal_up(self):
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.position,[4,6])

    def test_normal_down(self):
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.position,[8,6])
    
    def test_normal_left(self):
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.position,[6,4])

    def test_normal_right(self):
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.position,[6,8])
        
# checking face after movement
    def test_face_up(self):
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.facing,"up")

    def test_face_down(self):
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.facing,"down")
    
    def test_face_left(self):
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.facing,"left")

    def test_face_right(self):
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.facing,"right")

# King is not alive
    def test_king_alive(self):
        self.kings.alive = False
        self.kings.move('up', self.v)
        self.assertEqual(self.kings.position, [6, 6])

# function does not move the King when it reaches a non-blank and non-spawn tile
    def test_blank_down(self):
        self.kings.position = [4,11]
        self.kings.move('down', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [5, 11])

    def test_blank_up(self):
        self.kings.position = [8,11]
        self.kings.move('up', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [8, 11])

    def test_blank_left(self):
        self.kings.position = [6,13]
        self.kings.move('left', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [6, 13])

    def test_blank_right(self):
        self.kings.position = [6,9]
        self.kings.move('right', self.v)  # (6,11)position of hut
        self.assertEqual(self.kings.position, [6, 10])

# function correctly handles the case when the King tries to move out of bounds in the 'up' direction.
    def test_boundry_up(self):
        self.kings.position = [1,5]
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.position,[0,5])

    def test_boundry_down(self):
        self.kings.position = [16,5]
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.position,[17,5])
    
    def test_boundry_left(self):
        self.kings.position = [5,1]
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.position,[5,0])

    def test_boundry_right(self):
        self.kings.position = [5,35]
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.position,[5,35])

#   # checking face after movement at boundry condition
    def test_boundry_face_up(self):
        self.kings.position = [1,5]
        self.kings.move("up",self.v)
        self.assertEqual(self.kings.facing,"up")

    def test_boundry_face_down(self):
        self.kings.position = [16,5]
        self.kings.move("down",self.v)
        self.assertEqual(self.kings.facing,"down")
    
    def test_boundry_face_left(self):
        self.kings.position = [5,1]
        self.kings.move("left",self.v)
        self.assertEqual(self.kings.facing,"left")

    def test_boundry_face_right(self):
        self.kings.position = [5,36]
        self.kings.move("right",self.v)
        self.assertEqual(self.kings.facing,"right")


# -------------------------------------------------------------------------------
    #     # Testing invalid inputs
    #     self.assertRaises(ValueError, King.move, "invalid_direction", 1)
    #     self.assertRaises(ValueError, King.move, "up", -1)





# run the test
# unittest.main()
# test_cases = unittest.TestLoader().loadTestsFromTestCase(TestKing)

class_test = unittest.TestSuite()
class_test.addTest(unittest.makeSuite(TestKing))
class_test.addTest(unittest.makeSuite(TestKing_speed))


runner = unittest.TextTestRunner().run(class_test)




if runner.wasSuccessful():
    f = open("output.txt","w")
    f.write("TRUE")
else:
    f = open("output.txt","w")
    f.write("FALSE")


