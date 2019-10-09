#import sys
#import platform

#print("hello")


#print( 1, sys.version )
#print( 2, platform.python_implementation())
#print( 3, sys.executable)

import random
import time
from math import pi, sin, cos
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3, TextNode

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setColor(255, 0, 0, 2)
        self.scene.setPos(-16, 84, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # PANDA FUNCTION
        def panda1(x,r1,g1,b1,r2,g2,b2,r3,g3,b3,v1,v2,v3,u1,u2,u3):
            # Load medium-sized panda
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005) # medium scale
            self.pandaActor.setColorScale(r2, g2, b2, 100)
            self.pandaActor.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor.loop("walk")
            # Walking animation
            pandaPosInterval1 = self.pandaActor.posInterval(v2,
                                                            Point3(x, -10, 5),
                                                            startPos=Point3(x, 10, 5))
            pandaPosInterval2 = self.pandaActor.posInterval(v2,
                                                            Point3(x, 10, 5),
                                                            startPos=Point3(x, -10, 5))
            pandaHprInterval1 = self.pandaActor.hprInterval(u2,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor.hprInterval(u2,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace = Sequence(pandaPosInterval1,
                                      pandaHprInterval1,
                                      pandaPosInterval2,
                                      pandaHprInterval2,
                                      name="pandaPace")
            self.pandaPace.loop()

            # Load small panda
            self.pandaActor2 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor2.setScale(0.0025, 0.0025, 0.0025) # small scale
            self.pandaActor2.setColorScale(r1, g1, b1, 100)
            self.pandaActor2.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor2.loop("walk")
            # Walking animation
            pandaPosInterval3 = self.pandaActor2.posInterval(v1,
                                                            Point3(x, -10, 0),
                                                            startPos=Point3(x, 10, 7.5))
            pandaPosInterval4 = self.pandaActor2.posInterval(v1,
                                                            Point3(x, 10, 7.5),
                                                            startPos=Point3(x, -10, 0))
            pandaHprInterval3 = self.pandaActor2.hprInterval(u1,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval4 = self.pandaActor2.hprInterval(u1,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace2 = Sequence(pandaPosInterval3,
                                    pandaHprInterval3,
                                    pandaPosInterval4,
                                    pandaHprInterval4,
                                    name="pandaPace2")
            self.pandaPace2.loop()

            # Load big panda
            self.pandaActor3 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor3.setScale(0.01, 0.01, 0.01) # large scale
            self.pandaActor3.setColorScale(r3, g3, b3, 1)
            self.pandaActor3.reparentTo(self.render)
            # Leg movement animation.
            self.pandaActor3.loop("walk")
            # Walking animation
            pandaPosInterval5 = self.pandaActor3.posInterval(v3,
                                                            Point3(x, -10, 7.5),
                                                            startPos=Point3(x,10, 0))
            pandaPosInterval6 = self.pandaActor3.posInterval(v3,
                                                            Point3(x, 10, 0),
                                                            startPos=Point3(x, -10, 7.5))
            pandaHprInterval5 = self.pandaActor3.hprInterval(u3,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval6 = self.pandaActor3.hprInterval(u3,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace3 = Sequence(pandaPosInterval5,
                                    pandaHprInterval5,
                                    pandaPosInterval6,
                                    pandaHprInterval6,
                                    name="pandaPace3")
            self.pandaPace3.loop()

        # PANDA FUNCTION 2
        def panda2(x,r1,g1,b1,r2,g2,b2,r3,g3,b3,v1,v2,v3,u1,u2,u3):
            # Load medium-sized panda
            self.pandaActor4 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor4.setScale(0.005, 0.005, 0.005) # medium scale
            self.pandaActor4.setColorScale(r2, g2, b2, 100)
            self.pandaActor4.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor4.loop("walk")
            # Walking animation
            pandaPosInterval1 = self.pandaActor4.posInterval(v2,
                                                            Point3(x, -10, 5),
                                                            startPos=Point3(x, 10, 5))
            pandaPosInterval2 = self.pandaActor4.posInterval(v2,
                                                            Point3(x, 10, 5),
                                                            startPos=Point3(x, -10, 5))
            pandaHprInterval1 = self.pandaActor4.hprInterval(u2,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor4.hprInterval(u2,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace4 = Sequence(pandaPosInterval1,
                                      pandaHprInterval1,
                                      pandaPosInterval2,
                                      pandaHprInterval2,
                                      name="pandaPace4")
            self.pandaPace4.loop()

            # Load small panda
            self.pandaActor5 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor5.setScale(0.0025, 0.0025, 0.0025) # small scale
            self.pandaActor5.setColorScale(r1, g1, b1, 100)
            self.pandaActor5.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor5.loop("walk")
            # Walking animation
            pandaPosInterval3 = self.pandaActor5.posInterval(v1,
                                                            Point3(x, -10, 0),
                                                            startPos=Point3(x, 10, 7.5))
            pandaPosInterval4 = self.pandaActor5.posInterval(v1,
                                                            Point3(x, 10, 7.5),
                                                            startPos=Point3(x, -10, 0))
            pandaHprInterval3 = self.pandaActor5.hprInterval(u1,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval4 = self.pandaActor5.hprInterval(u1,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace5 = Sequence(pandaPosInterval3,
                                    pandaHprInterval3,
                                    pandaPosInterval4,
                                    pandaHprInterval4,
                                    name="pandaPace5")
            self.pandaPace5.loop()

            # Load big panda
            self.pandaActor6 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor6.setScale(0.01, 0.01, 0.01) # large scale
            self.pandaActor6.setColorScale(r3, g3, b3, 1)
            self.pandaActor6.reparentTo(self.render)
            # Leg movement animation.
            self.pandaActor6.loop("walk")
            # Walking animation
            pandaPosInterval5 = self.pandaActor6.posInterval(v3,
                                                            Point3(x, -10, 7.5),
                                                            startPos=Point3(x,10, 0))
            pandaPosInterval6 = self.pandaActor6.posInterval(v3,
                                                            Point3(x, 10, 0),
                                                            startPos=Point3(x, -10, 7.5))
            pandaHprInterval5 = self.pandaActor6.hprInterval(u3,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval6 = self.pandaActor6.hprInterval(u3,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace6 = Sequence(pandaPosInterval5,
                                    pandaHprInterval5,
                                    pandaPosInterval6,
                                    pandaHprInterval6,
                                    name="pandaPace6")
            self.pandaPace6.loop()

        # PANDA FUNCTION 3
        def panda3(x,r1,g1,b1,r2,g2,b2,r3,g3,b3,v1,v2,v3,u1,u2,u3):
            # Load medium-sized panda
            self.pandaActor7 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor7.setScale(0.005, 0.005, 0.005) # medium scale
            self.pandaActor7.setColorScale(r2, g2, b2, 100)
            self.pandaActor7.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor7.loop("walk")
            # Walking animation
            pandaPosInterval1 = self.pandaActor7.posInterval(v2,
                                                            Point3(x, -10, 5),
                                                            startPos=Point3(x, 10, 5))
            pandaPosInterval2 = self.pandaActor7.posInterval(v2,
                                                            Point3(x, 10, 5),
                                                            startPos=Point3(x, -10, 5))
            pandaHprInterval1 = self.pandaActor7.hprInterval(u2,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor7.hprInterval(u2,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace7 = Sequence(pandaPosInterval1,
                                      pandaHprInterval1,
                                      pandaPosInterval2,
                                      pandaHprInterval2,
                                      name="pandaPace7")
            self.pandaPace7.loop()

            # Load small panda
            self.pandaActor8 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor8.setScale(0.0025, 0.0025, 0.0025) # small scale
            self.pandaActor8.setColorScale(r1, g1, b1, 100)
            self.pandaActor8.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor8.loop("walk")
            # Walking animation
            pandaPosInterval3 = self.pandaActor8.posInterval(v1,
                                                            Point3(x, -10, 0),
                                                            startPos=Point3(x, 10, 7.5))
            pandaPosInterval4 = self.pandaActor8.posInterval(v1,
                                                            Point3(x, 10, 7.5),
                                                            startPos=Point3(x, -10, 0))
            pandaHprInterval3 = self.pandaActor8.hprInterval(u1,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval4 = self.pandaActor8.hprInterval(u1,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace8 = Sequence(pandaPosInterval3,
                                    pandaHprInterval3,
                                    pandaPosInterval4,
                                    pandaHprInterval4,
                                    name="pandaPace8")
            self.pandaPace8.loop()

            # Load big panda
            self.pandaActor9 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor9.setScale(0.01, 0.01, 0.01) # large scale
            self.pandaActor9.setColorScale(r3, g3, b3, 1)
            self.pandaActor9.reparentTo(self.render)
            # Leg movement animation.
            self.pandaActor9.loop("walk")
            # Walking animation
            pandaPosInterval5 = self.pandaActor9.posInterval(v3,
                                                            Point3(x, -10, 7.5),
                                                            startPos=Point3(x,10, 0))
            pandaPosInterval6 = self.pandaActor9.posInterval(v3,
                                                            Point3(x, 10, 0),
                                                            startPos=Point3(x, -10, 7.5))
            pandaHprInterval5 = self.pandaActor9.hprInterval(u3,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval6 = self.pandaActor9.hprInterval(u3,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace9 = Sequence(pandaPosInterval5,
                                    pandaHprInterval5,
                                    pandaPosInterval6,
                                    pandaHprInterval6,
                                    name="pandaPace9")
            self.pandaPace9.loop()

        def panda4(x1,y1,x2,y2,r,g,b,v,u):
            # Load medium-sized panda
            self.pandaActor10 = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor10.setScale(0.005, 0.005, 0.005) # medium scale
            self.pandaActor10.setColorScale(r, g, b, 100)
            self.pandaActor10.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor10.loop("walk")
            # Walking animation
            pandaPosInterval1 = self.pandaActor10.posInterval(v,
                                                            Point3(x1, y2, 0),
                                                            startPos=Point3(x1, y1, 7.5))
            pandaPosInterval2 = self.pandaActor10.posInterval(v,
                                                            Point3(x2, y2, 7.5),
                                                            startPos=Point3(x1, y2, 0))
            pandaPosInterval3 = self.pandaActor10.posInterval(v,
                                                            Point3(x2, y1, 0),
                                                            startPos=Point3(x2, y2, 7.5))
            pandaPosInterval4 = self.pandaActor10.posInterval(v,
                                                            Point3(x1, y1, 7.5),
                                                            startPos=Point3(-x2, y1, 0))
            pandaHprInterval1 = self.pandaActor10.hprInterval(u,
                                                            Point3(-90, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor10.hprInterval(u,
                                                            Point3(-180, 0, 0),
                                                            startHpr=Point3(-90, 0, 0))
            pandaHprInterval3 = self.pandaActor10.hprInterval(u,
                                                            Point3(-270, 0, 0),
                                                            startHpr=Point3(-180, 0, 0))
            pandaHprInterval4 = self.pandaActor10.hprInterval(u,
                                                            Point3(-360, 0, 0),
                                                            startHpr=Point3(-270, 0, 0))
            self.pandaPace10 = Sequence(pandaPosInterval1,
                                      pandaHprInterval1,
                                      pandaPosInterval2,
                                      pandaHprInterval2,
                                      pandaPosInterval3,
                                      pandaHprInterval3,
                                      pandaPosInterval4,
                                      pandaHprInterval4,
                                      name="pandaPace10")
            self.pandaPace10.loop()

        # panda_(x,r1,g1,b1,r2,g2,b2,r3,g3,b3,v1,v2,v3,u1,u2,u3)
        # x = x co-ordinate
        # r1 = r value for small panda
        # g1 = g value for small panda
        # b1 = b value for small panda
        # r2 = r value for medium panda
        # b2 = b value for medium panda
        # g2 = g value for medium panda
        # r3 = r value for large panda
        # g3 = g value for large panda
        # b3 = b value for large panda
        # v1 = walking speed for small panda
        # v2 = walking speed for medium panda
        # v3 = walking speed for large panda
        # u1 = turning speed for small panda
        # u2 = turning speed for medium panda
        # u3 = turning speed for large panda

        # Allows for easy control of certain variable in the panda generation
        panda1(0,0,255,0,255,255,0,255,0,0,5,2.5,1.25,1,0.5,0.25)
        panda2(5,255,0,0,255,0,255,0,0,255,1.25,5,2.5,0.25,1,0.5)
        panda3(-5,0,0,255,0,255,255,0,255,0,2.5,1.25,5,0.5,0.25,1)
        panda4(5,10,-5,-10,255,255,255,5,1)

        # Adding sound
        def sound():
            # Generates a random float between 0 and 1, rounded to 1 decimal place
            ###vol = round(random.uniform(0, 1), 1)
            music = base.loader.loadSfx("bensound-dubstep.mp3")
            music.setVolume(0.5)
            music.setLoop(True)
            music.play()
            # Uses a while loop with an unachievable condition so it lasts forever
            ###while vol < 1.01:
                # Sets the volume of the music to random float
                #music.setVolume(vol)
                # Waits for the volume of the music multiplied by 60 seconds to determine how long the music plays at that volume for
                ###time.sleep(vol * 60)
                # Regenerating the number
                ###vol = round(random.uniform(0, 1), 1)

        sound()

        # Adding text
        def text():
            font = loader.loadFont('cmr12.egg')
            text1 = TextNode('node name')
            text1.setText("Pande")
            text1.setFont(font)
            text1.setSmallCaps(True)
            text1.setSlant(-0.3)
            text1.setTextColor(0, 0, 0, 1)
            text1.setShadow(0.05, 0.05)
            text1.setShadowColor(1, 0, 0, 1)
            text1.setAlign(TextNode.ARight)
            text2 = TextNode('node name')
            text2.setText("monium")
            text2.setFont(font)
            text2.setSmallCaps(True)
            text2.setSlant(0.3)
            text2.setTextColor(0, 0, 0, 1)
            text2.setShadow(0.05, 0.05)
            text2.setShadowColor(1, 0, 0, 1)
            text2.setAlign(TextNode.ALeft)
            textNodePath = aspect2d.attachNewNode(text1)
            textNodePath.setScale(0.3)
            textNodePath = aspect2d.attachNewNode(text2)
            textNodePath.setScale(0.3)

        text()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 48.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(42 * sin(angleRadians), -42.0 * cos(angleRadians), 7)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()
