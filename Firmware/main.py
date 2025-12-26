import board
import displayio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.display import Display, ImageEntry
import adafruit_ssd1306

keyboard = KMKKeyboard()

# MATRIX
keyboard.row_pins = (
    board.GP26,  # R0
    board.GP27,  # R1
    board.GP28,  # R2
)

keyboard.col_pins = (
    board.GP29,  # C0
    board.GP0,   # C1
    board.GP3,   # C2
    board.GP4,   # C3
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# BUTON ENCODER
keyboard.coord_mapping = [
    0, 1, 2,
    4, 5, 6,
    8, 9, 10,
    12,
]

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9,
        KC.BRIU,
    ]
]

keyboard.matrix = KeysScanner(
    pins=(board.GP2,),
    value_when_pressed=False,
)

# ENCODER ROTIRE
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.GP1, board.GP0),  # A, B
)

encoder.map = [
    ((KC.VOLD, KC.VOLU),),
]

#OLED
displayio.release_displays()

i2c = board.I2C()
display = adafruit_ssd1306.SSD1306_I2C(
    128, 32, i2c, addr=0x3C
)

oled = Display(
    display=display,
    entries=[
        ImageEntry(
            image_file='image.bmp',
            x=0,
            y=0
        ),
    ],
)

keyboard.extensions.append(oled)

if __name__ == '__main__':
    keyboard.go()