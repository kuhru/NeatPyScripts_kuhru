import os
import shutil
import time

"""
This script is for finding 'same name' images (that's what im using it for)
though it certainly can be modified easily to do the same for other files
or all files of the same name.
"""

lfile = []
# list for storing filenames without file extensions
locfile = []
# list of storing filelocations to be manipulated later
repfileloc = []
# list later used to collect all the duplicate files which are discovered
lox = "C:\\Users\\userNameWowie\\Desktop\\welop\\extra"
# this is the export location, and thus for convenience is not included in the countable search


def counter(loc):
    """
    used to find all relevant files and paths in locations, and storing each in a list
    """
    for r, d, f in os.walk(loc):
        if r != lox:
            for file in f:
                if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".jpeg"):
                    lfile.append(file[:len(file) - 4])
                    locfile.append(os.path.join(r, file))


def merge(l, m, p, q, r):
    """
    This is a somewhat specialized mergesort, sorting 2 lists based on 1 list.
    """
    n1 = q - p + 1
    n2 = r - q
    left = l[p: p + n1]
    left2 = m[p: p + n1]
    right = l[q + 1: q + 1 + n2]
    right2 = m[q + 1: q + 1 + n2]

    i = 0
    j = 0
    k = p
    while k < r + 1:
        if i == n1:
            l[k] = right[j]
            m[k] = right2[j]
            j += 1
        elif j == n2:
            l[k] = left[i]
            m[k] = left2[i]
            i += 1
        elif left[i] <= right[j]:
            l[k] = left[i]
            m[k] = left2[i]
            i += 1
        else:
            l[k] = right[j]
            m[k] = right2[j]
            j += 1
        k += 1


def _merge_sort(l, m, p, r):
    if p < r:
        q = int((p + r) / 2)
        _merge_sort(l, m, p, q)
        _merge_sort(l, m, q + 1, r)
        merge(l, m, p, q, r)


def merge_sort(l, m):
    """
    l is the fileList, m is the fileLocationList
    """
    _merge_sort(l, m, 0, len(l) - 1)


def tally():
    """
    a basic function to check for same filebasenames in the list, and if found
    to add them to the repfileloc list, to be processed further
    """
    for x in range(len(locfile)):
        if locfile[x] in repfileloc:
            break
            # if the file already exists in the replacement list, then immediately break
        chk = len(repfileloc)
        # useful to make sure that the next loop actually added anything to the replacement list
        for y in range(x + 1, len(locfile)):
            if lfile[x] == lfile[y]:
                repfileloc.append(locfile[y])
            elif lfile[x] != lfile[y]:
                # as soon as the filenames are different, it just breaks
                break
        if len(repfileloc) > chk and locfile[x] not in repfileloc:
            # hence if files were added, then obviously the one which was being used to compare to rest is also required in the list.
            repfileloc.append(locfile[x])


counter("C:\\Users\\userNameWowie\\Desktop\\welop")
print("1st location is being counted")
# all subfolders in imagestorage 1 will be included
counter("Y:\\Either\\images")
print("2nd location is being counted")
# if you had folders elsewhere, keep copying the counter(location) as many times as you need. however don't overlap
# the subfolders or the locations will be counted twice and that'll generate an error in program.

# that's the two locations i have, you do yours for as many locations as you have

startTime = time.perf_counter()
merge_sort(lfile, locfile)
print("\n--- sorting time: \t\t\t\t\t%s seconds ---" % (time.perf_counter() - startTime))

startTime = time.perf_counter()
tally()
print("--- duplicate discovery time: \t\t%s seconds ---" % (time.perf_counter() - startTime))

# now that the replacement list is created and finalised, this is where the move happens.
print("\nTotal files found: " + str(len(lfile)) + "\nTotal duplicates found: " + str(len(repfileloc)))

if len(repfileloc) != 0:
    print("Commencing Move")
while len(repfileloc) != 0:
    loxx = repfileloc.pop()
    loxn = os.path.basename(loxx)
    flox = loxn[:len(loxn) - 4] + " (" + loxx[:len(loxx) - len(loxn) -1].replace("\\", "!").replace(":", ",") + ")" + loxn[len(loxn) - 4:]
    # flox in the new name in the form of 'filename (location with ! and , instead of \ and :).ext'
    try:
        shutil.move(loxx, os.path.join(lox, flox))
    except:
        print(loxx)
        print(os.path.join(lox, flox))
    else:
        None
