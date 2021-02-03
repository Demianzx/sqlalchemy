from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, create_engine

engine = create_engine('postgresql://postgres:undercover@localhost/sqlalchemy')
Base = declarative_base()

class Commit(Base):
    __tablename__='commits'

    commit_id = Column(Integer(), primary_key=True)
    comment = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
    date = Column(DateTime(), default=datetime.now())
    
    

    def __str__(self):
        return self.comment

class PullRequest(Base):
    __tablename__='pull_request'

    pull_request_id = Column(Integer(), primary_key=True)    
    commit = relationship("Commit", back_populates="pull_request")
    commit_id = Column(Integer, ForeignKey('commits.commit_id'))
    date = Column(DateTime(), default=datetime.now())

class Branch(Base):
    __tablename__='branch'

    branch_id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    date = Column(DateTime(), default=datetime.now())
    content = Column(String(255), nullable=True)
    pull_request_id = Column(Integer, ForeignKey('pull_request.pull_request_id'))

class Repository(Base):
    __tablename__='repository'

    repository_id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    branch_id = Column(Integer, ForeignKey('branch.branch_id'))
    about = Column(String(255), nullable=True)
    tags = Column(String(255), nullable=True)
    date = Column(DateTime(), default=datetime.now())

Session = sessionmaker(engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

