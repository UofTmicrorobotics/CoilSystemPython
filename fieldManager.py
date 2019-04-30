# assign pin # to the coil
PIN_X1 = [5, 5.003] # pin number, factor number (mT/V)
PIN_X2 = [1, 4.879]
PIN_Y1 = [2, 5.143]
PIN_Y2 = [6, 5.024]
PIN_Z1 = [3, 5.024]
PIN_Z2 = [7, 4.433]

class FieldManager(object):
    def __init__(self,dac):
        self.x = 0
        self.y = 0
        self.z = 0
        self.dac = dac

    # Uniform field
    def setX(self,mT):
        self.dac.s826_aoPin(PIN_X1[0], mT / PIN_X1[1])
        self.dac.s826_aoPin(PIN_X2[0], mT / PIN_X2[1])
        self.x = mT

    def setY(self,mT):
        self.dac.s826_aoPin(PIN_Y1[0], mT / PIN_Y1[1])
        self.dac.s826_aoPin(PIN_Y2[0], mT / PIN_Y2[1])
        self.y = mT

    def setZ(self,mT):
        self.dac.s826_aoPin(PIN_Z1[0], mT / PIN_Z1[1])
        self.dac.s826_aoPin(PIN_Z2[0], mT / PIN_Z2[1])
        self.z = mT

    def setXYZ(self,x_mT,y_mT,z_mT):
        self.setX(x_mT)
        self.setY(y_mT)
        self.setZ(z_mT)

    # Generate a pulling force by applying current to only one coil
    # mT is a measurement of current in the coil. It has nothing to do with actual field strength.
    def setXGradient(self,mT):
        if mT > 0:
            self.dac.s826_aoPin(PIN_X1[0], mT / PIN_X1[1])
        else:
            self.dac.s826_aoPin(PIN_X2[0], mT / PIN_X2[1])
        self.x = 0

    def setYGradient(self,mT):
        if mT > 0:
            self.dac.s826_aoPin(PIN_Y1[0], mT / PIN_Y1[1])
        else:
            self.dac.s826_aoPin(PIN_Y2[0], mT / PIN_Y2[1])
        self.y = 0

    def setZGradient(self,mT):
        if mT > 0:
            self.dac.s826_aoPin(PIN_Z1[0], mT / PIN_Z1[1])
        else:
            self.dac.s826_aoPin(PIN_Z2[0], mT / PIN_Z2[1])
        self.z = 0
