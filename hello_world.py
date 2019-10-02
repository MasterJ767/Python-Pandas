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

        # PANDA 1 - Tiny Panda
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.0005, 0.0005, 0.0005)
        self.pandaActor.setColorScale(0, 25, 25, 5)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterval1 = self.pandaActor.posInterval(13,
                                                        Point3(0, -10, 0),
                                                        startPos=Point3(0, 10, 0))
        pandaPosInterval2 = self.pandaActor.posInterval(13,
                                                        Point3(0, 10, 0),
                                                        startPos=Point3(0, -10, 0))
        pandaHprInterval1 = self.pandaActor.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
        pandaHprInterval2 = self.pandaActor.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1,
                                  pandaHprInterval1,
                                  pandaPosInterval2,
                                  pandaHprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()

        # PANDA 2 - Medium-sized Panda
        # Load and transform the panda actor.
        self.pandaActor2 = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor2.setScale(0.005, 0.005, 0.005)
        self.pandaActor2.setColorScale(25, 0, 0, 5)
        self.pandaActor2.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor2.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterva21 = self.pandaActor2.posInterval(13,
                                                        Point3(0, -10, 0),
                                                        startPos=Point3(0, 10, 0))
        pandaPosInterva22 = self.pandaActor2.posInterval(13,
                                                        Point3(0, 10, 0),
                                                        startPos=Point3(0, -10, 0))
        pandaHprInterva21 = self.pandaActor2.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
        pandaHprInterva22 = self.pandaActor2.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace2 = Sequence(pandaPosInterva21,
                                  pandaHprInterva21,
                                  pandaPosInterva22,
                                  pandaHprInterva22,
                                  name="pandaPace2")
        self.pandaPace2.loop()

        # PANDA 3 - Big Panda
        # Load and transform the panda actor.
        self.pandaActor3 = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor3.setScale(0.05, 0.05, 0.05)
        self.pandaActor3.setColorScale(25, 25, 0, 5)
        self.pandaActor3.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor3.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterva31 = self.pandaActor3.posInterval(13,
                                                         Point3(0, -10, 0),
                                                         startPos=Point3(0, 10,0))
        pandaPosInterva32 = self.pandaActor2.posInterval(13,
                                                         Point3(0, 10, 0),
                                                         startPos=Point3(0, -10, 0))
        pandaHprInterva31 = self.pandaActor2.hprInterval(3,
                                                         Point3(180, 0, 0),
                                                         startHpr=Point3(0, 0, 0))
        pandaHprInterva32 = self.pandaActor2.hprInterval(3,
                                                         Point3(0, 0, 0),
                                                         startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace3 = Sequence(pandaPosInterva31,
                                  pandaHprInterva31,
                                  pandaPosInterva32,
                                  pandaHprInterva32,
                                  name="pandaPace3")
        self.pandaPace3.loop()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()
