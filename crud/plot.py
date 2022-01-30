from DataBase.database import engine
from sqlalchemy import text


def total_transactions(total='count'):
    if total == 'count':
        sql = text('select count(*) from transactions t, stocks s where t.stockId = s.id')
    else:
        sql = text('select sum(t.price * t.quantity) from transactions t, stocks s where t.stockId = s.id')
    result = engine.execute(sql)
    for row in result:
        return row[0]


def sector_count(total='count', data='sector'):
    if total == 'count':
        sql = text(f'select s.{data} as sector, count(s.{data}) as cnt from transactions t, stocks s where t.stockId = '
                   f's.id GROUP BY s.{data}')
    else:
        sql = text(f'select s.{data} as sector, sum(t.price * t.quantity) as cnt from transactions t, stocks s '
                   f'where t.stockId = s.id GROUP BY s.{data}')
    result = engine.execute(sql)
    sectors = [row for row in result]
    return sectors


def sector_wise_count():
    total = total_transactions('count')
    sectors = sector_count('count')
    labels = [f"{i[0]} = {i[1]}" for i in sectors]
    data = [round((i[1] / total) * 100, 2) for i in sectors]
    return labels, data


def sector_wise_amount():
    total = total_transactions('sum')
    sectors = sector_count('sum')
    labels = [f"{i[0]} = {i[1]}" for i in sectors]
    data = [round((i[1] / total) * 100, 2) for i in sectors]
    return labels, data


def sector_segment_wise_data(flag, data):
    total = total_transactions(flag)
    sectors = sector_count(flag, data)
    labels = [f"{i[0]} = {i[1]}" for i in sectors]
    data = [round((i[1] / total) * 100, 2) for i in sectors]
    return labels, data
