from manim import *

class BubbleSort(Scene):
    def construct(self):

        # create squares that resemble array elements
        s1 = Square()
        value1 = Text('1')
        gr1 = VGroup(s1, value1)

        s2 = Square()
        value2 = Text('2')
        gr2 = VGroup(s2, value2)

        s3 = Square()
        value3 = Text('3')
        gr3 = VGroup(s3, value3)

        s4 = Square()
        value4 = Text('4')
        gr4 = VGroup(s4, value4)

        s5 = Square()
        value5 = Text('5')
        gr5 = VGroup(s5, value5)

        group = VGroup(gr1, gr2, gr3, gr4, gr5).set_x(0).arrange(buff=0.2)
        self.play(Write(group), run_time = 3)
        self.wait()

        #new order: 54231
        self.play(Swap(gr5, gr1), run_time = 1)
        self.wait()

        self.play(Swap(gr4, gr2), run_time = 1)
        self.wait()

        self.play(Swap(gr2, gr3), run_time = 1)
        self.wait()

        #sort, 1st iteration
        self.play(s5.animate.set_fill(BLUE, opacity=0.5))
        self.play(s4.animate.set_fill(BLUE, opacity=0.5))

        self.play(s5.animate.set_fill(RED, opacity=0.5))
        self.play(s4.animate.set_fill(RED, opacity=0.5))

        self.play(Swap(gr5, gr4), run_time = 2)

        self.play(s4.animate.set_fill(BLUE, opacity=0.5))
        self.play(s5.animate.set_fill(BLUE, opacity=0.5))

        self.play(s4.animate.set_fill(BLUE, opacity=0))
        self.play(s2.animate.set_fill(BLUE, opacity=0.5))

        self.play(s5.animate.set_fill(RED, opacity=0.5))
        self.play(s2.animate.set_fill(RED, opacity=0.5))

        self.play(Swap(gr5, gr2), run_time=2)

        self.play(s5.animate.set_fill(BLUE, opacity=0.5))
        self.play(s2.animate.set_fill(BLUE, opacity=0.5))

        self.play(s2.animate.set_fill(BLUE, opacity=0))
        self.play(s3.animate.set_fill(BLUE, opacity=0.5))

        self.play(s5.animate.set_fill(RED, opacity=0.5))
        self.play(s3.animate.set_fill(RED, opacity=0.5))

        self.play(Swap(gr5, gr3), run_time=2)

        self.play(s5.animate.set_fill(BLUE, opacity=0.5))
        self.play(s3.animate.set_fill(BLUE, opacity=0.5))

        self.play(s3.animate.set_fill(BLUE, opacity=0))
        self.play(s1.animate.set_fill(BLUE, opacity=0.5))

        self.play(s5.animate.set_fill(RED, opacity=0.5))
        self.play(s1.animate.set_fill(RED, opacity=0.5))

        self.play(Swap(gr5, gr1), run_time=2)

        self.play(s5.animate.set_fill(GREEN, opacity=0.5))
        self.play(s1.animate.set_fill(BLUE, opacity=0))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('hi')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
