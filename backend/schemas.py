import datetime as _dt

from dataclasses import dataclass


@dataclass
class _UserBase:
    email: str


@dataclass
class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


@dataclass
class User(_UserBase):
    id: int

    class Config:
        orm_mode = True


@dataclass
class _LeadBase:
    first_name: str
    last_name: str
    email: str
    company: str
    note: str


class LeadCreate(_LeadBase):
    pass


@dataclass
class Lead(_LeadBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_udated: _dt.datetime

    class Config:
        orm_mode = True
