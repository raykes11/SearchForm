from typing import Any, Dict, Type, List

from pydantic import BaseModel, EmailStr, create_model, TypeAdapter

from .custom_pydantic_class import Date, PhoneNumber
from db_tiny.tinyDB import tinydb_form

""" Функция для динамического создания модели на основе словаря (dict) """


def create_pydantic_model(data: Dict[str, Any]) -> Type[BaseModel]:
    fields = {}
    # Динамически добавляем поля в модель в зависимости от названия
    for name, value in data.items():
        if value == "data":
            fields[name] = (Date, ...)
        elif value == "phone":
            fields[name] = (PhoneNumber, ...)
        elif value == "email":
            fields[name] = (EmailStr, ...)  # Для email используем встроенный EmailStr
        elif name == "name":
            pass
        else:
            fields[name] = (str, ...)  # Для других полей используем строку

    # Динамически создаем модель с использованием Pydantic
    name: str = data["name"]
    name.title()
    return create_model(name, **fields)


""" Запрос всех Pydantic model """


def all_pydantic_model() -> List[Type[BaseModel]]:
    list_pydantic_models = []
    list_forms = tinydb_form()
    for form in list_forms:
        pydantic_model = create_pydantic_model(form)
        list_pydantic_models.append(pydantic_model)
    return list_pydantic_models


""" Индификация модели с использованием Pydantic """


def identify_model(
    data: Dict[str, Any], models: List[Type[BaseModel]]
) -> str | Dict[str, Any]:
    for model in models:
        try:
            # Пытаемся провести валидацию
            validated_model = model.model_validate(data)
            return f"Model: {model.__name__}"
        except Exception:
            continue

    return parser_dict(data)


""" Определение типов данных с использованием Pydantic """


def parser_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    models_type = {
        "data": TypeAdapter(Date),
        "phone": TypeAdapter(PhoneNumber),
        "email": TypeAdapter(EmailStr),
        "str": TypeAdapter(str),
    }
    fields = {}
    for name, value in data.items():
        for type, model in models_type.items():
            try:
                value = model.validate_python(value)
                fields[name] = type
                break
            except Exception:
                continue
    return fields
