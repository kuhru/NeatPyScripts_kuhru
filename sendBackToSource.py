import os
import shutil

lox = "C:\\Users\\userNameWowie\\Desktop\\welop\\extra"

lfile = []
for r, d, f in os.walk(lox):
    for file in f:
        lfile.append(file)
print(len(lfile))
c = 0
for x in range(len(lfile)):
    try:
        nloc = lfile[x][lfile[x].index("(") + 1:lfile[x].index(")")].replace("!", "\\").replace(",", ":")
        nname = lfile[x][:lfile[x].index("(") - 1] + lfile[x][lfile[x].index(")") + 1:]
        shutil.move(os.path.join(lox, lfile[x]), os.path.join(nloc, nname))
    except:
        print("Failed to move: " + nname + " to " + nloc)
    else:
        c = c + 1
print("Successfully moved " + c + " files")
