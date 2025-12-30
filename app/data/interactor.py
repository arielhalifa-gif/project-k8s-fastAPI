from pymongo import MongoClient
import pymongo

class Interactor:
    def get_connection():
        client = MongoClient('mongodb://localhost:27017/')
        db = client["contacts_db"]
        return db
    

    def create_contact(contact_data: dict) -> str:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        inserted_contact = contacts_collection.insert_one(contact_data)
        return inserted_contact.inserted_id
    

    def get_all_contacts() -> list:
        db = Interactor.get_connection()
        contacts_collection = db["contacts"]
        