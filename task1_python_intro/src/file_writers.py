import json
import logging
import xml.etree.ElementTree as ET
from xml.dom import minidom

logger = logging.getLogger(__name__)


class JsonWriter:
    def __init__(self):
       logger.info('JsonWriter initialized')

    def write_to_file(self,
                      file_path: str,
                      data: list | tuple, 
                      column_names: list[str]):
        if not column_names:
            logger.error('Column names list cannot be empty')
            raise ValueError('Column names list cannot be empty')

        if not data:
            logger.error('data list cannot be empty')
            raise ValueError('data list cannot be empty')
        
        if not file_path.endswith('.json'):
            file_path += '.json'

        num_columns = len(column_names)
        list_of_dicts = []

        for i, row in enumerate(data):
            if len(row) != num_columns:
                error_msg = (
                    f'Row {i+1} has {len(row)} values, but {num_columns} column names were provided'
                    f'Row data: {row}'
                )
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            record = dict(zip(column_names, row))
            list_of_dicts.append(record)

        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(list_of_dicts, json_file, indent=4, ensure_ascii=False)
            logger.info(f'Successfully wrote {len(list_of_dicts)} records to {file_path}')
        except Exception as e:
            logger.error(f'Failed to write to file {file_path}: {e}', exc_info=True)



class XmlWriter:
    def __init__(self):
        logger.info('XmlWriter initialized')

    def _is_valid_xml_tag(self, tag: str) -> bool:
        if not tag or not isinstance(tag, str):
            return False
        if ' ' in tag: 
            return False
        if not tag[0].isalpha() and tag[0] != '_':
             pass
        return True

    def write_to_file(self,
                      file_path: str,
                      data: list | tuple,
                      column_names: list[str]):
        
        root_element_name: str = 'data'
        row_element_name: str = 'record'

        if not column_names:
            logger.error('Column names list cannot be empty')
            raise ValueError('Column names list cannot be empty')

        if not data:
            logger.error('Data list cannot be empty')
            raise ValueError('Data list cannot be empty')

        if not file_path.endswith('.xml'):
            file_path += '.xml'

        for col_name in column_names:
            if not self._is_valid_xml_tag(col_name):
                msg = f'Column name \'{col_name}\' is not a valid XML tag. Check for spaces or invalid starting characters.'
                logger.error(msg)
                raise ValueError(msg)

        num_columns = len(column_names)
        
        try:
            root = ET.Element(root_element_name)
        except ValueError as e: 
            logger.error(f'Failed to create root XML element \'{root_element_name}\': {e}')
            raise ValueError(f'Invalid root element name \'{root_element_name}\': {e}') from e

        for i, row_data_item in enumerate(data):
            if not isinstance(row_data_item, (list, tuple)):
                error_msg = f'Row {i+1} is not a list or tuple. Row data: {row_data_item}'
                logger.error(error_msg)
                raise ValueError(error_msg)

            if len(row_data_item) != num_columns:
                error_msg = (
                    f'Row {i+1} has {len(row_data_item)} values, but {num_columns} column names were provided. '
                    f'Row data: {row_data_item}'
                )
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            try:
                row_element = ET.SubElement(root, row_element_name)
            except ValueError as e:
                 logger.error(f'Failed to create row XML element \'{row_element_name}\': {e}')
                 raise ValueError(f'Invalid row element name \'{row_element_name}\': {e}') from e

            for col_idx, col_name in enumerate(column_names):
                try:
                    value = row_data_item[col_idx]
                    col_element = ET.SubElement(row_element, col_name)
                    col_element.text = str(value) 
                except ValueError as e: 
                    logger.error(f'Failed to create column XML element \'{col_name}\': {e}')
                    raise ValueError(f'Invalid column name \'{col_name}\': {e}') from e
                except IndexError:
                    error_msg = f'Index error for column \'{col_name}\' in row {i+1}.'
                    logger.error(error_msg)
                    raise ValueError(error_msg)

        try:
            rough_string = ET.tostring(root, encoding='utf-8', method='xml')
            parsed_string = minidom.parseString(rough_string)
            pretty_xml_as_string = parsed_string.toprettyxml(indent='    ', encoding='utf-8')
        except Exception as e:
            logger.error(f'Failed to generate or pretty-print XML for {file_path}: {e}', exc_info=True)
            pretty_xml_as_string = rough_string 

        try:
            with open(file_path, 'wb') as xml_file: 
                xml_file.write(pretty_xml_as_string)
            logger.info(f'Successfully wrote {len(data)} records to {file_path}')
        except Exception as e:
            logger.error(f'Failed to write to file {file_path}: {e}', exc_info=True)

