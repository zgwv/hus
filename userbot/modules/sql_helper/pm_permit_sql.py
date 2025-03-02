try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func


class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


PMPermit.__table__.create(checkfirst=True)


def is_approved(chat_id):
    try:
        return SESSION.query(PMPermit).filter(
            PMPermit.chat_id == chat_id).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def approve(chat_id):
    adder = PMPermit(chat_id)
    SESSION.add(adder)
    SESSION.commit()


def dissprove(chat_id):
    rem = SESSION.query(PMPermit).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
