from holon.Blackboard import Blackboard
from holon.HolonicAgent import HolonicAgent
from holon.Blackboard import Blackboard
from holon.HolonicDesire import HolonicDesire
from holon.HolonicIntention import HolonicIntention

if __name__ == '__main__':
    b = Blackboard()
    d = HolonicDesire()
    i = HolonicIntention()
    a = HolonicAgent(b, d, i)
    a.start()
