from fastapi import FastAPI, HTTPException
from data.interactor import Interactor as i
from data.contacts import Contact as con
import uvicorn


app = FastAPI()


@app.get("/contacts")
def get_all():
    list_of_contacts = i.get_all_contacts() # get list of objects -> we need dict
    list_of_dicts = []
    for doc in list_of_contacts:
        list_of_dicts.append(con.into_dict(doc))
    return list_of_dicts


@app.post("/contacts")
def create_new_contact(contact_data):
    contact_data = {"first_name": contact_data["first_name"], 
                    "last_name": contact_data["last_name"],
                    "phone_number": contact_data["phone_number"]}
    returned_id = i.create_contact(contact_data)
    return {"message": "Contact created successfully",
            "id": returned_id}


@app.put("/contacts/{id}")
def update_existing_contact(new_data):
   result = i.update_contact(id, new_data)
   if result:
       return {"message": "updated successfully"}
   else:
       return {"message": "update failed"}
   

@app.delete("/contacts/{id}")
def delete_existing_contact():
    result = i.delete_contact(id)
    if result:
        return {"message": "deleted succesfully"}
    else:
        return {"message": "failed to delete"}
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")