from dbus import Interface
from dbus import SessionBus

bus=SessionBus()
obj=bus.get_object('com.my_bus', '/com/example/HelloWorld')
interface=Interface(obj, 'com.Example.GetDiskUsage')
interface.disk_space('/tmp')
