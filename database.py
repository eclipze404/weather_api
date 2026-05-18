import sqlite3

def get_conn():
    return sqlite3.connect('weather.db')

def range_filter(
    query: str,
    params: list,
    column: str,
    min_val=None,
    max_val=None
):
    if min_val is not None and max_val is not None:
        query+=f' AND {column} BETWEEN ? AND ?'
        params.extend([min_val, max_val])
    elif min_val is not None:
        query+=f' AND {column}>=?'
        params.extend([min_val])
    elif max_val is not None:
        query+=f' AND {column}<=?'
        params.extend([max_val])

    return query, params


def get_data(
    town_id: int = None,
    date_from: str = None,
    date_to: str = None,
    weather_main: str = None,
    temp_from: float = None,
    temp_to: float = None,
    pressure_from: float = None,
    pressure_to: float = None,
    humidity_from: int = None,
    humidity_to: int = None,
    wind_speed_from: float = None,
    wind_speed_to: float = None,
    clouds_from: int = None,
    clouds_to: int = None,
    limit=100,
    offset=0
):
    conn = get_conn()
    cursor = conn.cursor()
    query = '''SELECT id,
town_id,
created_at,
weather_main,
main_temp,
main_feels_like,
main_pressure,
main_humidity,
wind_speed,
clouds_all

FROM weather

WHERE 1=1
'''
    params = []
    if  town_id is not None:
        query+=' AND town_id=?'
        params.append(town_id)

    query, params = range_filter(query, params, column='created_at', min_val=date_from, max_val=date_to)

    if weather_main is not None:
        query+=' AND weather_main=?'
        params.append(weather_main)

    query, params = range_filter(query, params, column='main_temp', min_val=temp_from, max_val=temp_to)

    query, params = range_filter(query, params, column='main_pressure', min_val=pressure_from, max_val=pressure_to)

    query, params = range_filter(query, params, column='main_humidity', min_val=humidity_from, max_val=humidity_to)

    query, params = range_filter(query, params, column='wind_speed', min_val=wind_speed_from, max_val=wind_speed_to)

    query, params = range_filter(query, params, column='clouds_all', min_val=clouds_from, max_val=clouds_to)

    # query+=' ORDER BY created_at DESC'
    query+=' LIMIT ? OFFSET ?'
    params.append(limit)
    params.append(offset)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    conn.close()

    columns = [desc[0] for desc in cursor.description]
    return [dict(zip(columns, row)) for row in rows]
