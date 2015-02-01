from Tkinter import *
import tkMessageBox
import random
import time
import os, sys
import webbrowser

import math
from math import sqrt, pow
from math import sin, cos, atan2, degrees, radians, pi
import winsound
import pygame
from PIL import ImageTk

global stat
global xc
global yc

stat = "first"
WIDTH = 500
HEIGHT = 500
MAXRAD = 60
PI = 3.14159
xc = WIDTH / 2
xc = HEIGHT / 2

col_index = 0
cols = ("red", "yellow", "blue", "orange", "green", "purple", "brown")

col = cols[col_index]

global pause
pause = True

#setting up the GUI
window = Tk()
#setting up the window title
window.wm_title("Project")

#obtaining project root folder
path = sys.path[0]

canvas= Canvas(window,width=1000, height=631, bg='light gray')
canvas.pack(expand = YES, fill = BOTH)

def shift_centre_proc(event):
    global xc
    global yc
    global stat
    if stat == "first":
        stat = "second"
        return
    xc = event.x
    yc = event.y

def my_draw_proc(event):
    global stat
    global col_index
    global col
    if stat == "first":
        canvas.create_text(200, 100, font = "Arial 12",\
        text="LH Mouse Butt - change flower position, \n"+\
                    "RH Mouse Butt - pop up menu")
        canvas.create_text(200,130,font="Arial 12 bold", text="OK")
        canvas.create_rectangle(60,80,340,140)
        return

    x = event.x
    y = event.y
    xr = x - xc
    yr = y - yc
    ang = 0
    if xr != 0:
        ang = math.atan(yr / xr + 0.0)

    rad = math.sqrt( (xr * xr) + (yr * yr) )
    if rad > MAXRAD:
        return
    for i in range (1,21):
        ang = ang + PI/10.0
        x = xc + rad * math.cos(ang)
        y = yc + rad * math.sin(ang)
        canvas.create_line(x,y,x+6,y,width=6,fill=col)

    col_index = col_index = 1
    if col_index > 9:
        col_index = 0
    col = cols[col_index]

#def clear_proc():
#    canvas.create_rectangle(1,1,WIDTH+2,HEIGHT+2,fill="white")

def menu_proc(event):
    my_menu.post(event.x_root,event.y_root)

def quit_proc():
    if tkMessageBox.askokcancel("Quit", "Are you sure ?")\
       == True:
        canvas.destroy()
        

canvas.bind("<Motion>", my_draw_proc)
canvas.bind("<Button-1>" , shift_centre_proc)
canvas.bind("<Button-3>" , menu_proc)

my_menu = Menu(canvas, tearoff=0)
#my_menu.add_command(label="clear", comman=clear_proc)
my_menu.add_command(label="quit", command=quit_proc)





#play music

    #setup mixer 
pygame.mixer.pre_init(44100, -16, 2, 2048)

    #initialize pygame
pygame.init()

    #initialize background music
pygame.mixer.music.load('sound/track_1.ogg')
pygame.mixer.music.play()
v=0.5
pygame.mixer.music.set_volume(v)

#pause function
def pausegame():
    global pause
    if pause == False:
        pause = True
        pygame.mixer.music.pause()
        pausebutton["text"] = "Start"
    else:
        pygame.mixer.music.unpause()
        pause=False
        pausebutton["text"] = "Pause"
        
global move
move=False

#end function

#import end images
success = ImageTk.PhotoImage(file = path+"/end/success.png")
time_out = ImageTk.PhotoImage(file = path+"/end/time_out.png")

END = True
def endgame():
    global END
    END == False
    END = True
    canvas.create_image(0, 0, image = success, anchor = NW)
    canvas.update()


global END
END=False



#press space to start
global move
move=False
def Space(self):
    global move
    move = True


#bind the space key to the space function
window.bind('<space>', Space)

#title image
title1 = ImageTk.PhotoImage(file = path+"/start/start.png")
title2 = ImageTk.PhotoImage(file = path+"/start/start1.png")

#startup animation
while move==False:
    titlex=canvas.create_image(0, 0, image = title1, anchor = NW)
    time.sleep(0.5)
    canvas.update()
    titlex=canvas.create_image(0, 0, image = title2, anchor = NW)
    time.sleep(0.5)
    canvas.update()

#red robot score
label1 = Label(text="Red robot score:",font=("Helvetica", 10))
label1.pack(padx=10, pady=0, side=LEFT)

score=0
labels1 = Label(text=score,font=("Helvetica", 10))
labels1.pack(padx=0, pady=0, side=LEFT)

#placeholder
label0 = Label(text=" ",font=("Helvetica", 10))
label0.pack(padx=2, pady=0, side=LEFT)

#adding the timer
#minutes(left number)
minn=0
labelm = Label(text=minn,font=("Helvetica", 10))
labelm.pack(padx=0, pady=0, side=LEFT)
#colon
label = Label(text=":",font=("Helvetica", 10))
label.pack(padx=0, pady=0, side=LEFT)
#seconds (right number)
sec=0
labels = Label(text=sec,font=("Helvetica", 10))
labels.pack(padx=1, pady=0, side=LEFT)

probcount1 = 100
labels3 = Label(text= probcount1,font=("Helvetica", 10))
labels3.pack(padx=0, pady= 0, side=RIGHT)

label3 = Label(text="Likeness of Blue gambling:",font=("Helvetica", 10))
label3.pack(padx=0, pady= 0, side=RIGHT)

probcount2 = 100
label4 = Label(text="Likeness of Red gambling:",font=("Helvetica", 10))
label4.pack(padx=0, pady= 0, side=LEFT)

labels4 = Label(text=probcount2 ,font=("Helvetica", 10))
labels4.pack(padx=0, pady= 40, side=LEFT)

#blue robot score
score=0
labels2 = Label(text=score,font=("Helvetica", 10))
labels2.pack(padx=0, pady=0, side=RIGHT)

label2 = Label(text="Blue robot score:",font=("Helvetica", 10))
label2.pack(padx=10, pady=0, side=RIGHT)

#placeholder 2
#label0 = Label(text=" ",font=("Helvetica", 10))
#label0.pack(padx=25, pady=0, side=LEFT)

#add volume slider
volume =Scale(window,orient=HORIZONTAL,width=10,length=150.0,from_= 0,to= 100,tickinterval=20,resolution=10,sliderlength=25,label="Volume")
v=50
volume.set(v)
volume.pack(padx=5, pady=0, side=LEFT)

#add pop-up checkbox
pop=IntVar()
c = Checkbutton(window, text="Pop-ups", variable=pop)
c.select()
c.pack()

#add a pause button
pausebutton = Button(window, text= "Pause" ,command = pausegame, width = 10)
pausebutton.pack()
pausegame()

#add an END button

endbutton = Button(window, text="END", command=endgame, width = 10)
endbutton.pack()
endgame()

#add a change color button
def colorchange ():
     r2d2.colorChange()
     c3po.colorChange()
     treasurestealer.colorChange()
colorbutton = Button(window, text= "Change Colors" ,command = colorchange, width = 10)
colorbutton.pack()

#add a next song button
global song
song=1
def nextsong ():
    if pause == False:
        global song
        song=song+1
        if song == 4:
            song=1
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sound/track_'+str(song)+'.ogg')
        pygame.mixer.music.play()
nextsong = Button(window, text= "Change Song" ,command = nextsong, width = 10)
nextsong.pack()


#import background image
bg = ImageTk.PhotoImage(file = path+"/Map_of_Bulgaria.jpg")
canvas.create_image(0, 0, image = bg, anchor = NW)


#import gold image
gold = ImageTk.PhotoImage(file = path+"/Images/type_11.png")

#import landmark titles
text1 = ImageTk.PhotoImage(file = path+"/text/text1.png")
text2 = ImageTk.PhotoImage(file = path+"/text/text2.png")
text3 = ImageTk.PhotoImage(file = path+"/text/text3.png")
text4 = ImageTk.PhotoImage(file = path+"/text/text4.png")
text5 = ImageTk.PhotoImage(file = path+"/text/text5.png")
text6 = ImageTk.PhotoImage(file = path+"/text/text6.png")
#return the angle between two points
def angle(x0, y0, x1, y1):
    return degrees( atan2(y1-y0, x1-x0) )

#return the distance between two points
def distance(x0, y0, x1, y1):
    return sqrt(pow(x1-x0, 2) + pow(y1-y0, 2))

#return the coordinates of given distance and angle from a point
def coordinates(x0, y0, distance, angle):
    return (x0 + cos(radians(angle)) * distance,
            y0 + sin(radians(angle)) * distance)

Bar1 = canvas.create_rectangle(760,70,790,100, fill='blue')
Bar2=canvas.create_rectangle(790,70,820,100, fill='blue')
Bar3 =canvas.create_rectangle(820,70,850,100, fill='blue')

def linearSearch(myItem, myList):
        found = False
        position = 0
        while position < len(myList) and not found:
            if myList[position]==myItem:
                found = True
            position = position + 1
        return found

class World: 
    def __init__(self):
        self.landmarks = []
        self.logo = []


class Landmark:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
    def drawLandmark(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_image(self.x, self.y, image = self.I, anchor = CENTER)


class Logo:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
    def drawLogo(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_image(self.x, self.y, image = self.I, anchor = CENTER)

def draw (x,y,z):
    logo = Logo(500,315, ImageTk.PhotoImage (file = path+x))
    world.logo.append(logo)
    logo.drawLogo(canvas)
    time.sleep(y)
    canvas.update()
    world.logo.remove(logo)
    time.sleep(z)
    canvas.update()

def reset (Bar1, Bar2, Bar3):
    canvas.itemconfig(Bar1, fill="blue")
    canvas.itemconfig(Bar2, fill="blue")
    canvas.itemconfig(Bar3, fill="blue")


def ColourChange(k1, Bar1):
    
    if k1 == 0:
        canvas.itemconfig(Bar1, fill="red")
    elif k1 == 1:
        canvas.itemconfig(Bar1, fill="yellow")
    elif k1 == 2:
        canvas.itemconfig(Bar1, fill="purple")
    elif k1 == 3:
        canvas.itemconfig(Bar1, fill="orange")
    elif k1 == 4:
        canvas.itemconfig(Bar1, fill="green")
    else:
        canvas.itemconfig(Bar1, fill="pink")
        
        
    time.sleep(2)
    canvas.update()

def LuckySearch():
    draw("/MyImages/GambleScreen.png", 0,0)
    draw("/MyImages/GambleScreenYes.png",2,1)
        
        
    j1 = random.randint(0,4)
    j2 = random.randint(0,4)
    j3 = random.randint(0,4)
    
    ColourChange(j1, Bar1)
    ColourChange(j2, Bar2)
    ColourChange(j3, Bar3)
    
    if j1 == j2 == j3:
        print 'jackpot'
        draw("/MyImages/jackpot.png",1,1)
        time.sleep(2)
        canvas.update()
        return (4, 1000)
            

    elif j1== j2 or j2 == j3:
        print '2 in a row'
        draw("/MyImages/twoinarow.png",1,1)
        time.sleep(2)
        canvas.update()
        return(1, 200)           

    else:
        print 'unlucky'
        draw("/MyImages/unlucky.png",1,1)
        time.sleep(2)
        canvas.update()
        return(-4, -200)
            

    time.sleep(0.5)
    canvas.update()

def NoDice():
     draw("/MyImages/GambleScreen.png", 0,0)
     draw("/MyImages/GambleScreenNo.png", 2,1)
     return(0, 0)

global c
c = [1 for j in range(6)]

class Robot(World):
    
    def __init__(self, name, world, x, y, I, speed=1.0, score =0, currentimage=0, regret = 0):
        
        self.speed = speed
        
        self.x = x 
        self.y = y 
        self.score = score
        self.I = I
        self.regret = regret

        self.name=name
        self.currentimage=0
        self.world = world
        self.feeler_length = 25
        
        self._vx = 0
        self._vy = 0
        
        
    def heading(self):

        """ Returns the robot's heading as angle in degrees.
        """

        return angle(self.x, self.y, self.x+self._vx, self.y+self._vy)

    def colorChange(self):
        r=random.randint(0, 3)
        while ( r==self.currentimage):
            r=random.randint(0, 3)
        self.currentimage=r
        name=self.name
        self.I=ImageTk.PhotoImage (file = path+"/Images/"+name+"_"+str(r)+".png") 
        self.drawRobot(canvas)
    def avoid_landmarks(self, m = 0.4 , collision=4):

        # Find out where the robot is going.
        a = self.heading()
        
        
        
        for landmark in self.world.landmarks:
            
          
            
           
            
            # Calculate the distance between the robot and the landmark.
            d = distance(self.x, self.y, landmark.x, landmark.y)
            
            # Respond faster if the robot is very close to an landmark.
            if d - 95 <= 4:
                m *= 10.0
                
                theList =world.landmarks[6::]
                theItem = landmark
                
                isFound = linearSearch(theItem, theList)
                i = world.landmarks.index(landmark)

                if isFound:
                    self.colorChange()
                    world.landmarks.remove(landmark)
                    canvas.update()
                    landmark = Landmark(landmark.x,landmark.y, ImageTk.PhotoImage (file = path+"/Images/type_11.png"))
                    world.landmarks.append(landmark)
                    landmark.drawLandmark(canvas)
                    canvas.update()

                    winsound.PlaySound(path+"/sound/sound.mp3", winsound.SND_ASYNC)
                    

                    
                    
                    print("Found")
                    self.score +=100  
                    print self.score

                    if self.regret <-7:
                        self.regret = -7

                    print self.regret , 'regret first'

                    ugo = random.randint(1,8 + self.regret)
                    
                    print ugo , 'ugo'

                    if ugo > 1:
                        x = LuckySearch()
                        reset(Bar1, Bar2, Bar3)
                        print x
                        d =  x[0]
                        g = x[1]
                        self.regret = self.regret + d
                        #print self.regret

                    else:
                        print 'wooo'
                        x = NoDice()
                        print x
                        d =  x[0]
                        g = x[1]
                        self.regret = self.regret + d

                    print self.regret , 'regret second'
                        
              
                    
                    
                    self.score +=g
                    #print self.score
                            
                                 
                
                    
                else:

                        links=["http://bulgariatravel.org/en/object/21/Krepost_Baba_Vida",
                              "http://bulgariatravel.org/en/object/2/Arheologicheski_rezervat_Madara",
                              "http://bulgariatravel.org/en/object/272/rilski_manastir",
                              "http://bulgariatravel.org/en/object/53/Nacionalen_park_Pirin",
                              "http://bulgariatravel.org/en/object/69/sveshtarska_grobnica",
                              "http://bulgariatravel.org/en/object/311/Perperikon"]
        
                        text=[text1, text2, text3, text4, text5, text6]
                        
                        if i < 6:
                            if c[i]==1:
                                self.colorChange()
                                canvas.create_image(landmark.x, landmark.y, image = text[i], anchor = CENTER)
                                if check:
                                    pausegame()
                                    webbrowser.open(links[i])
                                c[i] = c[i] + 1
                                
                                
                               
                
            # Check if the tip of the feeler falls inside the landmark.
            # This is never true if the feeler length
            # is smaller than the distance to the landmark.
            
            if d - 95 <= self.feeler_length:
                tip_x, tip_y = coordinates(self.x, self.y, d, a)
                if distance(landmark.x, landmark.y, tip_x, tip_y) <= 95:
                    
                       

                    # Nudge the robot away from the landmark.
                    m *= self.speed
                    
                    
                    
                    if tip_x < landmark.x:
                        self._vx -= random.randint(0, m)
                        
                    if tip_y < landmark.y:
                        self._vy -= random.randint(0, m)
                    if tip_x > landmark.x:
                        self._vx += random.randint(0, m)
                    if tip_y > landmark.y:
                        self._vy += random.randint(0, m)
                    

                    if d - 95 < 4: return
        
            
    def roam(self):
        
        self.avoid_landmarks()
        
        v = self.speed
        self._vx += random.randint(-v, v)
        self._vy += random.randint(-v, v)
        self._vx = max(-v, min(self._vx, v))
        self._vy = max(-v, min(self._vy, v)) 
        self.x += self._vx
        self.y += self._vy
        self.canvas.coords(self.shape, self.x, self.y)
        self.canvas.update()

        
        if self.x >= 760:
            self._vx = -v
            
        if self.y <= 40:
            self._vy = v
            
        if self.y >= 486:
            self._vy = -v
            
        if self.x <= 40:
            self._vx = v
            
    def drawRobot(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_image(self.x, self.y, image = self.I, anchor = CENTER)

world = World()    
    
        

class StealerRobot(World):
    
    def __init__(self, name, world, x, y, I, speed=1.0, score =0, currentimage=0):
        
        self.speed = speed
        
        self.x = x 
        self.y = y 
        self.score = score
        self.I = I

        self.name=name
        self.currentimage=0
        self.world = world
        self.feeler_length = 25
        
        self._vx = 0
        self._vy = 0
        
        
    def heading(self):

        """ Returns the robot's heading as angle in degrees.
        """

        return angle(self.x, self.y, self.x+self._vx, self.y+self._vy)

    def colorChange(self):
        r=random.randint(0, 3)
        while ( r==self.currentimage):
            r=random.randint(0, 3)
        self.currentimage=r
        name=self.name
        self.I=ImageTk.PhotoImage (file = path+"/Images/"+name+"_"+str(r)+".png") 
        self.drawRobot(canvas)
    def avoid_landmarks(self, m = 0.4 , collision=4):

        # Find out where the robot is going.
        a = self.heading()
        
        
        
        for landmark in self.world.landmarks:
            
          
            
           
            
            # Calculate the distance between the robot and the landmark.
            d = distance(self.x, self.y, landmark.x, landmark.y)
            
            # Respond faster if the robot is very close to an landmark.
            if d - 95 <= 4:
                m *= 10.0
                
                theList =world.landmarks[6::]
                theItem = landmark
                
                isFound = linearSearch(theItem, theList)
                i = world.landmarks.index(landmark)

                if isFound:
                    self.colorChange()
                    
                    world.landmarks.remove(landmark)
                    canvas.update()
                    landmark = Landmark(landmark.x,landmark.y, ImageTk.PhotoImage (file = path+"/Images/image7.png"))
                    world.landmarks.append(landmark)
                    landmark.drawLandmark(canvas)
                    canvas.update()


                    winsound.PlaySound(path+"/sound/sound.mp3", winsound.SND_ASYNC)
                    

                    
                    
                    print("Found")
                    self.score +=100
                    c3po.score -=100
                    r2d2.score -=100
                    
                    print self.score
                                 
                
                    
                else:

                        links=["http://bulgariatravel.org/en/object/21/Krepost_Baba_Vida",
                              "http://bulgariatravel.org/en/object/2/Arheologicheski_rezervat_Madara",
                              "http://bulgariatravel.org/en/object/272/rilski_manastir",
                              "http://bulgariatravel.org/en/object/53/Nacionalen_park_Pirin",
                              "http://bulgariatravel.org/en/object/69/sveshtarska_grobnica",
                              "http://bulgariatravel.org/en/object/311/Perperikon"]
        
                        text=[text1, text2, text3, text4, text5, text6]
                        
                        if i < 6:
                            if c[i]==1:
                                self.colorChange()
                                canvas.create_image(landmark.x, landmark.y, image = text[i], anchor = CENTER)
                                if check:
                                    pausegame()
                                    webbrowser.open(links[i])
                                c[i] = c[i] + 1
                                
                                
                               
                
            # Check if the tip of the feeler falls inside the landmark.
            # This is never true if the feeler length
            # is smaller than the distance to the landmark.
            
            if d - 95 <= self.feeler_length:
                tip_x, tip_y = coordinates(self.x, self.y, d, a)
                if distance(landmark.x, landmark.y, tip_x, tip_y) <= 95:
                    
                       

                    # Nudge the robot away from the landmark.
                    m *= self.speed
                    
                    
                    
                    if tip_x < landmark.x:
                        self._vx -= random.randint(0, m)
                        
                    if tip_y < landmark.y:
                        self._vy -= random.randint(0, m)
                    if tip_x > landmark.x:
                        self._vx += random.randint(0, m)
                    if tip_y > landmark.y:
                        self._vy += random.randint(0, m)
                    

                    if d - 95 < 4: return
        
            
    def roam(self):
        
        self.avoid_landmarks()
        
        v = self.speed
        self._vx += random.randint(-v, v)
        self._vy += random.randint(-v, v)
        self._vx = max(-v, min(self._vx, v))
        self._vy = max(-v, min(self._vy, v)) 
        self.x += self._vx
        self.y += self._vy
        self.canvas.coords(self.shape, self.x, self.y)
        self.canvas.update()

        
        if self.x >= 760:
            self._vx = -v
            
        if self.y <= 40:
            self._vy = v
            
        if self.y >= 486:
            self._vy = -v
            
        if self.x <= 40:
            self._vx = v
            
    def drawRobot(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_image(self.x, self.y, image = self.I, anchor = CENTER)

world = World()    
    
        


        



class Traffic: 
    def __init__(self, x, y, j, r):
        self.x = x
        self.y = y
        self.j = j
        self.r = r
    def drawTraffic(self, canvas):
        
   
        self.canvas = canvas
        
        self.shape = canvas.create_rectangle(self.x,self.y,self.x+25,self.y+60, fill='black')
        
        self.shape1 = canvas.create_oval(self.x+5,self.y+3,self.x+20,self.y+18,fill='red')
        self.shape2 = canvas.create_oval(self.x+5,self.y+23,self.x+20,self.y+38,fill='orange')
        self.shape3 = canvas.create_oval(self.x+5,self.y+43,self.x+20,self.y+58,fill='gray')

    def light (self):
        
        

   
    
        if t==40*self.j:
                canvas.itemconfig(self.shape1, fill="brown")
                self.r='green'
                canvas.itemconfig(self.shape2, fill="orange")
                canvas.itemconfig(self.shape3, fill="green")
            
                         
        if t==40*(self.j+1):
                        
                canvas.itemconfig(self.shape1, fill="brown")
                self.r='yellow'
                canvas.itemconfig(self.shape2, fill="yellow")                   
                canvas.itemconfig(self.shape3, fill="gray")

        if t==40*(self.j+2):
                        
                canvas.itemconfig(self.shape1, fill="red")
                self.r='red'
                canvas.itemconfig(self.shape2, fill="orange")
                canvas.itemconfig(self.shape3, fill="gray")
                self.j=self.j+3
                

r2d2 = Robot("r2d2" , world, x=random.randint(40, 890), y=random.randint(40, 600),
             I=ImageTk.PhotoImage (file = path+"/Images/r2d2_0.png"), speed = 10.0, score = 0, currentimage=0)
c3po = Robot("c3po", world, x=random.randint(40, 890), y=random.randint(40, 600),
             I=ImageTk.PhotoImage (file = path+"/Images/c3po_0.png"), speed = 10.0, score = 0, currentimage=0)
treasurestealer = StealerRobot("Treasure stealer", world, x=random.randint(20,890), y=random.randint(20,600),
             I=ImageTk.PhotoImage (file = path+"/Images/treasure stealer_0.png"), speed = 10.0, score = 0, currentimage=0)
r2d2.drawRobot(canvas)
c3po.drawRobot(canvas)
treasurestealer.drawRobot(canvas)


traffic1 = Traffic(600, 300, 1, 'red')
traffic1.drawTraffic(canvas)

traffic2 = Traffic(340, 400, 2, 'red')
traffic2.drawTraffic(canvas)

traffic3 = Traffic(100, 200, 3, 'red')
traffic3.drawTraffic(canvas)

landmark = Landmark(110,55, ImageTk.PhotoImage (file = path+"/Images/Image1.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(720,165, ImageTk.PhotoImage (file = path+"/Images/Image2.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(200,395, ImageTk.PhotoImage (file = path+"/Images/Image3.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(210,495, ImageTk.PhotoImage (file = path+"/Images/Image4.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(620,100, ImageTk.PhotoImage (file = path+"/Images/Image5.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(560,445, ImageTk.PhotoImage (file = path+"/Images/Image6.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(310,295, ImageTk.PhotoImage (file = path+"/Images/Image7.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(810,225, ImageTk.PhotoImage (file = path+"/Images/Image8.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(460,345, ImageTk.PhotoImage (file = path+"/Images/Image9.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(410,195, ImageTk.PhotoImage (file = path+"/Images/Image7.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(210,145, ImageTk.PhotoImage (file = path+"/Images/Image7.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

landmark = Landmark(940, 610, ImageTk.PhotoImage (file = path+"/Images/empty.png"))
world.landmarks.append(landmark)
landmark.drawLandmark(canvas)

logo = Logo(805,35, ImageTk.PhotoImage (file = path+"/MyImages/slots.png"))
world.logo.append(logo)
logo.drawLogo(canvas)

def detect (x, y):
        
        if distance(r2d2.x, r2d2.y, landmark.x, landmark.y)< 120:
            r2d2.x = 500
            r2d2.y = 40
            
            
                    
        if distance(c3po.x, c3po.y, landmark.x, landmark.y)<= 120:
            c3po.x = 400
            c3po.y = 600

        if distance(treasurestealer.x, treasurestealer.y, landmark.x, landmark.y)<= 87:
            treasurestealer.x = 440
            treasurestealer.y = 480
            
                  
for landmark in world.landmarks:    
    detect(landmark.x, landmark.y)

t=0

#move robots
while True:
    #loop for the pause button
    while pause == False:
        
                #stop the program if 5 treasures have been found
        #while c3po.score + r2d2.score == 500 :
           # canvas.create_image(0, 0, image = success, anchor = NW)
           # canvas.update()

                 #stop the program after 3 minutes
        while minn == 3:
            canvas.create_image(0, 0, image = time_out, anchor = NW)
            canvas.update()
            
        #update the seconds and minutes
        if t%10==0 and t <> 0:
            sec=sec+1
            labels['text'] = sec
            labels.pack()
        if sec==60:
            sec=0
            labels['text'] = sec
            minn=minn+1
            labelm['text'] = minn
            labels.pack()
            labelm.pack()
            
        #update volume
        v=volume.get()
        volume.pack()
        pygame.mixer.music.set_volume(v/100.0)

        #update stting form checkbox
        check=pop.get()
        
        #move robots
        r2d2.roam()
        c3po.roam()
        treasurestealer.roam()
        
        #stop robots if traffic lights are red        
        if traffic1.r == 'red' or traffic1.r == 'yellow':
                r2d2.speed = 0
        else:
            r2d2.speed = 10.0
        if traffic2.r == 'red' or traffic2.r == 'yellow':
                c3po.speed = 0
        else:
            c3po.speed = 10.0
        if traffic3.r == 'red' or traffic3.r == 'yellow':
            treasurestealer.speed = 0
        else:
            treasurestealer.speed = 10.0

        
        d1 = distance(r2d2.x, r2d2.y, c3po.x, c3po.y)

        if d1 <=50:
            
            r2d2.x -= 2*r2d2._vx
            c3po.x -= 2*c3po._vx
            r2d2.y -= 2*r2d2._vy
            c3po.y -= 2*c3po._vy

        d2 = distance(r2d2.x, r2d2.y, treasurestealer.x, treasurestealer.y)

        if d2 <=30:
            r2d2.x -= 2*r2d2._vx
            treasurestealer.x -= 2*treasurestealer._vx
            r2d2.y -= 2*r2d2._vy
            treasurestealer.y -= 2*treasurestealer._vy

        d3 = distance(c3po.x, c3po.y, treasurestealer.x, treasurestealer.y)

        if d3 <=30:
            c3po.x -= 2*c3po._vx
            treasurestealer.x -= 2*treasurestealer._vx
            c3po.y -= 2*c3po._vy
            treasurestealer.y -= 2*treasurestealer._vy
                      
                 
                  
        traffic1.light()
        traffic2.light()
        traffic3.light()
        
        #update score
        labels1['text'] = r2d2.score
        labels1.pack()
        
        labels2['text'] = c3po.score
        labels2.pack()

        

        #delay animation by 0.1 seconds
        time.sleep(0.1)

        t=t+1

        try:
            probcount1 = float((c3po.regret + 8)-1)
            probcount1=  probcount1 /(c3po.regret +8)
            probcount1 = int(probcount1 * 100)
            if probcount1 >=0:
                labels3['text'] = str(probcount1) + '%' 
                labels3.pack()
            else:
                labels3['text'] = '0%' 
                labels3.pack()
        except(ZeroDivisionError):
            labels3['text'] = '0%' 
            labels3.pack()

        try:
            probcount2 = float((r2d2.regret + 8)-1)
            probcount2=  probcount2 /(r2d2.regret +8)
            probcount2 = int(probcount2 * 100)
            if probcount2 >=0:
                labels4['text'] = str(probcount2) + '%'
                labels4.pack()
            else:
                labels4['text'] = '0%' 
                labels4.pack()
        except(ZeroDivisionError):
            labels4['text'] = '0%' 
            labels4.pack()

    canvas.update()
window.mainloop()   
       
