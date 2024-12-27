
import pprint
import os
from rmcl import Item, Document, Folder, invalidate_cache_s
import trio

# Script to move PDFs to Remarkable while preserving the directory structure

pp = pprint.PrettyPrinter(indent=4)
relative_path = "/Users/xxxxxxx/Desktop"
#papers_dir = "papers/discretization"
papers_dir = "papers"
abs_dir = os.path.join(relative_path,papers_dir)

TRASH_ID = 'trash'

# clear cache
invalidate_cache_s()

async def list_files():
    root = await Item.get_by_id('')  # The root folder has ID of empty string
    for child in root.children:

        if isinstance(child, Folder):
            print(f"folder: {child.name}")
            pp.pprint(child.__dict__)
            #if child.name in ['foo', 'testpath', 'SynologyDrive', 'papers']:
            #    print("child recognized")
            #    await child.delete()

        elif isinstance(child, Document):  # The only other possibility
            print(f"{await child.type()}: {child.name}")
            print(child.id)
            pp.pprint(child.__dict__)

            # move item to trash by updating metadata
            #child.parent = TRASH_ID
            #await child.update_metadata()

            await child.delete()

async def list_dir(folder):
    root = await Folder.get_by_id(folder.id)
    parentName = root.name
    sub_dirs = []

    print(f"{parentName}: ")
   
    for child in root.children:

        if isinstance(child, Folder):
            #parentItem = await Item.get_by_id(child.parent)
            #parentName = parentItem.name
            sub_dirs.append(child)
            #print(f" {child.name}/")
            print(f"  {child.name}/")

            #print(f"folder: {child.name}")
            #print(f"{child.parent} -> {child.name}")
            #pp.pprint(child.__dict__)
            #await list_dir(child)

        elif isinstance(child, Document):  # The only other possibility
            print(f"  {child.name}, {await child.type()}")
            #print(f"{await child.type()}, {child.name}")
            #print(f"  {child.name} ({await child.type()})")
            #pp.pprint(child.__dict__)

            #await child.delete()

    for child in sub_dirs:
        await list_dir(child)

    #for child in sub_dirs:
    #    if child.name != ".trash":
    #        await child.delete()


async def list_nested_files():
    root = await Item.get_by_id('')  # The root folder has ID of empty string

    sub_dirs = []

    for child in root.children:

        if isinstance(child, Folder):
            #parentItem = await Item.get_by_id(child.parent)
            #parentName = parentItem.name
            sub_dirs.append(child)
            print(f"  {child.name}/")
            #pp.pprint(child.__dict__)
            #if child.name in ['foo', 'testpath', 'SynologyDrive', 'papers']:
            #    print("child recognized")
            #    await child.delete()

        elif isinstance(child, Document):  # The only other possibility
            print(f"  {child.name}, {await child.type()}")
            #print(child.id)
            #pp.pprint(child.__dict__)

            # move item to trash by updating metadata
            #child.parent = TRASH_ID
            #await child.update_metadata()

            #await child.delete()

    for child in sub_dirs:
        await list_dir(child)

    #for child in sub_dirs:
    #    if child.name != ".trash":
    #        await child.delete()



#trio.run(list_files)
#trio.run(list_nested_files)


def migrate_dir(folder):

    for child in folder.children:
        if isinstance(child, Folder):
            #parentItem = await Item.get_by_id(child.parent)
            #parentName = parentItem.name
            sub_dirs.append(child)
            print(f"  {child.name}/")
            #pp.pprint(child.__dict__)
            #if child.name in ['foo', 'testpath', 'SynologyDrive', 'papers']:
            #    print("child recognized")
            #    await child.delete()

        elif isinstance(child, Document):  # The only other possibility
            print(f"  {child.name}, {child.type()}")
            #print(child.id)
            #pp.pprint(child.__dict__)

            # move item to trash by updating metadata
            #child.parent = TRASH_ID
            #await child.update_metadata()

            #await child.delete()

    #for child in sub_dirs:
    #    await list_dir(child)

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(abs_dir):
    print()
    rel_path = os.path.relpath(root, relative_path)
    #print(rel_path)
    rpath = rel_path.split(os.sep)
    print(root)

    path = root.split(os.sep)

    #for dirpath in dirs:
    #    print(dirpath)

    #print("mkdir " + rel_path)
    
    for file in files:
        print("file:", file)
        #file_path = os.path.join(root, file)
        #if file[0] != '.':
        #    print("upload " + file_path + " " + rel_path)
    for dir in dirs:
        print("dir:", dir)
