from pydantic import BaseModel, Field, SecretStr
import logging


class UserDetails(BaseModel):
    user_name:str=Field(..., description='Please specify the username', max_length=10)
    password:SecretStr
    
