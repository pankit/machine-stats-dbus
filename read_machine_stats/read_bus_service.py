from collections import namedtuple

import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import os

DiskUsage = namedtuple('usage', 'total used free')


class Example(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('com.my_bus', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/example/HelloWorld')

    @dbus.service.method('com.Example.GetDiskUsage', in_signature='s', out_signature='a{sx}')
    def disk_space(self, path):
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        used = (st.f_blocks - st.f_bfree) * st.f_frsize
        return {
            'total': total,
            'used': used,
            'free': free
        }

    @dbus.service.method('com.example.HelloWorld.SayHello')
    def say_hello(self):
        return 'hello world'


DBusGMainLoop(set_as_default=True)

example_obj = Example()

try:
    GLib.MainLoop().run()
except KeyboardInterrupt:
    print("\nThe MainLoop will close...")
    GLib.MainLoop().quit()
