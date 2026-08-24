import logging

from sqlalchemy import create_engine

from ssb_altinn_form_tools.batch_form_processor import BatchFormProcessor
from ssb_altinn_form_tools.default_form_extractor import DefaultFormExtractor
from ssb_altinn_form_tools.default_form_processor import DefaultFormProcessor
from ssb_altinn_form_tools.sqlalchemy_storage_connector import (
    SqlAlchemyStorageConnector,
)

from config.config import settings


def pre_insert_operations(): ...


def get_extractor():
    return DefaultFormExtractor()


def get_storage_connector():
    engine = engine = create_engine("sqlite:///./db.db", echo=False)
    return SqlAlchemyStorageConnector(engine)


def main_process_forms():
    processor = BatchFormProcessor(
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