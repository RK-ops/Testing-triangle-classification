#Importing the unittest, automated test platform library.
import unittest   

#Functions for classifying different types of triangles.
def classify_triangle(a,b,c):
    
    if a == b and b == c and a==c:
        print("The given Triangle is a Equilateral triangle")
        type = 'Equilateral'
    elif a==b or b==c or a==c:
        print("The given Triangle is a Isosceles triangle")
        type = 'Isosceles'
    else:
        print("The given Triangle is a Scalene triangle")
        type = 'Scalene'

    return type

#Function for right angeled triangle.
def right_angle(a, b, c):
    
    if (a * a) + (b * b) == (c * c):
        print("The given Triangle is a Right angled Triangle")
        type = 'Right'

    return type

def main():

    #User input for different sides of the triangle.
    print("\nInput the lengths of sides of the Triangle: ")

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

class TestTriangles(unittest.TestCase):

    #Checking the test cases for a right angeled triangle.
    def testSet1(self): 
        self.assertEqual(right_angle(3, 4, 5),'Right')
        self.assertEqual(right_angle(8,15,17),'Right')
        self.assertEqual(right_angle(9,12,15),'Right')
        #self.assertEqual(right_angle(7,8,9),'Right')
        
    #Checking the test cases for different types of triangles.
    def testSet2(self): 

        self.assertEqual(classify_triangle(12,12,12),'Equilateral')
        self.assertEqual(classify_triangle(5,7,7),'Isosceles')
        self.assertEqual(classify_triangle(90,94,85),'Scalene')
        self.assertEqual(classify_triangle(6,9,9),'Isosceles')
        self.assertEqual(classify_triangle(1,2,3),'Scalene')
        self.assertEqual(classify_triangle(10,15,30),'Scalene')
        self.assertNotEqual(classify_triangle(19,9,9),'Equilateral')
        self.assertNotEqual(classify_triangle(10,10,10),'Isosceles')

#Invoking the function calls from the main function.
if __name__ == '__main__':

    classify_triangle
    right_angle
    unittest.main(exit=False,verbosity=2)
