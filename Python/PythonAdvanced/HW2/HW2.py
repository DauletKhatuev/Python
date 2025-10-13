from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, ConfigDict

class Address(BaseModel):
    city: str = Field(min_length=2, description="Name of city")
    street: str = Field(min_length=3, description="Name of street")
    house_number: int = Field(gt=0, description="Number of house")
    model_config = ConfigDict(extra='forbid')


class User(BaseModel):
    name: str
    @field_validator('name')
    #Валидация для проверки имени
    def validate_name(cls, value):
        if not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters")
        return value
    is_employed: bool
    age: int = Field(ge=0, le=120, description="Age of user")
    email: EmailStr
    @model_validator(mode='after')
    def validate_employment_age(self):
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError("If user works, age must be between 18 and 65")
        return self
    address: Address

    #Конфигурирование сериализации
    model_config = ConfigDict(
        validate_assignment=True,  # повторная валидация при изменении
        extra='forbid',            # запрет лишних полей
        str_strip_whitespace=True, # автоматически обрезает пробелы
        title='User model example' # метаданные
    )
