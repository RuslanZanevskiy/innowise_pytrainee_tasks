from src.parsers import DbConfigParser, ArgumentParser
from src.db import DbConnector, DbExecutor
from src.json_reader import JsonReader
from src.file_writers import JsonWriter, XmlWriter

import logging


def get_args():
    logging.info('getting args')
    args = list(ArgumentParser.parse_args(3))
    args[2] = args[2].lower()
    assert args[2] in ('json', 'xml')
    return args

def main():
    students_data_file, rooms_data_file, output_format = get_args()

    db_config = DbConfigParser.parse_config()

    connector = DbConnector(db_config)
    connector.connect()

    executor = DbExecutor(connector)

    executor.execute_sql_file('sql/schema.sql')

    rooms_data = JsonReader.read(rooms_data_file)
    students_data = JsonReader.read(students_data_file)
    rooms_data = [[*d.values()] for d in rooms_data]
    students_data = [[*d.values()] for d in students_data]

    executor.populate_table('Rooms', ['id', 'name'], rooms_data)
    executor.populate_table('Students', 
                            ['birthday', 'id', 'name', 'room_id', 'sex'], 
                            students_data)

    executor.execute_sql_file('sql/indexes.sql')

    data_writer = JsonWriter() if output_format == 'json' else XmlWriter() 

    executor.execute_sql_file('sql/nstudents_in_rooms.sql')
    students_in_rooms = executor.get_records()
    columns = executor.get_columns()
    data_writer.write_to_file('query_data/students_in_rooms', students_in_rooms, columns)

    executor.execute_sql_file('sql/small_mean_age_rooms.sql')
    small_mean_age_rooms = executor.get_records()
    columns = executor.get_columns()
    data_writer.write_to_file('query_data/small_mean_age_rooms', small_mean_age_rooms, columns)

    executor.execute_sql_file('sql/big_age_diff_rooms.sql')
    big_age_diff_rooms = executor.get_records()
    columns = executor.get_columns()
    data_writer.write_to_file('query_data/big_age_diff_rooms', big_age_diff_rooms, columns)

    executor.execute_sql_file('sql/male_female_rooms.sql')
    male_female_rooms = executor.get_records()
    columns = executor.get_columns()
    data_writer.write_to_file('query_data/male_female_rooms', male_female_rooms, columns)

    executor.close()
    connector.close()

if __name__ == '__main__':
    logging.basicConfig(filename='logs.log', 
                        format='%(asctime)s - %(name)s - %(levelname)s - [%(module)s.%(funcName)s:%(lineno)d] - %(message)s', 
                        encoding='utf-8', 
                        level=logging.DEBUG)
    main()
