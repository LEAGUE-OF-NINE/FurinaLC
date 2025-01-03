from pydantic import BaseModel
from database.client import db
from resources.parser.user_stuff.item import create_item_format_list
from limbus.formats import ItemFormat
from typing import List, Optional

item_collection = db["items"]


class ItemFormatWithUID(BaseModel):
    uid: int
    item_id: int
    num: int


def insert_item_formats(uid: int) -> None:
    try:
        item_format_list = create_item_format_list()
        item_format_with_uid_list = [
            ItemFormatWithUID(
                uid=uid,
                item_id=item_format.item_id,
                num=item_format.num,
            )
            for item_format in item_format_list
        ]

        if item_format_with_uid_list:
            item_collection.insert_many(
                [item.dict() for item in item_format_with_uid_list]
            )
    except Exception as e:
        print("WARN:     " + str(e))


def get_item_formats_by_uid(uid: int) -> List[ItemFormat]:
    try:
        item_docs = item_collection.find({"uid": uid})

        return [
            ItemFormat(
                item_id=doc["item_id"],
                num=doc["num"],
            )
            for doc in item_docs
        ]

    except Exception as e:
        print("WARN:     " + str(e))

        return []


def update_item_format(uid: int, item_id: int, num: Optional[int] = None) -> bool:
    try:
        update_fields = {}
        if num is not None:
            update_fields["num"] = num

        if update_fields:
            item_collection.update_one(
                {"uid": uid, "item_id": item_id}, {"$set": update_fields}
            )

            return True

        return True

    except Exception as e:
        print("WARN:     " + str(e))

        return False


def sync_item_formats(uid: int) -> Optional[List[ItemFormat]]:
    try:
        existing_item_docs = item_collection.find({"uid": uid})
        existing_item_ids = {doc["item_id"] for doc in existing_item_docs}

        new_item_formats = create_item_format_list()

        new_items_to_add = [
            item_format
            for item_format in new_item_formats
            if item_format.item_id not in existing_item_ids
        ]

        if new_items_to_add:
            item_format_with_uid_list = [
                ItemFormatWithUID(
                    uid=uid,
                    item_id=item_format.item_id,
                    num=item_format.num,
                )
                for item_format in new_items_to_add
            ]

            item_collection.insert_many(
                [item.dict() for item in item_format_with_uid_list]
            )

            print(
                "INFO:     "
                + f"{len(new_items_to_add)} new item(s) inserted for UID {uid}."
            )

            return [
                ItemFormat(
                    item_id=item_format.item_id,
                    num=item_format.num,
                )
                for item_format in new_items_to_add
            ]
        else:
            print("INFO:     " + f"No new item data to insert for UID {uid}.")
            return None

    except Exception as e:
        print("WARN:     " + str(e))
        return None
