from Tkinter import *
import random
import time
import os, sys
import webbrowser

import math
from math import sqrt, pow
from math import sin, cos, atan2, degrees, radians, pi
import winsound
path = sys.path[0]
from PIL import ImageTk
#setting up the GUI
window = Tk()
#setting up the window title
window.wm_title("Project")

canvas= Canvas(window,width=1000, height=631, bg='light gray')
canvas.pack(expand = YES, fill = BOTH)

      
global move
move=False


#press space to start
def Space(self):
    
    global move
    move = True
       
window.bind('<space>', Space) # space can't be used for anything else

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

bg = ImageTk.PhotoImage(file = path+"/Map_of_Bulgaria.jpg")
canvas.create_image(0, 0, image = bg, anchor = NW)


label1 = Label(text="Red robot score :",font=("Helvetica", 16))
label1.pack(padx=0, pady=0, side=LEFT)

score=0
labels1 = Label(text=score,font=("Helvetica", 20))
labels1.pack(padx=0, pady=0, side=LEFT)

score=0
labels2 = Label(text=score,font=("Helvetica", 20))
labels2.pack(padx=0, pady=0, side=RIGHT)

label2 = Label(text="Blue robot score :",font=("Helvetica", 16))
label2.pack(padx=0, pady=0, side=RIGHT)

gold = ImageTk.PhotoImage(file = path+"/Images/type_11.png")
text1 = ImageTk.PhotoImage(file = path+"/text/text1.png")
text2 = ImageTk.PhotoImage(file = path+"/text/text2.png")
text3 = ImageTk.PhotoImage(file = path+"/text/text3.png")
text4 = ImageTk.PhotoImage(file = path+"/text/text4.png")
text5 = ImageTk.PhotoImage(file = path+"/text/text5.png")
text6 = ImageTk.PhotoImage(file = path+"/text/text6.png")
def angle(x0, y0, x1, y1):
    """ Returns the angle between two points.
    """
    return degrees( atan2(y1-y0, x1-x0) )

def distance(x0, y0, x1, y1):
    """ Returns the distance between two points.
    """
    return sqrt(pow(x1-x0, 2) + pow(y1-y0, 2))

def coordinates(x0, y0, distance, angle):
    """ Returns the coordinates of given distance and angle from a point.
    """
    return (x0 + cos(radians(angle)) * distance,
            y0 + sin(radians(angle)) * distance)

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


class Landmark:
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I
    def drawLandmark(self, canvas):
        self.canvas = canvas
        self.shape = canvas.create_image(self.x, self.y, image = self.I, anchor = CENTER)

global c
c = [1 for j in range(6)]

class Robot:
    
    def __init__(self, world, x, y, I, speed=1.0, score =0):
        
        self.speed = speed
        
        self.x = x 
        self.y = y 
        self.score = score
        self.I = I
        

        self.world = world
        self.feeler_length = 25
        
        self._vx = 0
        self._vy = 0
        
        
    def heading(self):

        """ Returns the robot's heading as angle in degrees.
        """

        return angle(self.x, self.y, self.x+self._vx, self.y+self._vy)
    
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
                    
                    world.landmarks.remove(landmark)
                    landmark = Landmark(landmark.x,landmark.y, ImageTk.PhotoImage (file = path+"/Images/type_11.png"))
                    world.landmarks.append(landmark)
                    landmark.drawLandmark(canvas)
                    canvas.update()

                    winsound.PlaySound(path+"/sound/sound.mp3", winsound.SND_ASYNC)
                    
                    
                    
                    print("Found")
                    self.score +=100
                    
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
                                canvas.create_image(landmark.x, landmark.y, image = text[i], anchor = CENTER)
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
    
        
class StealerRobot:
    
    def __init__(self, world, x, y, I, speed=1.0, score =0):
        
        self.speed = speed
        
        self.x = x 
        self.y = y 
        self.score = score
        self.I = I
        

        self.world = world
        self.feeler_length = 25
        
        self._vx = 0
        self._vy = 0
        
        
    def heading(self):

        """ Returns the robot's heading as angle in degrees.
        """

        return angle(self.x, self.y, self.x+self._vx, self.y+self._vy)
    
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
                    
                    world.landmarks.remove(landmark)
                    landmark = Landmark(landmark.x,landmark.y, ImageTk.PhotoImage (file = path+"/Images/Image7.png"))
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
                                canvas.create_image(landmark.x, landmark.y, image = text[i], anchor = CENTER)
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
                

r2d2 = Robot(world, x=random.randint(40, 890), y=random.randint(40, 600),
             I=ImageTk.PhotoImage (file = path+"/Images/red_robot.png"), speed = 10.0, score = 0)
c3po = Robot(world, x=random.randint(40, 890), y=random.randint(40, 600),
             I=ImageTk.PhotoImage (file = path+"/Images/blue_robot.png"), speed = 10.0, score = 0)
treasurestealer = StealerRobot(world, random.randint(20,890), random.randint(20,600),
             I=ImageTk.PhotoImage (file = path+"/Images/green_robot.png"), speed = 10.0, score = 0) 
                               

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


for t in range(1000):

        
        r2d2.roam()
        
        c3po.roam()

        treasurestealer.roam()
        
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
        d2 = distance(treasurestealer.x, treasurestealer.y, r2d2.x, r2d2.y)

        if d2 <=30:

            treasurestealer.x -= 2*treasurestealer._vx
            r2d2.x -= 2*r2d2._vx
            treasurestealer.y -= 2*treasurestealer._vy
            r2d2.y -= 2*r2d2._vy

        d3 = distance(treasurestealer.x, treasurestealer.y, c3po.x, c3po.y)

        if d3 <=30:

            treasurestealer.x -= 2*r2d2._vx
            c3po.x -= 2*c3po._vx
            treasurestealer.y -= 2*treasurestealer._vy
            c3po.y -= 2*c3po._vy
       
        traffic1.light()
        traffic2.light()
        traffic3.light()

        labels1['text'] = r2d2.score
        labels1.pack()
        
        labels2['text'] = c3po.score
        labels2.pack() 

        time.sleep(0.1)
window.mainloop()   
