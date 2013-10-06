from SimpleCV import Image, Color

class Food:
  APPLE = 1
  BANANA = 2
  REDBULL = 3

def thirds(image):
  first = image.crop(image.width*0/3, 0, image.width/3, image.height)
  second = image.crop(image.width*1/3, 0, image.width/3, image.height)
  third = image.crop(image.width*2/3, 0, image.width/3, image.height)
  return first, second, third

def extract(empty, full):
  mask = (full-empty).hueDistance(color=Color.BLACK).binarize()
  return full.crop((full-mask.invert()).getPIL().getbbox())

def fruit_color(empty, full):
  extracted = extract(empty, full)
  if extracted:
    return extracted.meanColor()
  return False

def pct_diff(a, b):
  return (a-b)/((a+b)*2)*100

def is_apple(color):
  if color:
    b, g, r = color
    print color
    print pct_diff(b, g)
    print pct_diff((b+g)/1.2, r)
    print ""
  else:
    print "no color"
  return True

def scan_image(empty, full):
  empty = Image(empty)
  full = Image(full)

  e1, e2, e3 = thirds(empty)
  b1, b2, b3 = thirds(full)

  colors = [fruit_color(e1, b1),
            fruit_color(e2, b2),
            fruit_color(e3, b3)]

  fruit = []

  for color in colors:
    if is_apple(color):
      fruit.append(Food.APPLE)

  return fruit

assert(Food.APPLE not in scan_image("empty.jpg", "empty.jpg"))
assert(Food.APPLE not in scan_image("empty.jpg", "banana.jpg"))
assert(Food.APPLE in scan_image("empty.jpg", "appleredbull.jpg"))
assert(Food.APPLE not in scan_image("empty.jpg", "redbull.jpg"))
assert(Food.APPLE not in scan_image("empty.jpg", "redbullpepsi.jpg"))
assert(Food.APPLE in scan_image("empty.jpg", "redbullpepsiapple.jpg"))

assert(scan_image("empty.jpg", "empty.jpg") == [])
assert(scan_image("empty.jpg", "banana.jpg") == [Food.BANANA])
assert(scan_image("empty.jpg", "appleredbull.jpg") == [Food.APPLE, Food.REDBULL])
assert(scan_image("empty.jpg", "redbull.jpg") == [Food.REDBULL])
assert(scan_image("empty.jpg", "redbullpepsi.jpg") == [Food.REDBULL, Food.PEPSI])
assert(scan_image("empty.jpg", "redbullpepsiapple.jpg") == [Food.REDBULL, Food.PEPSI, Food.APPLE])
