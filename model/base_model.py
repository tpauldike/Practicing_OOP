#!/usr/bin/env python3
import uuid
from datetime import datetime

class BaseModel:
    '''BaseModel class'''
    __id = uuid.uuid4()
    __created_at = datetime.now()
    __updated_at = datetime.now()

var = BaseModel
print(var.__name__)
