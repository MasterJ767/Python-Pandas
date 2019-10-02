#import sys
#import platform

#print("hello")


#print( 1, sys.version )
#print( 2, platform.python_implementation())
#print( 3, sys.executable)

from math import pi, sin, cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # PANDA 1
        def Panda(x,r,g,b,v,u):
            # Load medium-sized panda
            self.pandaActor = Actor("models/panda-model",
                                    {"walk": "models/panda-walk4"})
            self.pandaActor.setScale(0.005, 0.005, 0.005) # medium scale
            self.pandaActor.setColorScale(r, g, b, 100)
            self.pandaActor.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor.loop("walk")
            # Walking animation
            pandaPosInterval1 = self.pandaActor.posInterval(v,
                                                            Point3(x, -10, 5),
                                                            startPos=Point3(x, 10, 5))
            pandaPosInterval2 = self.pandaActor.posInterval(v,
                                                            Point3(x, 10, 5),
                                                            startPos=Point3(x, -10, 5))
            pandaHprInterval1 = self.pandaActor.hprInterval(u,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval2 = self.pandaActor.hprInterval(u,
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
            self.pandaActor2.setColorScale(r, g, b, 100)
            self.pandaActor2.reparentTo(self.render)
            # Leg movement animation
            self.pandaActor2.loop("walk")
            # Walking animation
            pandaPosInterval3 = self.pandaActor2.posInterval(v,
                                                            Point3(x, -10, 7.5),
                                                            startPos=Point3(x, 10, 7.5))
            pandaPosInterval4 = self.pandaActor2.posInterval(v,
                                                            Point3(x, 10, 7.5),
                                                            startPos=Point3(x, -10, 7.5))
            pandaHprInterval3 = self.pandaActor2.hprInterval(u,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval4 = self.pandaActor2.hprInterval(u,
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
            self.pandaActor3.setColorScale(r, g, b, 100)
            self.pandaActor3.reparentTo(self.render)
            # Leg movement animation.
            self.pandaActor3.loop("walk")
            # Walking animation
            pandaPosInterval5 = self.pandaActor3.posInterval(v,
                                                            Point3(x, -10, 0),
                                                            startPos=Point3(x,10, 0))
            pandaPosInterval6 = self.pandaActor3.posInterval(v,
                                                            Point3(x, 10, 0),
                                                            startPos=Point3(x, -10, 0))
            pandaHprInterval5 = self.pandaActor3.hprInterval(u,
                                                            Point3(180, 0, 0),
                                                            startHpr=Point3(0, 0, 0))
            pandaHprInterval6 = self.pandaActor3.hprInterval(u,
                                                            Point3(0, 0, 0),
                                                            startHpr=Point3(180, 0, 0))
            self.pandaPace3 = Sequence(pandaPosInterval5,
                                    pandaHprInterval5,
                                    pandaPosInterval6,
                                    pandaHprInterval6,
                                    name="pandaPace3")
            self.pandaPace3.loop()

        # Panda(x,r,g,b,v,u)
        # x = x co-ordinate
        # r = r value
        # g = g value
        # b = b value
        # v = walking speed
        # u = turning speed

        Panda(0,255,255,0,5,1)
        Panda(5,0,255,255,5,1)
        Panda(-5,255,0,255,5,1)

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 12.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(35 * sin(angleRadians), -35.0 * cos(angleRadians), 7)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()
