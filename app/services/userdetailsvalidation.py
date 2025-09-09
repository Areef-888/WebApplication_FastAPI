from pydantic import SecretStr
import logging


userdetails={
    "user":"Areef",
    "password":"Welcome@EY"
}

logging.basicConfig(level=logging.INFO)

class Validations:
    def userloginvalidations(username:str,password:SecretStr):

        if (userdetails["user"]==username) and (userdetails["password"]==password.get_secret_value()):
                                
                logging.info("User details validated successfully")
        else:
                raise ValueError("Details Mismatch")


