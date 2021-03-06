import django
import player
from player import Mp3Player, PlayerListener
import time

class Mp3Listener(PlayerListener):
    def __init__(self):
        self.steps = {
            'play' : 0,
            'pause' : 0,
            'resume' : 0,
            'stop' : 0,
            'shutdown' : 0
        }

    def onPlay(self, source):
        self.steps['play'] += 1

    def onPause(self):
        self.steps['pause'] += 1

    def onResume(self):
        self.steps['resume'] += 1

    def onStop(self):
        self.steps['stop'] += 1

    def onShutdown(self):
        self.steps['shutdown'] += 1

class TestPlayerListener(django.test.TestCase):

    def setUp(self):
        self.filename = 'player/tests/assets/test.mp3'
        self.filename_bad = 'player/tests/assets/raspiwhite.png'
        self.player = Mp3Player()
        self.listener = Mp3Listener()
        self.player.attachListener(self.listener)

    def tearDown(self):
        pass

    def test_listener(self):
        pass
