import sqlalchemy as sq
import sqlalchemy.orm as ors



Excel = ors.declarative_base()
Sess = ors.sessionmaker()
unreal = sq.create_engine("sqlite:///unitylist.db")


class Table(Excel):
    __tablename__ = "usert"
    ind = sq.Column(sq.Integer(), primary_key = True)
    name = sq.Column(sq.String(12), unique = True, nullable = False)
    score = sq.Column(sq.Integer())

