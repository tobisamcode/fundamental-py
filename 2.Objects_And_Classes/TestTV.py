class TV:
    def __init__(self):
        self.channel = 1 # Default channel is 1
        self.volumeLevel = 1 # Default volume is 1
        self.on = False # Initially, TV is off

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.off = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolumeLevel(self, volumeLevel):
        if self.on and 1 <= self.volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.volumeLevel > 1:
            self.volumeLevel -= 1



def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolumeLevel(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()
    tv2.volumeUp()
    tv2.volumeUp()
    tv2.volumeUp()
    tv2.volumeUp()


    print("tv1's channel is", tv1.getChannel(), 'and volume level is', tv1.getVolumeLevel())
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolumeLevel())

main()
