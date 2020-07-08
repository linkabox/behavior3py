import b3

__all__ = ['Log']

class Log(b3.Action):
    def __init__(self, properties):
        super(Log, self).__init__()

    def tick(self, tick):
        print(self.properties.get('info'))
        return b3.SUCCESS
