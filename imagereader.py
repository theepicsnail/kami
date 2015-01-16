from PIL import Image
from StringIO import StringIO
from urllib import urlopen

im = Image.open("img.jpg")
width, height =  im.size
width = 10 * height/16

cell_w = width / 10
cell_h = height/ 16
#im.crop((0,0,width,height)).save('crop.png')

board = [[0]*10 for _ in xrange(16)]
for row in xrange(16):
  for col in xrange(10):
    r, g, b = 0,0,0
    cell_x = cell_w * col
    cell_y = cell_h * row
    err = 0
    count = 0
    for dx in xrange(cell_w):
        for dy in xrange(cell_h):
            pxl = im.getpixel((cell_x+dx, cell_y+dy))
            if sum(pxl) > 700:
                err += 1
                continue
            if sum(pxl) < 50:
                err += 1
                count -=1
                continue
            r += pxl[0]
            g += pxl[1]
            b += pxl[2]
            count += 1
    K=50
    r -= K*count/float(1+.01*((row-2)**2 + (col-2)**2))
    g -= K*count/float(1+.01*((row-2)**2 + (col-2)**2))
    b -= K*count/float(1+.01*((row-2)**2 + (col-2)**2))

    r /= count
    g /= count
    b /= count

    if err > 2000:
        print err
        r = 255
        g = 255
        b = 255

    #if white > .05 * cell_w * cell_h:
    #    r = 255
    #    g = 255
    #    b = 255
    #print int(white*100/cell_w/cell_h),
    board[row][col] =tuple(map(int, (r,g,b)))
  print ""

names   = ["k",        " ",           "w",             "y",          "r"]
#buckets = [(40,40,40), (255,255,255), (170, 125, 100), (180,120,50), (190,50,40)]
names   = ["k",        " ",           "c",             "o",          "r"]
buckets = [(20,40,55), (255,255,255), (97, 149, 110),  (200, 90, 40), (145, 15, 50)]
def quantize(color):
    def dist((c1,c2)):
        return sum(map(lambda (x,y):abs(x-y), zip(c1,c2)))
    d, c = sorted(zip(map(dist,[(b, color) for b in buckets]), buckets))[0]
    print "(%3s,%1d)"%(d,buckets.index(c)),
    return c
for row in xrange(15,-1,-1):
    for col in xrange(0,10):
        if sum(board[row-1][col]) == 255*3:
            board[row][col] = (255,255,255)
        print "%4s%4s%4s" % board[row][col],
        board[row][col] = quantize(board[row][col])
    print

import sys
out = Image.new("RGB", (10,16), "white")
for row in xrange(16):
  sys.stdout.write('    "')
  for col in xrange(10):
    out.putpixel((col,row),board[row][col])
    sys.stdout.write(names[buckets.index(board[row][col])])
  print '",'
out.resize((100,160)).save('crop.png')
