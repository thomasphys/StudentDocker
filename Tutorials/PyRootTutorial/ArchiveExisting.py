import os, datetime

def ArchiveExisting(fname):
    """This function takes a filename (relative or absolute) and checks to see
    if such a file already exists.  If it doesn't, nothing is done.  If a file already
    exists, then it moves the existing file into a directory "old" in the same final
    directory as the file, and appends a timestamp to the filename of the moved file.
    If "old" does not exist, it is created."""
    if not os.path.exists(fname):
        return
    head,tail = os.path.split(fname)
    olddir = os.path.join(head,"old")
    if not os.path.exists(olddir):
        os.mkdir(olddir)
    elif not os.path.isdir(olddir):
        raise RuntimeError("Need to create directory "+
                           olddir+" but file already exists with that name")
    timestamp = datetime.datetime.now().strftime("_%Y%m%d%H%M%S")
    barename,ext = os.path.splitext(tail)
    archivename = os.path.join(olddir,barename+timestamp+ext)
    os.rename(fname,archivename)
    return
