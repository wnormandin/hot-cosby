import datetime
from sqlalchemy import create_engine, ForeignKey, Float, Column, Integer, DateTime, String, Boolean, Enum, Text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from ..config import DB_URL
from ..config.globals import SecurityType, OptionType, TradeAction


engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()


class Base(DeclarativeBase):
    pass


class TimestampedRecord(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)


class Account(TimestampedRecord):
    __tablename__ = 'accounts'

    username = Column(String(196), unique=True, nullable=False)
    last_login = Column(DateTime)
    active = Column(Boolean, default=False)
    email = Column(String(196), nullable=True, index=True)
    credential_file = Column(String(1024), nullable=True)



class Config(TimestampedRecord):
    __tablename__ = 'configuration'

    key = Column(String(196), unique=True, nullable=False)
    value = Column(String(196), nullable=True)

    @classmethod
    def get_config(cls, session, key):
        return session.query(Config).filter_by(key=key).first()


class Product(TimestampedRecord):
    __tablename__ = 'products'

    symbol = Column(String(196), unique=True, nullable=False)
    type = Column(Enum(SecurityType), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    option_type = Column(Enum(OptionType), nullable=False)
    last_quote_date = Column(DateTime)

    @classmethod
    def get_pending_quotes(cls, session):
        quote_interval_hours = Config.get_config(session=session, key='QUOTE_INTERVAL_HOURS') or 24
        quote_update_interval = datetime.timedelta(hours=int(quote_interval_hours))
        return (session.query(Product)
                       .filter(Product.last_quote_date < (datetime.datetime.now() - quote_update_interval)))


class Strategy(TimestampedRecord):
    __tablename__ = 'strategies'

    name = Column(String(196), unique=True, nullable=False)
    active = Column(Boolean, default=False)
    description = Column(Text, nullable=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))

    account = relationship(Account)


class Trade(TimestampedRecord):
    __tablename__ = 'trades'

    symbol = Column(String(196), ForeignKey('products.symbol'))
    strategy_id = Column(Integer, ForeignKey('strategies.id'))
    action = Column(Enum(TradeAction))
    dollar_amount = Column(Float)

    product = relationship(Product)
    strategy = relationship(Strategy)


class Quote(TimestampedRecord):
    __tablename__ = 'quotes'


def create_db():
    Base.metadata.create_all(bind=engine)


__all__ = ['create_db', 'Quote', 'Trade', 'Strategy', 'Account', 'Product', 'Config', 'get_session']
