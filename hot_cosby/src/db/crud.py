from . import get_session, Product, Config


def _find_row(session, orm_cls, **filters):
    find_query = session.query(orm_cls)

    for key, val in filters.items():
        find_query = find_query.filter_by(key=val)

    return find_query.first()


def _upsert(session, orm_cls, identifiers: dict, **attributes):
    created = False
    row = _find_row(session=session, orm_cls=orm_cls, **identifiers)
    if row is None:
        row = orm_cls(**identifiers, **attributes)
        session.add(row)
        session.commit()
        created = True

    return row, created


def upsert_product(session, symbol: str, **attributes):
    return _upsert(
        session=session,
        identifiers={'symbol': symbol},
        **attributes
    )


def get_config(session, key: str) -> dict:
    found = _find_row(session=session, orm_cls=Config, key=key)
    if found:
        return {'key': key, 'value': found.value}
    return {'key': key, 'value': None}


def set_config(session, key: str, value: str):
    return _upsert(session=session, orm_cls=Config, identifiers={'key': key}, value=value)


__all__ = ['upsert_product', 'get_config', 'set_config']
