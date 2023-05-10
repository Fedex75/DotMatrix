from PIL import Image

im = Image.open('example_5x7.png')
pix = im.load()

FONT_WIDTH = 5
FONT_HEIGHT = 7

TEMPLATE_WIDTH = 12
TEMPLATE_HEIGHT = 8

def get_pixel(char_x, char_y, dot_x, dot_y):
    return pix[char_x * (FONT_WIDTH + 3) + 1 + dot_x, char_y * (FONT_HEIGHT + 3) + 1 + dot_y]

def split_string(string, n):
    return [string[i:i+n] for i in range(0, len(string), n)]

segments = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

segment_counter = 0
for dot_y in range(0, 7):
    for dot_x in range(0, 5):
        char = 126
        out = ''
        
        for y in range(7, -1, -1):
            for x in range(11, -1, -1):
                if get_pixel(x, y, dot_x, dot_y) == (0, 0, 0, 255):
                    out += '1'
                else:
                    out += '0'

                char -= 1

        out = ' '.join([str(int(b, 2)) for b in split_string(out, 32)])

        print('{}: {}'.format(segments[segment_counter], out))
        
        segment_counter += 1