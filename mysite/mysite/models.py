from django.db import models

class Клиент(models.Model):
    имя = models.CharField(max_length=100)
    электронная_почта = models.EmailField()
    номер_телефона = models.CharField(max_length=20)
    адрес = models.CharField(max_length=200)
    дата_регистрации = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.имя

class Товар(models.Model):
    название = models.CharField(max_length=100)
    описание = models.TextField()
    цена = models.DecimalField(max_digits=10, decimal_places=2)
    количество = models.PositiveIntegerField()
    дата_добавления = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.название

class Заказ(models.Model):
    клиент = models.ForeignKey(Клиент, on_delete=models.CASCADE)
    товары = models.ManyToManyField(Товар)
    общая_сумма = models.DecimalField(max_digits=10, decimal_places=2)
    дата_оформления = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.дата_оформления}"

# Функции CRUD для модели Клиент

def создать_клиента(имя, электронная_почта, номер_телефона, адрес):
    клиент = Клиент(имя=имя, электронная_почта=электронная_почта, номер_телефона=номер_телефона, адрес=адрес)
    клиент.save()
    return клиент

def получить_клиентов():
    return Клиент.objects.all()

def получить_клиента_по_id(идентификатор):
    return Клиент.objects.get(id=идентификатор)

def обновить_клиента(клиент, имя, электронная_почта, номер_телефона, адрес):
    клиент.имя = имя
    клиент.электронная_почта = электронная_почта
    клиент.номер_телефона = номер_телефона
    клиент.адрес = адрес
    клиент.save()

def удалить_клиента(клиент):
    клиент.delete()

# Функции CRUD для модели Товар

def создать_товар(название, описание, цена, количество):
    товар = Товар(название=название, описание=описание, цена=цена, количество=количество)
    товар.save()
    return товар

def получить_товары():
    return Товар.objects.all()

def получить_товар_по_id(идентификатор):
    return Товар.objects.get(id=идентификатор)

def обновить_товар(товар, название, описание, цена, количество):
    товар.название = название
    товар.описание = описание
    товар.цена = цена
    товар.количество = количество
    товар.save()

def удалить_товар(товар):
    товар.delete()

# Функции CRUD для модели Заказ

def создать_заказ(клиент, товары, общая_сумма):
    заказ = Заказ(клиент=клиент, общая_сумма=общая_сумма)
    заказ.save()
    заказ.товары.set(товары)
    return заказ

def получить_заказы():
    return Заказ.objects.all()

def получить_заказ_по_id(идентификатор):
    return Заказ.objects.get(id=идентификатор)

def обновить_заказ(заказ, клиент, товары, общая_сумма):
    заказ.клиент = клиент
    заказ.товары.set(товары)
    заказ.общая_сумма = общая_сумма
    заказ.save()

def удалить_заказ(заказ):
    заказ.delete()