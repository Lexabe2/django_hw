from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    date_of_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.number_phone} - ' \
               f'{self.address} - {self.date_of_registration}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    prace = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.prace} - ' \
               f'{self.quantity} - {self.photo}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Заказ #{self.id} от {self.registration_date}"


def add_client(name, email, number_phone, address):
    client = Client(name=name, email=email,
                    number_phone=number_phone, address=address)
    client.save()
    return client


def return_client():
    return Client.objects.all()


def filter_client_name(name):
    return Client.objects.get(name=name)


def update_client(client, name, email, number_phone, address):
    client.name = name
    client.email = email
    client.number_phone = number_phone
    client.address = address
    client.save()


def del_client(client):
    client.delete()


def add_product(title, description, prace, quantity):
    product = Product(title=title, description=description, prace=prace,
                      quantity=quantity)
    product.save()
    return product


def return_product():
    return Product.objects.all()


def filter_product_title(title):
    return Product.objects.get(title=title)


def update_product(product, title, description, prace, quantity):
    product.title = title
    product.description = description
    product.prace = prace
    product.quantity = quantity
    product.save()


def del_product(product):
    product.delete()


def add_Order(client, products, total_cost):
    order = Order(client=client, total_cost=total_cost)
    order.save()
    order.products.set(products)
    return order


def return_order():
    return Order.objects.all()


def filter_order_title(total_cost):
    return Order.objects.get(total_cost=total_cost)


def update_order(order, client, products, total_cost):
    order.client = client
    order.products.set(products)
    order.total_cost = total_cost
    order.save()


def del_order(order):
    order.delete()
