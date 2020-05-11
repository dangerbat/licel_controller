import licel_controller.settings
from licel_controller.interface import Controller

# override settings
licel_controller.settings.HOST = "localhost"
licel_controller.settings.PORT = 2055

if __name__ == '__main__':
    c = Controller()
    c.select(2, 3, 5)
    c.pmtgain(2, 980)
    c.mstart()
    c.mstop()
    c.run()
