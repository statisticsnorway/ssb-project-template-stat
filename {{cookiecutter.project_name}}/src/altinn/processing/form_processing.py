import logging

from sqlalchemy import create_engine

from ssb_altinn_form_tools.default_form_extractor import DefaultFormExtractor
from ssb_altinn_form_tools.default_form_processor import DefaultFormProcessor
from ssb_altinn_form_tools.parquedit_storage_connector import (
    ParqueditStorageConnector,
)
from ssb_parquedit import ParquEdit

from config.config import settings


def pre_insert_operations(): ...


def get_extractor():
    return DefaultFormExtractor()


def get_storage_connector():
    conn = ParquEdit()
    return ParqueditStorageConnector(engine=conn)


def main_process_forms():
    for form in settings.form_numbers:
        processor = DefaultFormProcessor(
            form_name=form,
            form_base_path=f"{settings.form_folder}/{form}",
            extractor=get_extractor(),
            connector=get_storage_connector(),
            alias_mapping={},
            checkbox_mapping=[],
        )
        processor.process_new_forms()


if __name__ == "__main__":
    main_process_forms()
