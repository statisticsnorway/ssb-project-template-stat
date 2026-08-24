import logging

from sqlalchemy import create_engine

from ssb_altinn_form_tools.default_form_extractor import DefaultFormExtractor
from ssb_altinn_form_tools.default_form_processor import DefaultFormProcessor
from ssb_altinn_form_tools.parquedit_storage_connector import (
    ParqueditStorageConnector,
)
from parquedit import ParquEdit

from config.config import settings


def pre_insert_operations(): ...


def get_extractor():
    return DefaultFormExtractor()


def get_storage_connector():
    conn = ParquEdit()
    return ParqueditStorageConnector(engine = conn)


def main_process_forms():
    processor = DefaultFormProcessor(
        form_name=settings.form_number,
        form_base_path=settings.form_folder,
        extractor=get_extractor(),
        connector=get_storage_connector(),
        alias_mapping={},
        checkbox_mapping=[],
    )
    processor.process_new_forms()


if __name__ == "__main__":
    main_process_forms()
