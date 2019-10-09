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

        panda1 = {"scale": 0.02,"red": 255,"green": 255,"blue": 0,"walk_speed": 5,"turn_speed": 1,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda2 = {"scale": 0.02,"red": 0,"green": 255,"blue": 255,"walk_speed": 5,"turn_speed": 1,
                  "x_start": 10,"x_end": 10,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda3 = {"scale": 0.02,"red": 255,"green": 0,"blue": 255,"walk_speed": 5,"turn_speed": 1,
                  "x_start": -10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}

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
            self.pandaPace1 = Sequence(pandaPosInterval1_1,
                                      pandaHprInterval1_1,
                                      pandaPosInterval1_2,
                                      pandaHprInterval1_2,
                                      name="pandaPace1")
            self.pandaPace1.loop()

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
            self.pandaPace2 = Sequence(pandaPosInterval2_1,
                                      pandaHprInterval2_1,
                                      pandaPosInterval2_2,
                                      pandaHprInterval2_2,
                                      name="pandaPace2")
            self.pandaPace2.loop()

        def panda_3(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor3 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor3.setScale(scale, scale, scale)
            self.panda_actor3.setColorScale(red, green, blue, 100)
            self.panda_actor3.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor3.loop("walk")
            # Walking animation
            pandaPosInterval3_1 = self.panda_actor3.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval3_2 = self.panda_actor3.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval3_1 = self.panda_actor3.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval3_2 = self.panda_actor3.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace3 = Sequence(pandaPosInterval3_1,
                                      pandaHprInterval3_1,
                                      pandaPosInterval3_2,
                                      pandaHprInterval3_2,
                                      name="pandaPace3")
            self.pandaPace3.loop()

        panda_1(panda1["scale"],panda1["red"],panda1["green"],panda1["blue"],panda1["walk_speed"],panda1["turn_speed"],
                panda1["x_start"],panda1["x_end"],panda1["y_start"],panda1["y_end"],panda1["z_start"],panda1["z_end"])
        panda_2(panda2["scale"],panda2["red"],panda2["green"],panda2["blue"],panda2["walk_speed"],panda2["turn_speed"],
                panda2["x_start"],panda2["x_end"],panda2["y_start"],panda2["y_end"],panda2["z_start"],panda2["z_end"])
        panda_3(panda3["scale"],panda3["red"],panda3["green"],panda3["blue"],panda3["walk_speed"],panda3["turn_speed"],
                panda3["x_start"],panda3["x_end"],panda3["y_start"],panda3["y_end"],panda3["z_start"],panda3["z_end"])

        # Adding sound
        def sound():
            music = base.loader.loadSfx("bensound-dubstep.mp3")
            music.setVolume(0.5)
            music.setLoop(True)
            music.play()

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
