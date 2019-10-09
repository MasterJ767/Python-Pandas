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

        # Setting the Panda Parameters
        panda1 = {"scale": 0.02,"red": 255,"green": 0,"blue": 255,"walk_speed": 5,"turn_speed": 1,
                  "x_start": -10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda2 = {"scale": 0.02,"red": 255,"green": 255,"blue": 0,"walk_speed": 2.5,"turn_speed": 0.5,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda3 = {"scale": 0.02,"red": 0,"green": 255,"blue": 255,"walk_speed": 1.25,"turn_speed": 0.25,
                  "x_start": 10,"x_end": 10,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 0}
        panda4 = {"scale": 0.01,"red": 0,"green": 0,"blue": 255,"walk_speed": 1.25,"turn_speed": 0.25,
                  "x_start": -10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 10,"z_end": 10}
        panda5 = {"scale": 0.01,"red": 255,"green": 0,"blue": 0,"walk_speed": 5,"turn_speed": 1,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 10,"z_end": 10}
        panda6 = {"scale": 0.01,"red": 0,"green": 255,"blue": 0,"walk_speed": 2.5,"turn_speed": 0.5,
                  "x_start": 10,"x_end": 10,"y_start": 10,"y_end": -10,"z_start": 10,"z_end": 10}
        panda7 = {"scale": 0.005,"red": 0,"green": 255,"blue": 255,"walk_speed": 2.5,"turn_speed": 0.5,
                  "x_start": -10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 15,"z_end": 15}
        panda8 = {"scale": 0.005,"red": 255,"green": 0,"blue": 255,"walk_speed": 1.25,"turn_speed": 0.25,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 15,"z_end": 15}
        panda9 = {"scale": 0.005,"red": 255,"green": 255,"blue": 0,"walk_speed": 5,"turn_speed": 1,
                  "x_start": 10,"x_end": 10,"y_start": 10,"y_end": -10,"z_start": 15,"z_end": 15}
        panda10 = {"scale": 0.0025,"red": 0,"green": 255,"blue": 0,"walk_speed": 5,"turn_speed": 1,
                  "x_start": -10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 17.5,"z_end": 17.5}
        panda11 = {"scale": 0.0025,"red": 0,"green": 0,"blue": 255,"walk_speed": 2.5,"turn_speed": 0.5,
                  "x_start": 0,"x_end": 0,"y_start": 10,"y_end": -10,"z_start": 17.5,"z_end": 17.5}
        panda12 = {"scale": 0.0025,"red": 255,"green": 0,"blue": 0,"walk_speed": 1.25,"turn_speed": 0.25,
                  "x_start": 10,"x_end": 10,"y_start": 10,"y_end": -10,"z_start": 17.5,"z_end": 17.5}
        panda13 = {"scale": 0.00125,"red": 255,"green": 255,"blue": 255,"walk_speed": 0.625,"turn_speed": 0.125,
                  "x_start": 10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 18.75,"z_end": 0}
        panda14 = {"scale": 0.00125,"red": 255,"green": 255,"blue": 255,"walk_speed": 0.625,"turn_speed": 0.125,
                  "x_start": -10,"x_end": 10,"y_start": -10,"y_end": 10,"z_start": 18.75,"z_end": 0}
        panda15 = {"scale": 0.00125,"red": 255,"green": 255,"blue": 255,"walk_speed": 0.625,"turn_speed": 0.125,
                  "x_start": 10,"x_end": -10,"y_start": 10,"y_end": -10,"z_start": 0,"z_end": 18.75}
        panda16 = {"scale": 0.00125,"red": 255,"green": 255,"blue": 255,"walk_speed": 0.625,"turn_speed": 0.125,
                  "x_start": -10,"x_end": 10,"y_start": -10,"y_end": 10,"z_start": 0,"z_end": 18.75}

        # Defining each Panda as a unique function
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

        def panda_4(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor4 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor4.setScale(scale, scale, scale)
            self.panda_actor4.setColorScale(red, green, blue, 100)
            self.panda_actor4.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor4.loop("walk")
            # Walking animation
            pandaPosInterval4_1 = self.panda_actor4.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval4_2 = self.panda_actor4.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval4_1 = self.panda_actor4.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval4_2 = self.panda_actor4.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace4 = Sequence(pandaPosInterval4_1,
                                      pandaHprInterval4_1,
                                      pandaPosInterval4_2,
                                      pandaHprInterval4_2,
                                      name="pandaPace4")
            self.pandaPace4.loop()

        def panda_5(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor5 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor5.setScale(scale, scale, scale)
            self.panda_actor5.setColorScale(red, green, blue, 100)
            self.panda_actor5.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor5.loop("walk")
            # Walking animation
            pandaPosInterval5_1 = self.panda_actor5.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval5_2 = self.panda_actor5.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval5_1 = self.panda_actor5.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval5_2 = self.panda_actor5.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace5 = Sequence(pandaPosInterval5_1,
                                      pandaHprInterval5_1,
                                      pandaPosInterval5_2,
                                      pandaHprInterval5_2,
                                      name="pandaPace5")
            self.pandaPace5.loop()

        def panda_6(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor6 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor6.setScale(scale, scale, scale)
            self.panda_actor6.setColorScale(red, green, blue, 100)
            self.panda_actor6.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor6.loop("walk")
            # Walking animation
            pandaPosInterval6_1 = self.panda_actor6.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval6_2 = self.panda_actor6.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval6_1 = self.panda_actor6.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval6_2 = self.panda_actor6.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace6 = Sequence(pandaPosInterval6_1,
                                      pandaHprInterval6_1,
                                      pandaPosInterval6_2,
                                      pandaHprInterval6_2,
                                      name="pandaPace6")
            self.pandaPace6.loop()

        def panda_7(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor7 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor7.setScale(scale, scale, scale)
            self.panda_actor7.setColorScale(red, green, blue, 100)
            self.panda_actor7.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor7.loop("walk")
            # Walking animation
            pandaPosInterval7_1 = self.panda_actor7.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval7_2 = self.panda_actor7.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval7_1 = self.panda_actor7.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval7_2 = self.panda_actor7.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace7 = Sequence(pandaPosInterval7_1,
                                      pandaHprInterval7_1,
                                      pandaPosInterval7_2,
                                      pandaHprInterval7_2,
                                      name="pandaPace7")
            self.pandaPace7.loop()

        def panda_8(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor8 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor8.setScale(scale, scale, scale)
            self.panda_actor8.setColorScale(red, green, blue, 100)
            self.panda_actor8.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor8.loop("walk")
            # Walking animation
            pandaPosInterval8_1 = self.panda_actor8.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval8_2 = self.panda_actor8.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval8_1 = self.panda_actor8.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval8_2 = self.panda_actor8.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace8 = Sequence(pandaPosInterval8_1,
                                      pandaHprInterval8_1,
                                      pandaPosInterval8_2,
                                      pandaHprInterval8_2,
                                      name="pandaPace8")
            self.pandaPace8.loop()

        def panda_9(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor9 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor9.setScale(scale, scale, scale)
            self.panda_actor9.setColorScale(red, green, blue, 100)
            self.panda_actor9.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor9.loop("walk")
            # Walking animation
            pandaPosInterval9_1 = self.panda_actor9.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval9_2 = self.panda_actor9.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval9_1 = self.panda_actor9.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval9_2 = self.panda_actor9.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace9 = Sequence(pandaPosInterval9_1,
                                      pandaHprInterval9_1,
                                      pandaPosInterval9_2,
                                      pandaHprInterval9_2,
                                      name="pandaPace9")
            self.pandaPace9.loop()

        def panda_10(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor10 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor10.setScale(scale, scale, scale)
            self.panda_actor10.setColorScale(red, green, blue, 100)
            self.panda_actor10.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor10.loop("walk")
            # Walking animation
            pandaPosInterval10_1 = self.panda_actor10.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval10_2 = self.panda_actor10.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval10_1 = self.panda_actor10.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval10_2 = self.panda_actor10.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace10 = Sequence(pandaPosInterval10_1,
                                      pandaHprInterval10_1,
                                      pandaPosInterval10_2,
                                      pandaHprInterval10_2,
                                      name="pandaPace10")
            self.pandaPace10.loop()

        def panda_11(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor11 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor11.setScale(scale, scale, scale)
            self.panda_actor11.setColorScale(red, green, blue, 100)
            self.panda_actor11.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor11.loop("walk")
            # Walking animation
            pandaPosInterval11_1 = self.panda_actor11.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval11_2 = self.panda_actor11.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval11_1 = self.panda_actor11.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval11_2 = self.panda_actor11.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace11 = Sequence(pandaPosInterval11_1,
                                      pandaHprInterval11_1,
                                      pandaPosInterval11_2,
                                      pandaHprInterval11_2,
                                      name="pandaPace11")
            self.pandaPace11.loop()

        def panda_12(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor12 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor12.setScale(scale, scale, scale)
            self.panda_actor12.setColorScale(red, green, blue, 100)
            self.panda_actor12.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor12.loop("walk")
            # Walking animation
            pandaPosInterval12_1 = self.panda_actor12.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval12_2 = self.panda_actor12.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_end, z_end))
            pandaHprInterval12_1 = self.panda_actor12.hprInterval(turn_speed,
                                                                Point3(180, 0, 0),
                                                                startHpr=Point3(0, 0, 0))
            pandaHprInterval12_2 = self.panda_actor12.hprInterval(turn_speed,
                                                                Point3(0, 0, 0),
                                                                startHpr=Point3(180, 0, 0))
            self.pandaPace12 = Sequence(pandaPosInterval12_1,
                                      pandaHprInterval12_1,
                                      pandaPosInterval12_2,
                                      pandaHprInterval12_2,
                                      name="pandaPace12")
            self.pandaPace12.loop()

        def panda_13(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor13 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor13.setScale(scale, scale, scale)
            self.panda_actor13.setColorScale(red, green, blue, 100)
            self.panda_actor13.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor13.loop("walk")
            # Walking animation
            pandaPosInterval13_1 = self.panda_actor13.posInterval(walk_speed,
                                                                Point3(x_start, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval13_2 = self.panda_actor13.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_start),
                                                                startPos=Point3(x_start, y_end, z_end))
            pandaPosInterval13_3 = self.panda_actor13.posInterval(walk_speed,
                                                                Point3(x_end, y_start, z_end),
                                                                startPos=Point3(x_end, y_end, z_start))
            pandaPosInterval13_4 = self.panda_actor13.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_start, z_end))
            pandaHprInterval13_1 = self.panda_actor13.hprInterval(turn_speed,
                                                                Point3(-90, 0, 0),
                                                                startHpr=Point3(-360, 0, 0))
            pandaHprInterval13_2 = self.panda_actor13.hprInterval(turn_speed,
                                                                Point3(-180, 0, 0),
                                                                startHpr=Point3(-90, 0, 0))
            pandaHprInterval13_3 = self.panda_actor13.hprInterval(turn_speed,
                                                                Point3(-270, 0, 0),
                                                                startHpr=Point3(-180, 0, 0))
            pandaHprInterval13_4 = self.panda_actor13.hprInterval(turn_speed,
                                                                Point3(-360, 0, 0),
                                                                startHpr=Point3(-270, 0, 0))
            self.pandaPace13 = Sequence(pandaPosInterval13_1,
                                      pandaHprInterval13_1,
                                      pandaPosInterval13_2,
                                      pandaHprInterval13_2,
                                      pandaPosInterval13_3,
                                      pandaHprInterval13_3,
                                      pandaPosInterval13_4,
                                      pandaHprInterval13_4,
                                      name="pandaPace13")
            self.pandaPace13.loop()

        def panda_14(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor14 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor14.setScale(scale, scale, scale)
            self.panda_actor14.setColorScale(red, green, blue, 100)
            self.panda_actor14.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor14.loop("walk")
            # Walking animation
            pandaPosInterval14_1 = self.panda_actor14.posInterval(walk_speed,
                                                                Point3(x_start, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval14_2 = self.panda_actor14.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_start),
                                                                startPos=Point3(x_start, y_end, z_end))
            pandaPosInterval14_3 = self.panda_actor14.posInterval(walk_speed,
                                                                Point3(x_end, y_start, z_end),
                                                                startPos=Point3(x_end, y_end, z_start))
            pandaPosInterval14_4 = self.panda_actor14.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_start, z_end))
            pandaHprInterval14_1 = self.panda_actor14.hprInterval(turn_speed,
                                                                Point3(-270, 0, 0),
                                                                startHpr=Point3(-180, 0, 0))
            pandaHprInterval14_2 = self.panda_actor14.hprInterval(turn_speed,
                                                                Point3(-360, 0, 0),
                                                                startHpr=Point3(-270, 0, 0))
            pandaHprInterval14_3 = self.panda_actor14.hprInterval(turn_speed,
                                                                Point3(-90, 0, 0),
                                                                startHpr=Point3(-360, 0, 0))
            pandaHprInterval14_4 = self.panda_actor14.hprInterval(turn_speed,
                                                                Point3(-180, 0, 0),
                                                                startHpr=Point3(-90, 0, 0))
            self.pandaPace14 = Sequence(pandaPosInterval14_1,
                                      pandaHprInterval14_1,
                                      pandaPosInterval14_2,
                                      pandaHprInterval14_2,
                                      pandaPosInterval14_3,
                                      pandaHprInterval14_3,
                                      pandaPosInterval14_4,
                                      pandaHprInterval14_4,
                                      name="pandaPace14")
            self.pandaPace14.loop()

        def panda_15(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor15 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor15.setScale(scale, scale, scale)
            self.panda_actor15.setColorScale(red, green, blue, 100)
            self.panda_actor15.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor15.loop("walk")
            # Walking animation
            pandaPosInterval15_1 = self.panda_actor15.posInterval(walk_speed,
                                                                Point3(x_start, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval15_2 = self.panda_actor15.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_start),
                                                                startPos=Point3(x_start, y_end, z_end))
            pandaPosInterval15_3 = self.panda_actor15.posInterval(walk_speed,
                                                                Point3(x_end, y_start, z_end),
                                                                startPos=Point3(x_end, y_end, z_start))
            pandaPosInterval15_4 = self.panda_actor15.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_start, z_end))
            pandaHprInterval15_1 = self.panda_actor15.hprInterval(turn_speed,
                                                                Point3(-90, 0, 0),
                                                                startHpr=Point3(-360, 0, 0))
            pandaHprInterval15_2 = self.panda_actor15.hprInterval(turn_speed,
                                                                Point3(-180, 0, 0),
                                                                startHpr=Point3(-90, 0, 0))
            pandaHprInterval15_3 = self.panda_actor15.hprInterval(turn_speed,
                                                                Point3(-270, 0, 0),
                                                                startHpr=Point3(-180, 0, 0))
            pandaHprInterval15_4 = self.panda_actor15.hprInterval(turn_speed,
                                                                Point3(-360, 0, 0),
                                                                startHpr=Point3(-270, 0, 0))
            self.pandaPace15 = Sequence(pandaPosInterval15_1,
                                      pandaHprInterval15_1,
                                      pandaPosInterval15_2,
                                      pandaHprInterval15_2,
                                      pandaPosInterval15_3,
                                      pandaHprInterval15_3,
                                      pandaPosInterval15_4,
                                      pandaHprInterval15_4,
                                      name="pandaPace15")
            self.pandaPace15.loop()

        def panda_16(scale, red, green, blue, walk_speed, turn_speed, x_start, x_end, y_start, y_end, z_start, z_end):
            self.panda_actor16 = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
            self.panda_actor16.setScale(scale, scale, scale)
            self.panda_actor16.setColorScale(red, green, blue, 100)
            self.panda_actor16.reparentTo(self.render)
            # Leg movement animation
            self.panda_actor16.loop("walk")
            # Walking animation
            pandaPosInterval16_1 = self.panda_actor16.posInterval(walk_speed,
                                                                Point3(x_start, y_end, z_end),
                                                                startPos=Point3(x_start, y_start, z_start))
            pandaPosInterval16_2 = self.panda_actor16.posInterval(walk_speed,
                                                                Point3(x_end, y_end, z_start),
                                                                startPos=Point3(x_start, y_end, z_end))
            pandaPosInterval16_3 = self.panda_actor16.posInterval(walk_speed,
                                                                Point3(x_end, y_start, z_end),
                                                                startPos=Point3(x_end, y_end, z_start))
            pandaPosInterval16_4 = self.panda_actor16.posInterval(walk_speed,
                                                                Point3(x_start, y_start, z_start),
                                                                startPos=Point3(x_end, y_start, z_end))
            pandaHprInterval16_1 = self.panda_actor16.hprInterval(turn_speed,
                                                                Point3(-270, 0, 0),
                                                                startHpr=Point3(-180, 0, 0))
            pandaHprInterval16_2 = self.panda_actor16.hprInterval(turn_speed,
                                                                Point3(-360, 0, 0),
                                                                startHpr=Point3(-270, 0, 0))
            pandaHprInterval16_3 = self.panda_actor16.hprInterval(turn_speed,
                                                                Point3(-90, 0, 0),
                                                                startHpr=Point3(-360, 0, 0))
            pandaHprInterval16_4 = self.panda_actor16.hprInterval(turn_speed,
                                                                Point3(-180, 0, 0),
                                                                startHpr=Point3(-90, 0, 0))
            self.pandaPace16 = Sequence(pandaPosInterval16_1,
                                      pandaHprInterval16_1,
                                      pandaPosInterval16_2,
                                      pandaHprInterval16_2,
                                      pandaPosInterval16_3,
                                      pandaHprInterval16_3,
                                      pandaPosInterval16_4,
                                      pandaHprInterval16_4,
                                      name="pandaPace16")
            self.pandaPace16.loop()

        # Calling each Panda function with the parameters set in the dictionaries at the top
        panda_1(panda1["scale"],panda1["red"],panda1["green"],panda1["blue"],panda1["walk_speed"],panda1["turn_speed"],
                panda1["x_start"],panda1["x_end"],panda1["y_start"],panda1["y_end"],panda1["z_start"],panda1["z_end"])
        panda_2(panda2["scale"],panda2["red"],panda2["green"],panda2["blue"],panda2["walk_speed"],panda2["turn_speed"],
                panda2["x_start"],panda2["x_end"],panda2["y_start"],panda2["y_end"],panda2["z_start"],panda2["z_end"])
        panda_3(panda3["scale"],panda3["red"],panda3["green"],panda3["blue"],panda3["walk_speed"],panda3["turn_speed"],
                panda3["x_start"],panda3["x_end"],panda3["y_start"],panda3["y_end"],panda3["z_start"],panda3["z_end"])
        panda_4(panda4["scale"],panda4["red"],panda4["green"],panda4["blue"],panda4["walk_speed"],panda4["turn_speed"],
                panda4["x_start"],panda4["x_end"],panda4["y_start"],panda4["y_end"],panda4["z_start"],panda4["z_end"])
        panda_5(panda5["scale"],panda5["red"],panda5["green"],panda5["blue"],panda5["walk_speed"],panda5["turn_speed"],
                panda5["x_start"],panda5["x_end"],panda5["y_start"],panda5["y_end"],panda5["z_start"],panda5["z_end"])
        panda_6(panda6["scale"],panda6["red"],panda6["green"],panda6["blue"],panda6["walk_speed"],panda6["turn_speed"],
                panda6["x_start"],panda6["x_end"],panda6["y_start"],panda6["y_end"],panda6["z_start"],panda6["z_end"])
        panda_7(panda7["scale"],panda7["red"],panda7["green"],panda7["blue"],panda7["walk_speed"],panda7["turn_speed"],
                panda7["x_start"],panda7["x_end"],panda7["y_start"],panda7["y_end"],panda7["z_start"],panda7["z_end"])
        panda_8(panda8["scale"],panda8["red"],panda8["green"],panda8["blue"],panda8["walk_speed"],panda8["turn_speed"],
                panda8["x_start"],panda8["x_end"],panda8["y_start"],panda8["y_end"],panda8["z_start"],panda8["z_end"])
        panda_9(panda9["scale"],panda9["red"],panda9["green"],panda9["blue"],panda9["walk_speed"],panda9["turn_speed"],
                panda9["x_start"],panda9["x_end"],panda9["y_start"],panda9["y_end"],panda9["z_start"],panda9["z_end"])
        panda_10(panda10["scale"],panda10["red"],panda10["green"],panda10["blue"],panda10["walk_speed"],panda10["turn_speed"],
                panda10["x_start"],panda10["x_end"],panda10["y_start"],panda10["y_end"],panda10["z_start"],panda10["z_end"])
        panda_11(panda11["scale"],panda11["red"],panda11["green"],panda11["blue"],panda11["walk_speed"],panda11["turn_speed"],
                panda11["x_start"],panda11["x_end"],panda11["y_start"],panda11["y_end"],panda11["z_start"],panda11["z_end"])
        panda_12(panda12["scale"],panda12["red"],panda12["green"],panda12["blue"],panda12["walk_speed"],panda12["turn_speed"],
                panda12["x_start"],panda12["x_end"],panda12["y_start"],panda12["y_end"],panda12["z_start"],panda12["z_end"])
        panda_13(panda13["scale"],panda13["red"],panda13["green"],panda13["blue"],panda13["walk_speed"],panda13["turn_speed"],
                panda13["x_start"],panda13["x_end"],panda13["y_start"],panda13["y_end"],panda13["z_start"],panda13["z_end"])
        panda_14(panda14["scale"],panda14["red"],panda14["green"],panda14["blue"],panda14["walk_speed"],panda14["turn_speed"],
                panda14["x_start"],panda14["x_end"],panda14["y_start"],panda14["y_end"],panda14["z_start"],panda14["z_end"])
        panda_15(panda15["scale"],panda15["red"],panda15["green"],panda15["blue"],panda15["walk_speed"],panda15["turn_speed"],
                panda15["x_start"],panda15["x_end"],panda15["y_start"],panda15["y_end"],panda15["z_start"],panda15["z_end"])
        panda_16(panda16["scale"],panda16["red"],panda16["green"],panda16["blue"],panda16["walk_speed"],panda16["turn_speed"],
                panda16["x_start"],panda16["x_end"],panda16["y_start"],panda16["y_end"],panda16["z_start"],panda16["z_end"])

        # Adding sound
        def sound():
            music = self.loader.loadSfx("bensound-dubstep.mp3")
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
        angleDegrees = task.time * 64.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(64 * sin(angleRadians), -64.0 * cos(angleRadians), 32)
        self.camera.setHpr(angleDegrees, -16, 0)
        return Task.cont

app = MyApp()
app.run()
