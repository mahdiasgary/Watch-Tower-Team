from mongoengine import Document, StringField, DateTimeField, ListField
from datetime import datetime


class ASN(Document):
    program_name = StringField(required=True)
    asn_list = ListField(StringField())
    created_date = DateTimeField(default=datetime.now)
    last_update = DateTimeField(default=datetime.now)

    meta = {"indexes": [{"fields": ["program_name", "asn_list"], "unique": True}]}

    def json(self):
        return {
            "program_name": self.program_name,
            "asn_list": self.asn_list,
            "created_date": (
                self.created_date.isoformat() if self.created_date else None
            ),
            "last_update": (self.last_update.isoformat() if self.last_update else None),
        }