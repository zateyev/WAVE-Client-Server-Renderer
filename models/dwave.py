from ctypes import cdll, c_float
lib = cdll.LoadLibrary('./libDwave.so')

class Dwave(object):
    def __init__(self):
        self.obj = lib.Dwave_new()

    def run(self):
        lib.Dwave_start(self.obj)

    def set_cam_settings(self, px, py, pz, ux, uy, uz):
        lib.Dwave_set_cam_settings(self.obj, px, py, pz, ux, uy, uz)

    def set_scene_size(self, width, height):
        lib.Dwave_set_scene_size(self.obj, width, height)

    def set_geometry(self, xmin, xmax, ymin, ymax, zmin, zmax):
        lib.Dwave_set_geometry(self.obj, xmin, xmax, ymin, ymax, zmin, zmax)
