#1 Задание
import re


def extract_dates(text):
    pattern = r"\b(0[1-9]|[12][0-9]|3[01])([/\-.])(0[1-9]|1[0-2])\2(\d{4})\b"
    dates = re.findall(pattern, text)

    formatted_dates = [f"{day}{sep}{month}{sep}{year}" for day, sep, month, year in dates]

    return formatted_dates


text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."
dates = extract_dates(text)
print(dates)

#2 Задание
def split_tags(tag_string):
    tags = re.split(r'[,;/\\\s]+', tag_string)
    tags = [tag.strip() for tag in tags if tag.strip()]
    return tags

user_input = "Python, data-science / machine-learning; AI neural-networks"
tags = split_tags(user_input)
print(tags)