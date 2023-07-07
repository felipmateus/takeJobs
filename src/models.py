from sql_alchemy import db
from sqlalchemy import func

class JobsModel(db.Model):
    __tablename__ = 'scrapy_vagas'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    local = db.Column(db.String(80))
    date = db.Column(db.String(80))
    site = db.Column(db.String(80))
    date_extracted = db.Column(db.String(80))

    def __init__(self, title, description, local, date, site, date_extracted):
        self.title = title
        self.description = description
        self.local = local
        self.date = date
        self.site = site
        self.date_extracted = date_extracted

    
    def json(self):
        return{
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'local': self.local,
            'date': self.date,
            'site': self.site,
            'date_extracted': str(self.date_extracted)
        }
   
    
    @classmethod
    def find_by_title(cls, title, page, limit):
        jobs = cls.query.filter(func.lower(cls.title).contains(func.lower(title))).paginate(page=page, per_page=limit, max_per_page=limit)
        if jobs:
            return jobs
        return None

    @classmethod
    def select_all(cls, page, limit):
        jobs = cls.query.paginate(page=page, per_page=limit, max_per_page=limit)
        if jobs:
            return jobs
        return None
