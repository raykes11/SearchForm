import re
from datetime import date, datetime
from typing import List, Any

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema, CoreSchema


class Date(date):
    """Custom date"""

    allowed_formats: List[str] = ["%d.%m.%Y", "%Y-%m-%d"]

    @classmethod
    def try_parse_date(cls, value: Any, info: core_schema.ValidationInfo) -> Any:
        if value.count('-'):
            try:
                value = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError('Error format Data, use form %d.%m.%Y or %Y-%m-%d')
        elif value.count('.'):
            try:
                value = datetime.strptime(value, "%d.%m.%Y").date()
            except ValueError:
                raise ValueError('Error format Data, use form %d.%m.%Y or %Y-%m-%d')
        else:
            raise ValueError('Error format Data, use form %d.%m.%Y or %Y-%m-%d')
        return value

    @classmethod
    def truncate_datetime(cls, value: Any, info: core_schema.ValidationInfo) -> Any:
        """If a datetime value is provided, truncate to a date"""
        if isinstance(value, datetime):
            return value.date()
        else:
            return value

    @classmethod
    def __get_pydantic_core_schema__(
            cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:

        return core_schema.chain_schema(
            [
                core_schema.with_info_plain_validator_function(
                    function=cls.truncate_datetime,
                ),
                core_schema.with_info_plain_validator_function(
                    function=cls.try_parse_date,
                )

            ]
        )


class PhoneNumber(str):
    """Custom number"""

    @classmethod
    def parse_number(cls, value: Any, info: core_schema.ValidationInfo) -> Any:
        if not isinstance(value, str):
            raise ValueError(f"{value} type{type(value)} not str ")
        if not re.match(r'^\+?\d{11}$', value):
            raise ValueError("Incorrect number format")
        else:
            return value

    @classmethod
    def __get_pydantic_core_schema__(
            cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:

        return core_schema.chain_schema(
            [
                core_schema.with_info_plain_validator_function(
                    function=cls.parse_number,
                )
            ]
        )
