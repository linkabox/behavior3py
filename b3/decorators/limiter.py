import b3

__all__ = ['Limiter']

class Limiter(b3.Decorator):
    def __init__(self, properties):
        super(Limiter, self).__init__()

        self.properties = properties
        self.max_loop = properties.get('maxLoop', 1)

    # def open(self, tick):
    #     tick.blackboard.set('i', 0, tick.tree.id, self.id)

    def tick(self, tick):
        if not self.child:
            return b3.ERROR

        i = tick.blackboard.get('i', tick.tree.id, self.id, 0)
        if i < self.max_loop:
            print("Limiter:", i)
            status = self.child._execute(tick)

            if status == b3.SUCCESS or status == b3.FAILURE:
                tick.blackboard.set('i', i+1, tick.tree.id, self.id)

            return status

        return b3.FAILURE
        
