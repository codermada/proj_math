from . import db


class Supdomain(db.Model):
    __tablename__ = 'supdomains'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    domains = db.relationship('Domain', backref='supdomain', lazy='dynamic')
    def __repr__(self):
        return f'<supdomain {self.id}>'


class Domain(db.Model):
    __tablename__ = 'domains'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    supdomain_id = db.Column(db.Integer, db.ForeignKey('supdomains.id'))
    formulas = db.relationship('Formula', backref='domain', lazy='dynamic')
    def __repr__(self):
        return f'<domain {self.id}>'


class Formula(db.Model):
    __tablename__ = 'formulas'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    cover = db.Column(db.LargeBinary)
    description = db.Column(db.Text)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'))
    pictures = db.relationship('Picture', backref='formula', lazy='dynamic')
    def __repr__(self):
        return f'<supdomain {self.id}>'


class Picture(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    picture = db.Column(db.LargeBinary)
    description = db.Column(db.Text)
    formula_id = db.Column(db.Integer, db.ForeignKey('formulas.id'))
    def __repr__(self):
        return f'<picture {self.id}>'
