from dataclasses import dataclass


BASE_PATH = "/{library_type}/{library_id}"


@dataclass()
class ZoteroAPIOld:
    """
    Store Zotero API path.
    """
    API_KEY_INFO = "/keys/{key}"
    BASE_PATH = BASE_PATH
    COLLECTIONS = BASE_PATH + "/collections"
    COLLECTIONS_name = BASE_PATH + "/collections/{name}"
    COLLECTIONS_name_COLLECTIONS = BASE_PATH + "/collections/{name}/collections"
    COLLECTIONS_name_ITEMS = BASE_PATH + "/collections/{name}/items"
    COLLECTIONS_name_ITEMS_TOP = BASE_PATH + "/collections/{name}/items/top"
    COLLECTIONS_name_TAGS = BASE_PATH + "/collections/{name}/tags"
    COLLECTIONS_TOP = BASE_PATH + "/collections/top"
    CREATOR_FIELDS = "/creatorFields"
    DELETED = BASE_PATH + "/deleted"
    FULLTEXT = BASE_PATH + "/fulltext"
    GROUPS = "/users/{ID}/groups"
    ITEM_FIELDS = "/itemFields"
    ITEM_TYPES = "/itemTypes"
    ITEM_TYPE_CREATOR_TYPES = "/itemTypeCreatorTypes"
    ITEM_TYPE_FIELDS = "/itemTypeFields"
    ITEMS = BASE_PATH + "/items"
    ITEMS_itemkey = BASE_PATH + "/items/{itemkey}"
    ITEMS_itemkey_CHILDREN = BASE_PATH + "/items/{itemkey}/children"
    ITEMS_itemkey_FULLTEXT = BASE_PATH + "/items/{itemkey}/fulltext"
    ITEMS_itemkey_FILE = BASE_PATH + "/items/{itemkey}/file"
    ITEMS_itemkey_TAGS = BASE_PATH + "/items/{itemkey}/tags"
    ITEMS_TOP = BASE_PATH + "/items/top"
    ITEMS_TRASH = BASE_PATH + "/items/trash"
    PUBLICATIONS_ITEMS = BASE_PATH + "/publications/items"
    SEARCHES = BASE_PATH + "/searches"
    SETTINGS = BASE_PATH + "/settings"
    TAGS = BASE_PATH + "/tags"


__all__ = ["ZoteroAPIOld"]
