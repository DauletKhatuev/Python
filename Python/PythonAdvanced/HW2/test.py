import HW2

json_input = """
{
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "New York",
        "street": "5th Avenue",
        "house_number": 123
    }
}
"""
try:

    user = HW2.User.model_validate_json(json_input)
    print(user)
except Exception as e:
    print("Ошибка: ", e)