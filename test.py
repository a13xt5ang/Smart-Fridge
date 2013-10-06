from SimpleCV import Image, Color

class Food:
  APPLE = 1
  BANANA = 2
  REDBULL = 3

def thirds(image):
  first = image.crop(empty.width*0/3, 0, image.width/3, image.height)
  second = image.crop(empty.width*1/3, 0, image.width/3, image.height)
  third = image.crop(empty.width*2/3, 0, image.width/3, image.height)
  return first, second, third

empty = Image("empty.jpg")
full = Image("appleredbull.jpg")
e1, e2, e3 = thirds(empty)
b1, b2, b3 = thirds(full)

(b2).show()
raw_input()
(e2).show()
raw_input()
(b2-e2).show()
raw_input()

assert(scan_image("empty.jpg") == [])
assert(scan_image("banana.jpg") == [Food.BANANA])
assert(scan_image("appleredbull.jpg") == [Food.APPLE, Food.REDBULL])
assert(scan_image("redbull.jpg") == [Food.REDBULL])
assert(scan_image("redbullpepsi.jpg") == [Food.REDBULL, Food.PEPSI])
assert(scan_image("redbullpepsiapple.jpg") == [Food.REDBULL, Food.PEPSI, Food.APPLE])
