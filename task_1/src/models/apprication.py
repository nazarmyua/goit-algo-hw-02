import uuid


class Apprication:
    def __init__(self, data: str):
        self.id = uuid.uuid4()
        self.data = data

    def __str__(self):
        return f"Apprication(id={self.id}, data='{self.data}')"
