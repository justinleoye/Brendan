import urllib,urllib2, random
import Image,ImageEnhance,ImageFilter

import os

for i in range(50):
    url = "http://www.k4w.cn/message/code.html"
    print "download"
    file("./img/%04d.png" % random.randrange(10000), "wb").write(urllib.urlopen(url).read())

#compare the first column of font-box
def left_comp(img,pixdata,colors,not_target_color,might_color,p_left,p_top):
    
    for y in range(img.size[1]):
            if pixdata[p_left,y] in not_target_color:
                continue
            if pixdata[p_left,y] not in colors:
                colors.append(pixdata[p_left,y])

            if pixdata[p_left,y] == pixdata[p_left-1,y] or pixdata[p_left,y] != pixdata[p_left+1,y]:
                not_target_color.append(pixdata[p_left,y])
                if pixdata[p_left,y] in might_color:
                    might_color.remove(pixdata[p_left,y])
            
            else:
                if pixdata[p_left,y] not in might_color:
                    might_color.append(pixdata[p_left,y])

def right_comp(img,pixdata,colors,not_target_color,might_color,p_left,p_top):
    # check right edge color
    for y in range(img.size[1]):
        # already in the not target color list
        if pixdata[p_left+7,y] in not_target_color:
            continue
        #  not in the might color list, so must not target color
        if pixdata[p_left+7,y] not in might_color:
            not_target_color.append(pixdata[p_left+7,y])
        # not in the colors list, append
        if pixdata[p_left+7,y] not in colors:
            colors.append(pixdata[p_left+7,y])
        # same to the next column,so not the target color
        if pixdata[p_left+7,y] == pixdata[p_left+7+1,y]:
            not_target_color.append(pixdata[p_left+7,y])
            if pixdata[p_left+7,y] in might_color:
                might_color.remove(pixdata[p_left+7,y])

def right_comp_del(img,pixdata,colors,not_target_color,might_color,p_left,p_top):
    for color in might_color:
        #print 'color',color
        for y in range(img.size[1]):
            if pixdata[p_left+7,y] == color:
                #print color,'break'
                break
            if y == img.size[1]-1:
                #print 'y=',y
                might_color.remove(color)

def interval_del(img,pixdata,colors,not_target_color,might_color,p_left,p_top):
    for color in might_color:
        for y in range(img.size[1]):
            if pixdata[p_left+8,y] == color:
                might_color.remove(color)

def get_number(pixdata,f_color,fbox_left,fbox_top):
    if pixdata[fbox_left,fbox_top] == f_color:
        if pixdata[fbox_left,fbox_top+1] == f_color:
            return 5
        else:
            return 7
    else:
        if pixdata[fbox_left,fbox_top+1] == f_color:
            return 3
        else:
            if pixdata[fbox_left,fbox_top+2] == f_color:
                if pixdata[fbox_left,fbox_top+3] == f_color:
                    if pixdata[fbox_left,fbox_top+4] == f_color:
                        return 6
                    else:
                        return 9
                else:
                    if pixdata[fbox_left,fbox_top+6] == f_color:
                        return 8
                    else:
                        return 2
            else:
                if pixdata[fbox_left,fbox_top+3] == f_color:
                    return 0
                else:
                    if pixdata[fbox_left,fbox_top+5] == f_color:
                        return 4
                    else:
                        return 1

def get_numbers(pixdata,might_color,p_left,p_top):
    numbers = []
    f_color = might_color[0]
    for i in range(4):
        fbox_left = p_left + i * 9
        fbox_top = p_top
        n = get_number(pixdata,f_color,fbox_left,fbox_top)
        numbers.append(n)
    return numbers



dir = "./img/"
path = "./font/"
for f in os.listdir(dir):
    if f.endswith(".png"):
        print dir+f
        img = Image.open(dir+f)
        img = img.convert("RGB")
        pixdata = img.load()

        colors = []
        not_target_color = []
        might_color = []
        p_left = 15
        p_top = None

        #~ print pixdata[p_left,0]
        #~ print img.size[1]
        step = 0
        #because may '1' at the start place
        while might_color == [] and step <=27:
            
            left_comp(img,pixdata,colors,not_target_color,might_color,p_left+step,p_top)
            step += 9

        #~ print 'colors:',colors
        #~ print 'not target:',not_target_color

        #~ print 'might color1:',might_color
        
        if len(might_color) == 1:
            #set top
            for y in range(img.size[1]):
                if p_top != None:
                    break
                for x in range(8):
                    if pixdata[x+p_left,y] in might_color:
                        p_top = y
                        #print "top:",p_top
                        break
        else:
            right_comp_del(img,pixdata,colors,not_target_color,might_color,p_left,p_top)
            right_comp(img,pixdata,colors,not_target_color,might_color,p_left,p_top)
            interval_del(img,pixdata,colors,not_target_color,might_color,p_left,p_top)
            
                        
            if len(might_color) == 1:
                # set top
                for y in range(img.size[1]):
                    if p_top != None:
                        break
                    for x in range(8):
                        if pixdata[x+p_left,y] in might_color:
                            p_top = y
                            #print "top:",p_top
                            break
        print "might color:",might_color
        print p_left,p_top
        numbers = get_numbers(pixdata,might_color,p_left,p_top)
        result = dir
        for n in numbers:
            result += str(n)
        result += '.png'
        print "save to",result
        img.save(result)
        
