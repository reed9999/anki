import tempfile, os, shutil
from anki import new_or_existing_collection
#To make the project PEP8 compliant, import here, not inline.
from anki.collection import _Collection
from tests.collection_subclasses import get_collection_from_subclass
from tests.collection_subclasses import CollectionFailsWithFalse

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
        col = new_or_existing_collection(nam)
        col.db.close()
        getEmptyCol.master = nam
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(getEmptyCol.master, nam)
    _Collection.defaultSchedulerVersion = schedVer
    col = new_or_existing_collection(nam)
    _Collection.defaultSchedulerVersion = 1
    return col

getEmptyCol.master = ""

# Fallback for when the DB needs options passed in.
def getEmptyDeckWith(**kwargs):
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    os.close(fd)
    os.unlink(nam)
    return new_or_existing_collection(nam, **kwargs)

def getUpgradeDeckPath(name="anki12.anki"):
    src = os.path.join(testDir, "support", name)
    (fd, dst) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(src, dst)
    return dst

testDir = os.path.dirname(__file__)



def getCollectionFailsWithFalse(schedVer=1):
    """
    Creates a testing collection that we know will fail the sanity check.

    For the moment this is just a replica of getEmptyCol, but eventually it
    would be logical to refactor the commonalities.
    """
    if len(getEmptyCol.master) == 0:
        (fd, nam) = tempfile.mkstemp(suffix=".anki2")
        os.close(fd)
        os.unlink(nam)
        col = new_or_existing_collection(nam)
        col.db.close()
        getEmptyCol.master = nam
    (fd, nam) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(getEmptyCol.master, nam)
    _Collection.defaultSchedulerVersion = schedVer
    col = get_collection_from_subclass(nam, Subclass=CollectionFailsWithFalse)
    _Collection.defaultSchedulerVersion = 1
    return col