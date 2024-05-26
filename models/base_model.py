#!/usr/bin/python3
"""

"""
import uuid
from datetime from datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
    
    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


