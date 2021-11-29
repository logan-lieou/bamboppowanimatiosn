from manim import *

config.background_color = WHITE

class ModelOutput(Scene):
   def construct(self):
      # objects
      group = VGroup(Dot(2 * UP, color=BLACK), Dot(UP, color=BLACK), Dot(ORIGIN, color=BLACK),
                     Dot(DOWN, color=BLACK), Dot(2 * DOWN, color=BLACK)).scale(1.5)
      modelG = VGroup(Dot(DOWN+2*RIGHT, color=BLACK), Dot(UP+2*RIGHT, color=BLACK)).scale(1.5)
      sRG = SurroundingRectangle(modelG[1], color=RED)
      resText = Text("('NORMAL', 0.997)", color=BLACK, font="Noto Sans").scale(0.5)
      rAR = Arrow(end=modelG[1].get_center(), start=[0, 0.2, 0], color=BLACK)
      img = ImageMobject("brain.jpg")
      rect = Rectangle(width=img.width, height=img.height, color=BLACK)
      rect = rect.set_fill(BLACK, opacity=1)
      rect = rect.shift(2*LEFT)
      group = VGroup(Dot(2 * UP, color=BLACK), Dot(UP, color=BLACK), Dot(ORIGIN, color=BLACK),
                     Dot(DOWN, color=BLACK), Dot(2 * DOWN, color=BLACK)).scale(1.5)

      # data processing animation
      self.add(img)
      self.wait()
      self.play(img.animate.shift(2*LEFT))
      self.play(Create(rect))
      self.remove(img)
      self.play(Transform(rect, group))
      self.wait()
      self.remove(rect, group)

      # model output animation
      self.play(Transform(group, modelG))
      self.play(Create(sRG))
      self.wait()
      self.play(Uncreate(sRG))
      self.play(Create(resText))
      self.play(Create(rAR))
      self.wait()

