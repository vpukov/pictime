from PIL import Image, ImageDraw, ImageFont
import os
import sys
import time

TEXT_COVER_PERCENT = 25
FONT_FILE = 'C:\Windows\Fonts\Arial.ttf'
#FONT_FILE = 'C:\Windows\Fonts\digital-7 (mono).ttf'

def ApplyText(inputfile, text, outputfile):
    try:
        img = Image.open(inputfile)
    except:
        print("Could not open file: ", inputfile)
        return False
    dr = ImageDraw.Draw(img)
    h,v = img.size
    smallerside = v
    if(h < v):
        smallerside = h #get smaller side

    fontSize = int(2 * ((smallerside / (100/TEXT_COVER_PERCENT)) // len(text)))
    myFont = ImageFont.truetype(FONT_FILE, fontSize)
    text_place_h = h - ((2 + len(text)) * (fontSize/2))
    text_place_v = v - (2 * fontSize)
    dr.text((text_place_h, text_place_v), text, font=myFont, fill =(255, 0, 0))

    #img.show()
    img.save(outputfile, 'JPEG', quality=98)
    return True
    
def Usage():
    print("Usage:   pictime.py <inputpath> <outputpath>")
    print("         pictime.py <outputpath>")
    
    
def GetTimeString(filename):
    month = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #time.struct_time(tm_year=2018, tm_mon=6, tm_mday=27, tm_hour=5, tm_min=3, tm_sec=48, tm_wday=2, tm_yday=178, tm_isdst=1)
    #modif_time = os.path.getctime(full_path)
    creat_time = os.path.getctime(full_path)
    tm = time.localtime(creat_time)
    return "%i %s %04i %02i:%02i"%(tm.tm_mday, month[tm.tm_mon], tm.tm_year, tm.tm_hour, tm.tm_min)
    
    
input_path = "."
output_path = ""
if (len(sys.argv) == 2):
    output_path = sys.argv[1]
elif(len(sys.argv) == 3):
    input_path  = sys.argv[1]
    output_path = sys.argv[2]
else:
    Usage()
    sys.exit()
    

if os.path.exists(input_path) is True:
    if os.path.exists(output_path) is False:
        try:
            os.mkdir(output_path)
        except Exception as e:
            print("Faild to create output folder ", output_path, " Error message: ", e.args)
            
    for f in os.listdir(input_path):
        if not input_path.endswith('\\'):
            input_path = input_path + "\\"
        F = f.upper()
        if F.endswith('.JPG') or F.endswith('.JPEG'):
            full_path = input_path + F
            time_string = GetTimeString(full_path)
            ApplyText(full_path, time_string, output_path + "\\" + F)
            print("%-20s %s"%(full_path, time_string))
            
else:
    print("Input path ", input_path, " doesn't exist!")
    


