from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
	def __init__(self):
		pass
