def classify_triangle(a, b, c):
    """ Function that classifies triangle based on given values """
    type = ""
    # All sides are equal -> Equilateral triangle
    if a == b and a == c and b == c:
        type = "Given triangle is a Equilateral triangle"
    # Any two sides are equal -> Isosceles triangle
    elif a == b or a == c or b == c:
        type = "Given triangle is a Isosceles triangle"
    # No equal sides -> Scalene triangle
    else:
        type = "Given triangle is a Scalene triangle"
    # Checking for right angle triangle
    if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b):
        type += " and right angle triangle"
    else:
        type += " and not a right angle triangle"
    return type
