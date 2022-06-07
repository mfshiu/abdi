from core.Agent import Agent
from holon.Blackboard import Blackboard
from holon.HolonicDesire import HolonicDesire
from holon.HolonicIntention import HolonicIntention

class HolonicAgent(Agent) :
    def __init__(self, b:Blackboard=None, d:HolonicDesire=None, i: HolonicIntention=None):
        b = b or Blackboard()
        d = d or HolonicDesire()
        i = i or HolonicIntention()
        super().__init__(b, d, i)
        self.head_agents = []
        self.body_agents = []
        
    def start(self):
        for a in self.head_agents:
            print(f"head: {a.__module__} start")
            a.start()
        for a in self.body_agents:
            print(f"body: {a.__module__} start")
            a.start()
        



