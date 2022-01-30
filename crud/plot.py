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


def sector_segment_wise_data(flag, data):
    total = total_transactions(flag)
    sectors = sector_count(flag, data)
    labels = [f"{i[0]} = {i[1]}" for i in sectors]
    data = [round((i[1] / total) * 100, 2) for i in sectors]
    return labels, data


def sector_and_segment_wise_data(flag='count'):
    if flag == 'count':
        sql = text('select s.sector as sector, s.segment as segment, count(*) as amt from transactions t, '
                   ' stocks s where t.stockId = s.id GROUP BY s.sector, s.segment')
    else:
        sql = text(
            'select s.sector as sector, s.segment as segment, sum(t.price * t.quantity) as amt from transactions t, '
            ' stocks s where t.stockId = s.id GROUP BY s.sector, s.segment')
    result = engine.execute(sql)
    output = [row for row in result]

    labels = list()
    for i in output:
        if i[0] not in labels:
            labels.append(i[0])
    data = {i[1]: [0] * len(labels) for i in output}

    for row in output:
        data[row[1]][labels.index(row[0])] = row[2]

    return labels, data


def sector_and_segment_wise_stacked_data(flag='count'):
    if flag == 'count':
        sql = text('select s.sector as sector, s.segment as segment, count(*) as amt from transactions t, '
                   ' stocks s where t.stockId = s.id GROUP BY s.sector, s.segment')
    else:
        sql = text(
            'select s.sector as sector, s.segment as segment, sum(t.price * t.quantity) as amt from transactions t, '
            ' stocks s where t.stockId = s.id GROUP BY s.sector, s.segment')
    result = engine.execute(sql)
    output = [row for row in result]

    labels = list()
    for i in output:
        if i[0] not in labels:
            labels.append(i[0])

    legends = list()
    for i in output:
        if i[1] not in legends:
            legends.append(i[1])

    data = [[0 for i in range(len(labels))] for j in range(len(legends))]
    for row in output:
        data[labels.index(row[0])][legends.index(row[1])] = row[2]

    return labels, legends, data
