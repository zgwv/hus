try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String


class Mute(BASE):
    __tablename__ = "muted"
    chat_id = Column(String(14), primary_key=True)
    sender = Column(String(14), primary_key=True)

    def __init__(self, chat_id, sender):
        self.chat_id = chat_id
        self.sender = str(sender)


Mute.__table__.create(checkfirst=True)


def is_muted(chat_id):
    try:
        return SESSION.query(Mute).filter(Mute.chat_id == chat_id).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def mute(chat_id, sender):
    adder = Mute(chat_id, str(sender))
    SESSION.add(adder)
    SESSION.commit()


def unmute(chat_id, sender):
    rem = SESSION.query(Mute).get(((chat_id), (str(sender))))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
