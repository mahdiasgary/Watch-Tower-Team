from mongoengine import Document, StringField, DateTimeField, ListField, DictField
from datetime import datetime


class ip_http(Document):
    program_name = StringField(required=True)
    ip = StringField(required=True)
    port = StringField(required=True)
    scheme = StringField()
    webserver = StringField()
    tech = ListField(StringField())
    title = StringField()
    status_code = StringField()
    headers = DictField()
    url = StringField()
    favicon = StringField()
    created_date = DateTimeField(default=datetime.now())
    last_update = DateTimeField(default=datetime.now())

    meta = {
        "indexes": [
            {
                "fields": ["ip"],
                "unique": False,
            }  # Create a unique index on 'program_name' and 'subdomain'
        ]
    }

    def json(self):
        return {
            "program_name": self.program_name,
            "ip": self.ip,
            "port": self.port,
            "scheme": self.scheme,
            "webserver": self.webserver,
            "ips": self.ips or [],
            "tech": self.tech or [],
            "title": self.title,
            "status_code": self.status_code or [],
            "headers": self.headers or {},
            "url": self.url,
            "favicon": self.favicon,
            "created_date": (
                self.created_date.isoformat() if self.created_date else None
            ),
            "last_update": self.last_update.isoformat() if self.last_update else None,
        }
