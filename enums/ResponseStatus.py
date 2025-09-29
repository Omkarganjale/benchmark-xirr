from enum import Enum


class ResponseStatus(Enum):
	SUCCESS = "Success"
	ERROR = "Error"

	def __str__(self):
		return self.value
