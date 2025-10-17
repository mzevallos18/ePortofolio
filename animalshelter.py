from typing import Any, Dict, Iterable, Optional
from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection
from pymongo.results import InsertOneResult, UpdateResult, DeleteResult
from bson.objectid import ObjectId


class AnimalShelter:
    """CRUD wrapper around MongoDB for the aac.animals collection"""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 27017,
        username: Optional[str] = None,
        password: Optional[str] = None,
        db_name: str = "aac",
        coll_name: str = "animals",
        conn_str: Optional[str] = None,
        tls: bool = False,
    ):
        # Connect using connection string or host/port
        if conn_str:
            self.client = MongoClient(conn_str, tls=tls)
        else:
            if username and password:
                uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource={db_name}"
                self.client = MongoClient(uri)
            else:
                self.client = MongoClient(host=host, port=port)

        self.db = self.client[db_name]
        self.col: Collection = self.db[coll_name]

        # Create indexes
        self.col.create_index([("animal_type", ASCENDING)])
        self.col.create_index([("breed", ASCENDING)])
        self.col.create_index([("age_upon_outcome", ASCENDING)])

    # CREATE
    def create(self, doc: Dict[str, Any]) -> Optional[str]:
        # Insert one document
        if not isinstance(doc, dict) or not doc:
            return None
        res: InsertOneResult = self.col.insert_one(doc)
        return str(res.inserted_id) if res.inserted_id else None

    # READ
    def read(self, query: Optional[Dict[str, Any]] = None, limit: int = 0) -> Iterable[Dict[str, Any]]:
        # Find documents by query
        q = query or {}
        cursor = self.col.find(q)
        if limit and limit > 0:
            cursor = cursor.limit(limit)
        return cursor

    def read_one_by_id(self, oid: str) -> Optional[Dict[str, Any]]:
        # Find document by ObjectId
        try:
            return self.col.find_one({"_id": ObjectId(oid)})
        except Exception:
            return None

    # UPDATE
    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        # Update documents matching query
        if not query or not new_values:
            return 0
        res: UpdateResult = self.col.update_many(query, {"$set": new_values})
        return res.modified_count or 0

    # DELETE
    def delete(self, query: Dict[str, Any]) -> int:
        # Delete documents matching query
        if not query:
            return 0
        res: DeleteResult = self.col.delete_many(query)
        return res.deleted_count or 0

    # COMMON QUERIES
    def find_adoptable_dogs(self, breeds: Iterable[str] = ()) -> Iterable[Dict[str, Any]]:
        # Find adoptable intact dogs by breed
        q: Dict[str, Any] = {
            "animal_type": "Dog",
            "sex_upon_outcome": {"$regex": "Intact", "$options": "i"},
            "outcome_type": "Adoption"
        }
        if breeds:
            q["breed"] = {"$in": list(breed.strip() for breed in breeds)}
        return self.read(q)

    def find_by_simple_filters(self, animal_type: Optional[str] = None, age_contains: Optional[str] = None, limit: int = 0):
        # Find animals by type or age filters
        q: Dict[str, Any] = {}
        if animal_type:
            q["animal_type"] = {"$regex": f"^{animal_type}$", "$options": "i"}
        if age_contains:
            q["age_upon_outcome"] = {"$regex": age_contains, "$options": "i"}
        return self.read(q, limit=limit)
