

import re
import glob
import os

for name in glob.glob('./**', recursive = True):

    parts = name.split("/")

    lastPart = parts[-1]

    pattern = re.compile("\d{4}-\d{2}-\d{2}-.*\.md")

    match = re.search(pattern, lastPart)
    if match:

        pathName = "/".join(parts[:-1])# + "/"
        print(pathName)


        splitName = lastPart[11:]
        print(pathName + splitName)
        dstName = os.path.join(pathName, splitName)
        print("renaming", name, "to", dstName)

        try:
            os.rename(name, dstName)
        except OSError as e:
            print("exists already, removing", name)
            os.remove(name)




