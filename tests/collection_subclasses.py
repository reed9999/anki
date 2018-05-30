from anki import Collection as aopen
from anki.collection import _Collection


class CollectionFailsWithFalse(aopen):
    # Let's try this the naive way....
    def basicCheck(self):
        return False

class CollectionFailsWithException(_Collection):
    def basicCheck(self):
        raise "Intentional failure to test exception handling"
