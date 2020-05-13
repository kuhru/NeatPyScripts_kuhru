# NeatPyScripts_kuhru
Just random pieces of code I use on a regular basis to make my life easier. This selection will be in python. These are all mostly personalized codes, because I work with over 10,000 images and eyeballing it isn't exactly feasible. 

# About imgOpenBrowser:
Primarily a code for opening a batch of images in tabs of browser (chrome).

If you ever need to compare 2 images on the difference by eyeballing which is more appealing, as in the color saturation, exposure and so on. This can't necessarily be left to A.I., and opening in the default windows image viewer is doesn't have the same benefits as opening in chrome, essentially that multiple tabs of images while preserving the zoom state of all is allowed in chrome, so you can go back and forth to see the differences exactly.

This piece of code is more useful as a batch image processor, since just one or two images can be manually dragged to chrome, but once you're dealing with more than a hundred, it does get tedious very fast.

# About findNameDuplicates:
Primarily a code for finding duplicate filenames in different directories/paths.

Immensely useful if you use pixiv, yande.re, danbooru etc very actively and have a rigid naming system, but don’t exactly have enough mental memory to keep over 1000s of images in mind such that you’re not repeat downloading an image.

Runtime of over 10000 files without any duplicates is sub 1 second, so I do believe its sufficiently fast and efficient.
!! Make sure, you edit the variable 'lox' and the parameter of 'Counter' is correct for your usecase. !!
