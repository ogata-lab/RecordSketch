from Tkinter import *
import ctypes

class tabletWindow(Frame):
    def __init__(self, width=700, height=500, master=None):
        Frame.__init__(self, master)
        print "create window."
        self.tablet = ctypes.cdll.LoadLibrary('./libTabletLibC.so')

        self.tablet.get_point_x.restype = ctypes.c_longlong
        self.tablet.get_point_y.restype = ctypes.c_longlong
        self.tablet.get_point_z.restype = ctypes.c_longlong
        self.tablet.get_buttons.restype = ctypes.c_longlong
    
        self.tablet.get_tilt_x.restype = ctypes.c_double
        self.tablet.get_tilt_y.restype = ctypes.c_double
        self.tablet.get_rotation.restype = ctypes.c_double
        self.tablet.get_pressure.restype = ctypes.c_double
        self.tablet.get_tangent_pressure.restype = ctypes.c_double

        self.tablet.get_vendor1.restype = ctypes.c_longlong
        self.tablet.get_vendor2.restype = ctypes.c_longlong
        self.tablet.get_vendor3.restype = ctypes.c_longlong
        self.tablet.get_vendor_id.restype = ctypes.c_longlong
        self.tablet.get_tablet_id.restype = ctypes.c_longlong
        self.tablet.get_pointer_id.restype = ctypes.c_longlong
        self.tablet.get_device_id.restype = ctypes.c_longlong
        self.tablet.get_system_tablet_id.restype = ctypes.c_longlong
        self.tablet.get_vendor_pointer_type.restype = ctypes.c_longlong
        self.tablet.get_vendor_pointer_serial_number.restype = ctypes.c_longlong
        self.tablet.get_vendor_unique_id.restype = ctypes.c_longlong
        self.tablet.get_capability_mask.restype = ctypes.c_longlong
        self.tablet.get_pointer_type.restype = ctypes.c_longlong
        self.tablet.get_enter_proximity.restype = ctypes.c_longlong
        
        if self.tablet.init() == 0:
            print "init tablet success."
        else:
            print "init tablet failed."

        #canvas
        self.c0 = Canvas(self, width = '700', height = '600')
        self.c0.grid(row = 0, column = 0, columnspan = 3)
        
        #labels
        self.la_x = Label(self, text = "position X", bd = 2)
        self.la_x.grid(row = 1, column = 0)

        self.la_y = Label(self, text = "position Y", bd = 2)
        self.la_y.grid(row = 1, column = 1)
        
        self.la_p = Label(self, text = "pressure", bd = 2)
        self.la_p.grid(row = 1, column = 2)

        self.grid()

    def setLabel(self,state, x, y, p):
        if state:
            self.la_x.configure(text = "position X: %d" % x)
            self.la_y.configure(text = "position Y: %d" % y)
            self.la_p.configure(text = "pressure: %f" % p)

        else:
            self.la_x.configure(text = "no tablet data")
            self.la_y.configure(text = "mo tablet data")
            self.la_p.configure(text = "no tablet data")

    def m_frame(self):
        m_x = 0
        m_y = 0
        m_p = 0.
        m_state = True

        try:
            m_x = self.tablet.get_point_x()
            m_y = self.tablet.get_point_y()
            m_p = self.tablet.get_pressure()
        except:
            m_state = False

        self.setLabel(m_state, m_x, m_y, m_p)

        return m_state,m_x,m_y,m_p

    def exit(self):
        self.master.destroy()
