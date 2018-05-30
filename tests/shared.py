import tempfile, os, shutil
# What was the purpose of this aopen name? It's quite nonstandard.
from anki import Collection as aopen
from anki import Collection
#To make the project PEP8 compliant, import here, not inline.
from anki.collection import _Collection


def assertException(exception, func):
    found = False
    try:
        func()
    except exception:
        found = True
    assert found


# Creating new decks is expensive. Just do it once, and then spin off
# copies from the master.
def getEmptyCol(schedVer=1):
    if len(getEmptyCol.master) == 0:
        (fd, nam) = tempfile.mkstemp(suffix=".anki2")
        os.close(fd)
        os.unlink(nam)
        col = aopen(nam)
        col.db.close()
        getEmptyCol.master = nam
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(getEmptyCol.master, nam)
    _Collection.defaultSchedulerVersion = schedVer
    col = aopen(nam)
    _Collection.defaultSchedulerVersion = 1
    return col

getEmptyCol.master = ""

# Fallback for when the DB needs options passed in.
def getEmptyDeckWith(**kwargs):
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    os.unlink(nam)
    return aopen(nam, **kwargs)

def getUpgradeDeckPath(name="anki12.anki"):
    src = os.path.join(testDir, "support", name)
    (fd, dst) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(src, dst)
    return dst

testDir = os.path.dirname(__file__)


def getFailsWithFalseDeck(schedVer=1):
    print ("For the moment, not really a false-returning deck, just a copy "
           "of the other deck-factory function")
    if len(getEmptyCol.master) == 0:
        (fd, nam) = tempfile.mkstemp(suffix=".anki2")
        os.close(fd)
        os.unlink(nam)
        col = Collection(nam)
        col.db.close()
        getEmptyCol.master = nam
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(getEmptyCol.master, nam)
    _Collection.defaultSchedulerVersion = schedVer
    col = Collection(nam)
    _Collection.defaultSchedulerVersion = 1
    return col

def getFailsWithExceptionDeck(schedVer=1):
    print ("For the moment, not really an exception-creating deck, just a copy "
           "of the other deck-factory function")
    if len(getEmptyCol.master) == 0:
        (fd, nam) = tempfile.mkstemp(suffix=".anki2")
        os.close(fd)
        os.unlink(nam)
        col = Collection(nam)
        col.db.close()
        getEmptyCol.master = nam
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(getEmptyCol.master, nam)
    _Collection.defaultSchedulerVersion = schedVer
    col = Collection(nam)
    _Collection.defaultSchedulerVersion = 1
    return col