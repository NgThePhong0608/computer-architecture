import time
import Adafruit_Nokia_LCD as LCD
# Khai báo thư viện pillow để tạo và vẽ hình
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    # Khai báo các pin GPIO
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp  # khởi tạo biến global
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)  # Khởi tạo LCD
    disp.begin(contrast=60)
    # cài đặt độ sáng
    # # xóa màn hình.
    disp.clear()
    disp.display()  # tạo ảnh 1 bit color, với chiều rộng, cao bằng của LCD
    image = Image.new('1', (LCD.LCDWIDTH, LCD. LCDHEIGHT))
    # chọn đối tượng để vẽ.
    draw = ImageDraw.Draw(image)  # vẽ 1 hình chữ nhật màu trắng
    draw.rectangle((0, 0, LCD.LCDWIDTH-1, LCD. LCDHEIGHT-1),
                   outline=0, fill=255)
    # và các hình khác
    draw.ellipse((2, 2, 22, 22), outline=0, fill=255)
    draw.rectangle((24, 2, 44, 22), outline=0, fill=255)
    draw.polygon([(46, 22), (56, 2), (66, 22)], outline=1, fill=255)
    draw.line((68, 22, 81, 2), fill=0)

    draw.line((68, 2, 81, 22), fill=0)
    # load font chữ để chèn. (font chữ mặc định)
    font = ImageFont.load_default()
    draw.text((8, 30), 'Hello world!', font=font)
    # chèn chữ # hiển thị hình ảnh
    disp.image(image)
    disp.display()
    while True:
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:  # xử lí sự kiện Ctrl+c
    disp.clear()
