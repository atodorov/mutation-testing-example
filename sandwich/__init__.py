class FastFood(object):
    def make_sandwich(self, ham, eggs, mayo):
        return {
            'type' : 'unknown',
            'ham' : ham,
            'eggs': eggs,
            'mayo': mayo,
        }

class Burger(FastFood):
    def make_sandwich(self, ham=1, eggs=None, mayo=True):
        return {
            'type' : 'burger',
            'ham' : ham,
            'eggs': eggs or 0,
            'mayo': mayo,
        }
