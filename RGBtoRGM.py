#! /usr/bin/env python
# Author: Umesh Mohan (umesh@heterorrhina.in)
'''
Convert an RGB image into RGM (magenta) image for 
red-green colorblind people to distinguish with the help of blue hue. 
This program computes magenta "channel" by adding red and blue channels. 
The original blue channel is then replaced with this computed magenta channel.
'''
try:
    import Image, ImageMath
except ImportError:
    from PIL import Image, ImageMath

def RGBtoRGM(image):
    r, g, b = image.split()
    m = ImageMath.eval('convert(x+y,"L")', x=r, y=b)
    return Image.merge('RGB', (r, g, m))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_image', help='Input image file')
    parser.add_argument('-o', '--output', help='Output image file', default=None)
    arguments = parser.parse_args()
    input_image = arguments.input_image
    if arguments.output is None:
        output_image = '.'.join(input_image.split('.')[:-1] + ['RGM'] + [input_image.split('.')[-1]])
    else:
        output_image = arguments.output
    RGBtoRGM(Image.open(input_image)).save(output_image)