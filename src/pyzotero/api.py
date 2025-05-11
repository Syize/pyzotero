from dataclasses import dataclass


BASE_PATH = "/{library_type}/{library_id}"


@dataclass()
class ZoteroAPI:
    """
    Store Zotero API path.
    """
    API_KEY_INFO = "/keys/{key}"
    BASE_PATH = BASE_PATH
    COLLECTIONS = BASE_PATH + "/collections"
    COLLECTIONS_key = BASE_PATH + "/collections/{key}"
    COLLECTIONS_key_COLLECTIONS = BASE_PATH + "/collections/{key}/collections"
    COLLECTIONS_key_ITEMS = BASE_PATH + "/collections/{key}/items"
    COLLECTIONS_key_ITEMS_TAGS = BASE_PATH + "/collections/{key}/items_tags"
    COLLECTIONS_key_ITEMS_TOP = BASE_PATH + "/collections/{key}/items/top"
    COLLECTIONS_key_ITEMS_TOP_TAGS = BASE_PATH + "/collections/{key}/items/top/tags"
    COLLECTIONS_key_TAGS = BASE_PATH + "/collections/{key}/tags"
    COLLECTIONS_TOP = BASE_PATH + "/collections/top"
    CREATOR_FIELDS = "/creatorFields"
    DELETED = BASE_PATH + "/deleted"
    FULLTEXT = BASE_PATH + "/fulltext"
    GROUPS = "/users/{library_id}/groups"
    ITEM_FIELDS = "/itemFields"
    ITEM_TYPES = "/itemTypes"
    ITEM_TYPE_CREATOR_TYPES = "/itemTypeCreatorTypes"
    ITEM_TYPE_FIELDS = "/itemTypeFields"
    ITEMS = BASE_PATH + "/items"
    ITEMS_key = BASE_PATH + "/items/{key}"
    ITEMS_key_CHILDREN = BASE_PATH + "/items/{key}/children"
    ITEMS_key_FULLTEXT = BASE_PATH + "/items/{key}/fulltext"
    ITEMS_key_FILE = BASE_PATH + "/items/{key}/file"
    ITEMS_key_TAGS = BASE_PATH + "/items/{key}/tags"
    ITEMS_TOP = BASE_PATH + "/items/top"
    ITEMS_TOP_TAGS = BASE_PATH + "/items/top/tags"
    ITEMS_TRASH = BASE_PATH + "/items/trash"
    ITEMS_TRASH_TAGS = BASE_PATH + "/items/trash/tags"
    PUBLICATIONS_ITEMS = BASE_PATH + "/publications/items"
    PUBLICATIONS_ITEMS_TAGS = BASE_PATH + "/publications/items/tags"
    SEARCHES = BASE_PATH + "/searches"
    SEARCHES_key = BASE_PATH + "/searches/{key}"
    SETTINGS = BASE_PATH + "/settings"
    TAGS = BASE_PATH + "/tags"


@dataclass()
class ExportFormat:
    BIBTEX = "bibtex"
    BIBLATEX = "biblatex"
    BOOKMARKS = "bookmarks"
    COINS = "coins"
    CSLJSON = "csljson"
    CSV = "csv"
    MODS = "mods"
    REFER = "refer"
    RDF_BIBLIONTOLOGY = "rdf_bibliontology"
    RDF_DC = "rdf_dc"
    RDF_ZOTERO = "rdf_zotero"
    RIS = "ris"
    TEI = "tei"
    WIKIPEDIA = "wikipedia"


@dataclass()
class Format:
    ATOM = "atom"
    BIB = "bib"
    JSON = "json"
    KEYS = "keys"
    VERSIONS = "versions"


__all__ = ["ZoteroAPI", "ExportFormat", "Format"]
