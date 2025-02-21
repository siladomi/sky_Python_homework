
from smartphone import Smartphone

catalog = [
    Smartphone(brand="Apple", model="iPhone 11", phone_number="+79324012357"),
    Smartphone(brand="Tecno", model="pova 5", phone_number="+79048790129"),
    Smartphone(brand="samsung", model="a54", phone_number="+79029607178"),
    Smartphone(brand="Huawei", model="P40 lite", phone_number="+79222566300"),
    Smartphone(brand="Google", model="Pixel 6", phone_number="+79044713595")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")