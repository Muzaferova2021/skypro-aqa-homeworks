from Address import Address
from Address import Mailing


newAddress_to=Address("623100","Pervouralsk","Lenina","4","44")
newAddress_From=Address("123456","Ekaterinburg","Malinina","12","45")
newMailing=Mailing(newAddress_to,newAddress_From,1000,"ru123456789")


print("Отправление",newMailing.track,"из",newAddress_to.city,newAddress_to.street,newAddress_to.house,"-",newAddress_to.flat,"в",newAddress_From.city,newAddress_From.street,newAddress_From.house,"-",newAddress_From.flat,".",newMailing.cost,"рублей.")