from bson import ObjectId
from pymongo import MongoClient
from .contacts import Contact

class Interactor:
    def get_connection():
        client = MongoClient('mongodb://localhost:27017/')
        db = client["contacts_db"]
        return db

    # db = get_connection()
    # contacts_collection = db["contacts"]   
    @staticmethod
    def create_contact(contact_data: dict) -> str:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        inserted_contact = contacts_collection.insert_one(contact_data)
        return inserted_contact.inserted_id
    
    @staticmethod
    def get_all_contacts() -> list:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        collection = contacts_collection.find()
        contacts_list = []
        for contact in collection:
            contacts_list.append(Contact(contact["first_name"],
                                         contact["last_name"],
                                         contact["phone_number"]))
        return contacts_list
    
    @staticmethod
    def update_contact(id: str, contact_data: dict) -> bool:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        result = contacts_collection.update_one({"_id": ObjectId(id)}, # filter
                                                {"$set": {"first_name": contact_data["first_name"],
                                                          "last_name": contact_data["last_name"],
                                                          "phone_number": contact_data["phone_number"]}})
        return True
    
    @staticmethod
    def delete_contact(id: str) -> bool:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        deleted_contact = contacts_collection.delete_one({"_id": ObjectId(id)})
        return True