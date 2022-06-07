from holon.HolonicAgent import HolonicAgent
from guide.voice.Speaker import Speaker
from guide.voice.ToneProcessing import ToneProcessing

class Voice(HolonicAgent) :
    def __init__(self):
        super().__init__()
        self.head_agents.append(Speaker())
        self.body_agents.append(ToneProcessing())
