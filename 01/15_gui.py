# python -m pip install pyglet
import pyglet
window = pyglet.window.Window()

def process_text(char): # gets the character that was pressed
    print(char)
    had.y += 10


def tik(t): # gets precise elapsed time since last call
    # print(t)
    had.x += 10
    had.rotation += 10 # °

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    # tlacitko je leve,prave,prostredni, mod je normal,ctrl,shift,alt...

pyglet.clock.schedule_interval(tik, 0.5) # interval with one second

had_file = pyglet.image.load('01/had.png')
had = pyglet.sprite.Sprite(had_file)

def draw_had():
    window.clear()
    had.draw()

window.push_handlers(
    on_text=process_text,
    on_draw=draw_had,
    on_mouse_press=klik,
)
pyglet.app.run() # synchronous run, this initializes the app event loop implemented by pyglet
print('Thank you for using our aplication!') # executes after app is closed
