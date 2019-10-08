import random
import time
from math import pi, sin, cos
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Point3

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.5, 0.5, 0.5)
        self.scene.setColor(255, 255, 255, 2)
        self.scene.setPos(-16, 84, 0)

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        panda1 = {"scale": 0.01,"red": 255,"green": 0,"blue": 255,"walk_speed": 1,"turn_speed": 1,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda2 = {"scale": 0.01,"red": 0,"green": 255,"blue": 255,"walk_speed": 5,"turn_speed": 1,
                  "x_start": 5,"x_end": 5,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}

        def panda_1(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor1 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor1.setScale(scale, scale, scale)
            self.panda_actor1.setColorScale(red, green, blue, 100)
            self.panda_actor1.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor1.loop("walk")
            # Walking animation
            pandaPosInterval1_1 = self.panda_actor1.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval1_2 = self.panda_actor1.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval1_1 = self.panda_actor1.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval1_2 = self.panda_actor1.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace = Sequence(pandaPosInterval1_1,
                                      pandaHprInterval1_1,
                                      pandaPosInterval1_2,
                                      pandaHprInterval1_2,
                                      name="pandaPace")
            self.pandaPace.loop()

        def panda_2(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor2 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor2.setScale(scale, scale, scale)
            self.panda_actor2.setColorScale(red, green, blue, 100)
            self.panda_actor2.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor2.loop("walk")
            # Walking animation
            pandaPosInterval2_1 = self.panda_actor2.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval2_2 = self.panda_actor2.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval2_1 = self.panda_actor2.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval2_2 = self.panda_actor2.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace = Sequence(pandaPosInterval2_1,
                                      pandaHprInterval2_1,
                                      pandaPosInterval2_2,
                                      pandaHprInterval2_2,
                                      name="pandaPace")
            self.pandaPace.loop()

        panda_1(panda1["scale"],panda1["red"],panda1["green"],panda1["blue"],panda1["walk_speed"],panda1["turn_speed"],
                panda1["x_start"],panda1["x_end"],panda1["y_start"],panda1["y_end"],panda1["z_start"],panda1["z_end"])
        panda_2(panda2["scale"],panda2["red"],panda2["green"],panda2["blue"],panda2["walk_speed"],panda2["turn_speed"],
                panda2["x_start"],panda2["x_end"],panda2["y_start"],panda2["y_end"],panda2["z_start"],panda2["z_end"])

        # Adding sound
        def sound():
            music = base.loader.loadSfx("bensound-dubstep.mp3")
            music.setVolume(0.5)
            music.setLoop(True)
            music.play()

        sound()

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 48.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(42 * sin(angleRadians), -42.0 * cos(angleRadians), 7)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()
