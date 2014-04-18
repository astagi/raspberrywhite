import player
from player import Mp3Player, PlayerListener
import time

class Mp3Listener(PlayerListener):
    def __init__(self):
        self.finished = False

    def onPlay(self, source):
        pass

    def onPause(self):
        pass

    def onResume(self):
        pass

    def onStop(self):
        self.finished = True

    def onShutdown(self):
        pass

class TestPlayer():

    def setUp(self):
        self.filename = 'tests/assets/test.mp3'
        self.filename_bad = 'tests/assets/raspiwhite.png'
        self.player = Mp3Player()
        self.listener = Mp3Listener()
        self.player.attachListener(self.listener)

    def tearDown(self):
        self.player.shutdown()

    def test_play_song(self):
        self.player.play(self.filename)
        while self.player.isPlaying():
            pass
        assert self.player.getStatus() == player.STOP

    def test_play_commands(self):
        self.player.play(self.filename)
        time.sleep(6)
        self.player.pause()
        assert self.player.getStatus() == player.PAUSE
        self.player.resume()
        assert self.player.getStatus() == player.PLAY
        while self.player.isPlaying():
            pass
        assert self.player.getStatus() == player.STOP

    def test_bad_file(self):
        self.player.play(self.filename_bad)
        while self.player.isPlaying():
            pass
        assert self.player.getStatus() == player.STOP

    def test_bad_path(self):
        self.player.play('hello/' + self.filename)
        while self.player.isPlaying():
            pass
        assert self.player.getStatus() == player.STOP
