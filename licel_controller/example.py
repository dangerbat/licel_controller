from licel_controller.interface import Controller

if __name__ == '__main__':
    c = Controller()
    c.select(2, 3, 5)
    c.pmtgain(2, 980)
    c.mstart()
    c.mstop()
    c.run()
