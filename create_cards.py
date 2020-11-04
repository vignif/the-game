from PIL import Image, ImageDraw
folder = './cards/'

def create_it(num):
    img = Image.new('RGB', (25, 35), color='white')
    d = ImageDraw.Draw(img)
    d.text((5,10), str(num), fill=(0,0,0))
    img.save(folder+str(num)+'.png')

if __name__ == '__main__':
    for i in range(0,101):
        create_it(i)