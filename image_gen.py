import Image, ImageDraw

def round_rect(draw, (x,y,x2,y2), r=0, **kwargs):
    r2 = r*2
    if r != 0:
        draw.ellipse((    x,    y, x+r2, y+r2), **kwargs)
        draw.ellipse((x2-r2,    y,   x2, y+r2), **kwargs)
        draw.ellipse((x2-r2,y2-r2,   x2,   y2), **kwargs)
        draw.ellipse((    x,y2-r2, x+r2,   y2), **kwargs)
        draw.rectangle((x+r, y, x2-r, y2), **kwargs)
        draw.rectangle((x, y+r, x2, y2-r), **kwargs)
    else:
        draw.rectangle((x, y, x2, y2), **kwargs)

width = 400
height = 800

img = Image.new("RGBA", (width, height))

draw = ImageDraw.Draw(img)
round_rect(draw, (0,0,100,100), fill=(255,0,0))
round_rect(draw, (0,0,100,100), 50, fill=(255,128,128))
#draw.ellipse((25,25,75,75), fill=(255,0,0))

img.save('test.png', 'PNG')
