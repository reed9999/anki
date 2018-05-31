import os
import anki
from anki.collection import _Collection
from anki.storage import _upgradeSchema
from anki.db import DB
from anki.consts import SCHEMA_VERSION


class CollectionFailsWithFalse(_Collection):
    # Let's try this the naive way....
    def basicCheck(self):
        return False

class CollectionFailsWithException(_Collection):
    def basicCheck(self):
        raise "Intentional failure to test exception handling"


def get_collection_from_subclass(path, lock=True, server=False, sync=True,
                                 log=False, Subclass=_Collection):
    "Open a new or existing collection. Path must be unicode."
    assert path.endswith(".anki2")
    path = os.path.abspath(path)
    create = not os.path.exists(path)
    if create:
        base = os.path.basename(path)
        for c in ("/", ":", "\\"):
            assert c not in base
    # connect
    db = DB(path)
    db.setAutocommit(True)
    if create:
        ver = _createDB(db)
    else:
        ver = _upgradeSchema(db)
    db.execute("pragma temp_store = memory")
    if sync:
        db.execute("pragma cache_size = 10000")
        db.execute("pragma journal_mode = wal")
    else:
        db.execute("pragma synchronous = off")
    db.setAutocommit(False)
    # add db to col and do any remaining upgrades
    col = Subclass(db, server, log)
    if ver < SCHEMA_VERSION:
        _upgrade(col, ver)
    elif ver > SCHEMA_VERSION:
        raise Exception("This file requires a newer version of Anki.")
    elif create:
        # add in reverse order so basic is default
        addClozeModel(col)
        addBasicTypingModel(col)
        addForwardOptionalReverse(col)
        addForwardReverse(col)
        addBasicModel(col)
        col.save()
    if lock:
        col.lock()
    return col
