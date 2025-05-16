import psycopg2
from psycopg2.extras import execute_values

import logging

logger = logging.getLogger(__name__)


class DbConnector:
    def __init__(self, config: dict):
        self.config = config
        self.connection = None
        logger.debug('dbconnector initialized')

    def connect(self):
        logger.info('setting up db connection')
        assert self.connection is None
        self.connection = psycopg2.connect(**self.config)
        logger.info('connected to db')
        return self.connection
    
    def close(self):
        assert self.connection is not None
        logger.info('disconnecting from db')
        self.connection.close()
        self.connection = None


class DbExecutor:
    def __init__(self, connector):
        logger.info('initializing dbexecutor')
        self.connector = connector
        assert self.connector.connection is not None
        self.cursor = self.connector.connection.cursor()
        logger.info('dbexecutor and cursor created')

    def close(self):
        logger.info('closing dbexecutor')
        self.cursor.close()

    def execute_sql_file(self, file: str):
        logger.info(f'reading {file} for sql query')
        with open(file) as f:
            query = f.read().strip()

        logger.info(f'executing query from {file}')
        self.cursor.execute(query) 
        self.connector.connection.commit()
        logger.info(f'sucessfuly executed query from {file}')

    def get_records(self):
        logger.info('getting records')
        return self.cursor.fetchall()

    def get_columns(self):
        return [desc[0] for desc in self.cursor.description]

    def populate_table(self, table_name, columns, values):
        logger.info(f'starting to populate table {table_name} with {len(values)} values')

        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES %s;"
        try:
            logger.info(f'executing query to populate table {table_name}')
            execute_values(self.cursor, query, values)
        except (psycopg2.Error, psycopg2.Warning) as e:
            logger.info(f'failed trying to populate table {table_name}: {e}')
            try:
                self.connector.connection.rollback()
                logger.info(f'transaction rolled back for table {table_name}')
            except psycopg2.Error as rb_e:
                logger.error(f'rollback failed during unexpected error handling for {table_name}: {rb_e}')
            return
        self.connector.connection.commit()
        logger.info(f'successful transaction of populating table {table_name}')
