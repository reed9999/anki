import anki
from anki.collection import _Collection
from anki.storage import Collection as CollectionContainer

class CollectionFailsWithFalse(CollectionContainer(u'xxx.anki2')):
    # Let's try this the naive way....
    def __init__(self, name):
        super(name)

    def basicCheck(self):
        return False

class CollectionFailsWithException(_Collection):
    def basicCheck(self):
        raise "Intentional failure to test exception handling"
