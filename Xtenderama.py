#         WELCOME. DO NOT CHANGE THE CODE BELOW, EVEN FOR GOOD.
#
#         The program supposed to use with Python 3.4.1
#
#         All your blames, greetings and ideas about the program
#         please address to Yury Mishulin / ymishulin@slb.com /
#
#         Thanks for reading

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 30

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

import ctypes

# Constants from the Windows API
STD_OUTPUT_HANDLE = -11
FOREGROUND_RED    = 0x0004 # text color contains red.

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

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
print ("Cherry on top")
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)

while True:
    print('Xtenderama v.0.2.1 "Power of Imperfection"')
    print('[start]')
    from fractions import Fraction


    a = input('''Enter full length: ''')
    def drobilka(arg):
        a = arg.split()
        am1 = a[0]
        aL = len(a)
        if aL < 2:
            am2 = 0
        else:
            am2 = a[1]
        a1 = Fraction(am1)
        a2 = Fraction(am2) 
        return (a1 + a2)
    b = input('''Enter pin length (0 if none): ''')
    c1 = input('''
╔═════╤═════════════════════╗  ╔═════╤═════════════════════╗
║  #  │         PIN         ║  ║  #  │        BOX          ║
╠═════╪═════════════════════╣  ╠═════╪═════════════════════╣  
║  0  │     RTLM = 1.25     ║  ║  5  │    RTLF = 2.00      ║
║  1  │     MEXM = 3.257    ║  ║  6  │    MEXM = 1.838     ║
║  2  │     MEXD = 3.417    ║  ║  7  │    MEXC = 1.678     ║
║  3  │     MEXC = 3.417    ║  ║  8  │    EXTF = 1.678     ║
║  4  │     MXLD = 3.417    ║  ║  9  │    EXTM = 1.678     ║
╚═════╧═════════════════════╝  ╚═════╧═════════════════════╝

Enter a number from '0' t0 '9' to select a 'C' value: ''')
    m = [1.25, 3.257, 3.417, 3.417, 3.417, -2.00, -1.838, -1.678, -1.678, -1.678]
    c1 = int(c1)
    c = m[c1]
    d = drobilka(a) - drobilka(b) + c #десятичная длина
    dfrac = Fraction(d) #дробная длина
    d1 = dfrac.numerator
    d2 = dfrac.denominator
    d3 = d1 / d2
    d4 = int(d3)
    d5 = d3 - d4
    #d3 = d1 / d2
    #d4 = int((d1) // (d2))
    #d5 = d1 % d2
    d6 = d5 * 32
    d6 = int(round(d6))
    d6 = Fraction(d6/32)
    dround = round((d3), 3)
#    drb = (d4, d6)
    if c1 == 0:
        flcdc = str('RTLM, c = 1.25')
    elif c1 == 1:
        flcdc = str('MEXM, c = 3.257')
    elif c1 == 2:
        flcdc = str('MEXD, c = 3.417')
    elif c1 == 3:
        flcdc = str('MEXC, c = 3.417')
    elif c1 == 4:
        flcdc = str('MXLD, c = 3.417')
    elif c1 == 5:
        flcdc = str('RTLF, c = 2.00')
    elif c1 == 6:
        flcdc = str('MEXM, c = 1.838')
    elif c1 == 7:
        flcdc = str('MEXC, c = 1.678')
    elif c1 == 8:
        flcdc = str('EXTF, c = 1.678')
    elif c1 == 9:
        flcdc = str('EXTM, c = 1.678')
#    import os
#    clear = lambda: os.system('cls')
#    clear()

    from time import sleep
    import sys

    def print_slowly(text):
        for c in text:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.01)

    print_slowly('████████████████████████████████████████████████████████████')

    import os
    clear = lambda: os.system('cls')
    clear()

    print('Computed for L = ' + (a) + ', Pin L = ' + (b) + ', Filecode = ' + (flcdc))
    print('''
''')
    
    print('''════════════════════════════════════════════════════════════
''')
    print('Extender length = ' + str(dround) + ' or ' + str(d4) + ' ' + str(d6))

    RTLM = {0: [31.54, 34.28, ('RTLM-CC')], 1: [41.28, 44.02, ('RTLM-BD')]}
    MEXM = {0: [31.63, 35.15, ('MEXM-AA, -EA')], 1: [28.13, 31.65, ('MEXM-BA, -FA')], 2: [24.63, 28.15, ('MEXM-CA, -GA')], 3: [34.13, 37.65, ('MEXM-DA, -HA')], 4: [50.48, 54.00, ('MEXM-JA ')]}
    MEXD = {0: [27.82, 30.16, ('MEXD-BA, -BB, -BC')], 1: [30.22, 32.56, ('MEXD-CA, -CB, -CC')], 2: [25.36, 27.76, ('MEXD-DB, -DC')], 3: [31.96, 34.36, ('MEXD-EB')], 4: [22.36, 24.76, ('MEXD-GA')], 5: [19.36, 21.76, ('MEXD-HA')]}
    MEXC = {0: [32.11, 33.94, ('MEXC-BA')], 1: [30.32, 32.66, ('MEXC-EA, -JA')], 2: [13.00, 14.88, ('MEXC-AB, -KA')], 3: [27.92, 30.26, ('MEXC-LA')], 4: [25.56, 27.90, ('MEXC-MA')], 5: [10.60, 12.48, ('MEXC-CA, -NA')], 6: [8.24, 10.12, ('MEXC-DA, -PA')]}
    MXLD = {0: [51.82, 54.16, ('MXLD-BA')], 1: [51.39, 53.73, ('MXLD-CA, -CB, -CC')], 2: [49.39, 51.73, ('MXLD-DA, -DB, -DC')], 3: [47.39, 49.73, ('MXLD-EA, -EB, -EC')]}
    RTLF = {0: [14.96, 17.58, ('RTLF-BB, -BC, -DA')], 1: [12.85, 13.75, ('RTLF-CA')], 2: [28.81, 31.43, ('RTLF-EA')]}
    EXTF = {0: [12.82, 15.16, ('EXTF-AA, -DA, -DB')], 1: [10.41, 12.75, ('EXTF-BA')], 2: [8.06, 10.40, ('EXTF-CA')]}
    EXTM = {0: [15.49, 17.99, ('EXTM-AB, -FA, -KA')], 1: [13.37, 15.87, ('EXTM-BB, -DA')], 2: [11.25, 13.75, ('EXTM-CB, -HA')], 3: [11.22, 11.83, ('EXTM-EA')], 4: [17.58, 20.08, ('EXTM-GA, -GB')], 5: [22.07, 24.57, ('EXTM-JB')], 6: [19.92, 22.42, ('EXTM-JC')]}
    if c1 == 0:
        dic = RTLM
    elif c1 == 1:
        dic = MEXM
    elif c1 == 2:
        dic = MEXD
    elif c1 == 3:
        dic = MEXC
    elif c1 == 4:
        dic = MXLD
    elif c1 == 5:
        dic = RTLF
    elif c1 == 6:
        dic = MEXM
    elif c1 == 7:
        dic = MEXC
    elif c1 == 8:
        dic = EXTF
    elif c1 == 9:
        dic = EXTM


    #РАБОЧИЙ КОД
    #failure_count = 0
    #for i in range (0, len(dic)):
    #    elem = dic[i]
    #    ext_min = elem[0]
    #    ext_max = elem[1]
    #    ext_flcd = elem[2]    
    #    if ext_min <= (d3) <= ext_max:
    #        print('The length match exactly with ' + str(ext_flcd))
    #    elif ext_min - 0.06 <= (d3) <= ext_max + 0.06:
    #        print('The length match with min or max limit of ' + str(ext_flcd))
    #    else:
    #        failure_count += 1 
    #        if failure_count == len(dic):
    #            print('No match found')


    failure_count = 0

    def matcher(arg):
        for i in range (0, len(dic)):
            elem = dic[i]
            ext_min = elem[0]
            ext_max = elem[1]
            ext_flcd = elem[2]    
            if ext_min <= arg <= ext_max:
                return ('The length match exactly with ' + str(ext_flcd))
            elif ext_min - 0.06 <= arg <= ext_max + 0.06:
                return ('The length match with min or max limit of ' + str(ext_flcd))
    #        else:
    #            failure_count += 1 
    #            if failure_count == len(dic):
    #                return ('No match found')

    print('Filecode >> ' + str(matcher(d3)))

    print('''
════════════════════════════════════════════════════════════
''')

    if c1 == 2 or c1 == 4:
        print('''Checking for possibility to use extender with extensions:
''')
        print('With 4.5 + 4.5 >> ' + str(matcher(d3 - 9.0)))
        print('With 4.5 + 3.0 >> ' + str(matcher(d3 - 7.5)))
        print('With 4.5 + 2.4 >> ' + str(matcher(d3 - 6.9)))
        print('With 3.0 + 3.0 >> ' + str(matcher(d3 - 6.0)))
        print('With 3.0 + 2.4 >> ' + str(matcher(d3 - 5.4)))
        print('With 2.4 + 2.4 >> ' + str(matcher(d3 - 4.8)))
        print('With 4.5 >> ' + str(matcher(d3 - 4.5)))
        print('With 3.0 >> ' + str(matcher(d3 - 3.0)))
        print('With 2.4 >> ' + str(matcher(d3 - 2.4)))

    elif c1 == 3:
        dic = MEXD
        print("""It's also possible to use MEXD with S-402745 adapter instead of MEXC
              """)
        print('''If MEXD w/ adapter                 >> ''' + str(matcher(d3 - 2.4)))
        print('''If MEXD w/ adapter + 2.4 extension >> ''' + str(matcher(d3 - 4.8)))
        print('''If MEXD w/ adapter + 3.0 extension >> ''' + str(matcher(d3 - 5.4)))
        print('''If MEXD w/ adapter + 4.5 extension >> ''' + str(matcher(d3 - 6.9)))

    if c1 == 6:
        d3 = d1 / d2
        d3 = d3 - 0.07
        d4 = int(d3)
        d5 = d3 - d4
        #d3 = d1 / d2
        #d4 = int((d1) // (d2))
        #d5 = d1 % d2
        d6 = d5 * 32
        d6 = int(round(d6))
        d6 = Fraction(d6/32)
        dround = round((d3), 3)
        print('''If MEXM supposed to be install into LWD tool (StethoScope, SonicVISION, PeriScope keep in mind you have to use spacer 100262007 between the extender and tool extender base. See corrected length below: ''')
        print('''------------------------------------------------------------''')
        print('Extender length = ' + str(dround) + ' or ' + str(d4) + ' ' + str(d6))
        print('Filecode >> ' + str(matcher(d3)))
        print('''------------------------------------------------------------''')
        
    print('''
Press Enter to restart or 'q' to quit''')
    q = input()
    if q == 'q':
        break
