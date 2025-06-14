from .ui import RobotController

rc = RobotController()

try:
    rc.mainloop()
except KeyboardInterrupt:
    rc.destroy()