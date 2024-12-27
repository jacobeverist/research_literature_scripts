from pyzotero import zotero

api_key = 'XXXXXXXXX'
library_type = 'user'
library_id = '99999999'

zot = zotero.Zotero(library_id, library_type, api_key)
#items = zot.top(limit=5)
#items = zot.items()

#collections = zot.collections_top()
collections = zot.collections()

for col in collections:
    print()
    print("Collection")
    print("----", col['data']['name'])


    col_key = col['key']

    subs = zot.collections_sub(col_key)
    if subs:
        print()
        print("Sub-Collections:")
    for sub in subs:
        print("--", sub['data']['name'])

    print()

    items = zot.collection_items(col_key)

    for item in items:
        try:
            print(item['data']['title'])
        except:
            print(item.keys())
            pass
        print()
    #print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))


