# Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

def paint_fill(image, x, y, new_color):
    if image[x][y] == new_color:
        return # Might not be necessary anymore
    original_color = image[x][y]
    image[x][y] = new_color
    x_max = len(image)-1
    y_max = len(image[0])-1
    if x < x_max and image[x+1][y] == original_color:
        paint_fill(image, x+1, y, new_color)
    if y < y_max and image[x][y+1] == original_color:
        paint_fill(image, x, y+1, new_color)
    if 0 < x and image[x-1][y] == original_color:
        paint_fill(image, x-1, y, new_color)
    if 0 < y and image[x][y-1] == original_color:
        paint_fill(image, x, y-1, new_color)

def image_to_str(image):
    result = ""
    for i in range(len(image)):
        for j in range(len(image[0])):
            result += str(image[i][j])
        result += "\n"
    return result

def print_image(image):
    print(image_to_str(image))

if __name__ == '__main__':
    image = [
        [0,0,0,0,0],
        [0,1,1,1,1],
        [0,0,0,1,1],
        [0,1,0,0,0],
        [0,1,0,1,1],
        [0,1,0,0,0],
    ]
    paint_fill(image, 0, 0, 2)
    print("Image :")
    print_image(image)
    assert image_to_str(image) == """22222
21111
22211
21222
21211
21222
"""
    paint_fill(image, 1, 1, 3)
    print("Image :")
    print_image(image)
    assert image_to_str(image) == """22222
23333
22233
21222
21211
21222
"""
    paint_fill(image, 1, 1, 3)
    print("Image :")
    print_image(image)
    assert image_to_str(image) == """22222
23333
22233
21222
21211
21222
"""
