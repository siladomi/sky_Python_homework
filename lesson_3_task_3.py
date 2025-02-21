from Address import Address
from mailing import Mailing

to_address = Address(index="308007", city="Белгород", street="Гагарина", house="20", apartment="1")
from_address = Address(index="628400", city="Сургут", street="наб. Ивана Кайдалова", house="28", apartment="207")

mailing = Mailing(to_address=to_address, from_address=from_address, cost=420, track="10084693829")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
