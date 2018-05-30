import anki
from anki.collection import _Collection
from anki.storage import new_or_existing_collection

class CollectionFailsWithFalse(_Collection):
    # Let's try this the naive way....
    def __init__(self, name):
        super(name)

    def basicCheck(self):
        return False

class CollectionFailsWithException(_Collection):
    def basicCheck(self):
        raise "Intentional failure to test exception handling"
