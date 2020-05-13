# NeatPyScripts_kuhru
Just random pieces of code that I use on a regular basis to make my life easier. This selection will be in python. These are all mostly personalized codes, because I work with over 10,000 images and managing those by hand and eyeballs isn't exactly always feasible. These aren't necessarily interconnected, however some can be used in conjunction.

# About imgOpenBrowser:
Primarily a code for opening batches of images in tabs of a browser (chrome, in this instance).

If you've ever needed to compare 2 similar images which have been processed differently, on the differences they have, its really not that easy and Windows' default image handling software isn't exactly the most effective way to do such a thing. This can't necessarily be left to A.I. since the most important thing to me was personal appeal.

Benefits of using chrome is that multiple tabs of images can be simultaneously opened, and hence I can quickly move back and forth between multiple images while preserving the zoom state of all and catch the differences exactly.

This piece of code is more useful as a batch image processor, since just one or two images can be manually dragged to chrome, but once you're dealing with more than a hundred, it does get tedious very fast.

# About findNameDuplicates:
Primarily a code for finding duplicate filenames.

Immensely useful if you use pixiv, yande.re, danbooru etc. very actively and have a rigid naming system, but don’t exactly have enough mental memory to keep over 1000s of images in mind such that you’re not repeat downloading an image.

Runtime of over 10000 files without any duplicates is sub 1 second, so I do believe its sufficiently fast and efficient.

!! Make sure, you edit the variable 'lox' and the parameter of 'Counter' is correct for your usecase !!
!! Use it with sendBackToSource.py !!

# About sendBackToSource:
Primarily used in conjunction with findNameDuplicates.py. After running that script, files will be transfered to your desired directory 'lox', and after that to send them back to where they came from, this script is quick and handy. 

That's all this script does, just reverts the actions of findNameDuplicates.py.
