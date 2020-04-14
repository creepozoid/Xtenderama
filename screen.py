import ctypes

# Constants from the Windows API
STD_OUTPUT_HANDLE = -11

FOREGROUND_BLUE      = 0x0001 # text color contains blue.
FOREGROUND_GREEN     = 0x0002 # text color contains green.
FOREGROUND_CYAN      = 0x0003
FOREGROUND_RED       = 0x0004 # text color contains red.
FOREGROUND_MAGENTA   = 0x0005
FOREGROUND_YELLOW    = 0x0006
FOREGROUND_GREY      = 0x0007
#FOREGROUND_WHITE     = 0x0008
FOREGROUND_INTENSITY = 0x0008 # text color is intensified.
BACKGROUND_BLUE      = 0x0010 # background color contains blue.
BACKGROUND_GREEN     = 0x0020 # background color contains green.
BACKGROUND_RED       = 0x0040 # background color contains red.
BACKGROUND_INTENSITY = 0x0080 # background color is intensified.


Black   = 0x0000,
Blue    = 0x0001,
Green   = 0x0002, 
Cyan    = 0x0003,
Red     = 0x0004,
Magenta = 0x0005,
Yellow  = 0x0006,
Grey    = 0x0007,
White   = 0x0008


def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_YELLOW)
print ("Cherry on top")


ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_CYAN)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
print ("Cherry on top")
print ("Cherry on top")

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)


input()
