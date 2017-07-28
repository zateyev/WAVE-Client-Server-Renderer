from ctypes import cdll, c_float
lib = cdll.LoadLibrary('./libDwave.so')

class Dwave(object):
    def __init__(self):
        self.obj = lib.Dwave_new()

    def run(self):
        lib.Dwave_start(self.obj)

    # def set_quat(self, x, y, z, angle):
    #     lib.Dwave_set_quat(self.obj, x, y, z, angle)

    def set_quat(self, px, py, pz, ux, uy, uz):
        lib.Dwave_set_quat(self.obj, px, py, pz, ux, uy, uz)

# f = Dwave()
# f.set_quat(c_float(0.41003194468231546), c_float(0.14182406485987478), c_float(-0.90097710235425), c_float(0.00390625))
# f.run()
