import math
def calculate_area(shape, dimension1, dimension2=0):
    shape = shape.lower()
    if shape == "circle":
        return math.pi * dimension1 ** 2
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

 #Test cases   
circle_area = calculate_area("circle",7)
rectangle_area = calculate_area("rectangle", 5, 6)
triangle_area = calculate_area("triangle", 4, 3)
invalid_shape =calculate_area("hexagon", 6)

print(f"Area of circle: {circle_area}")
print(f"Area of rectangle: {rectangle_area}")       
print(f"Area of triangle: {triangle_area}")
print(f"Invalid shape test: {invalid_shape}")
