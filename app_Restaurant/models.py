from django.db import models as m


class Supplier(m.Model):  # Supplier - Поставик
    name = m.CharField(max_length=30)

    def __str__(self):
        return self.name


class Stuff(m.Model):  # Stuff - Персонал
    firstname = m.CharField(max_length=30)
    lastname = m.CharField(max_length=30)
    age = m.IntegerField()

    def __str__(self):
        return self.firstname, self.lastname


class EnergySupply(m.Model):    # EnergySupply - Электроснабжение
    energy_name = m.CharField(max_length=40)

    def __str__(self):
        return self.energy_name


class WaterSupply(m.Model):     # WaterSupply - Водоснабжение
    water_name = m.CharField(max_length=40)

    def __str__(self):
        return self.water_name


class Restaurant (m.Model):
    title = m.CharField(max_length=40)
    supplier = m.ManyToManyField(Supplier)
    stuff = m.ManyToManyField(Stuff)
    restaurant_area = m.FloatField()
    kitchen_theme = m.CharField(max_length=40)
    restaurant_year = m.DateField()
    water_supply = m.OneToOneField(WaterSupply, on_delete=m.SET_NULL, null=True)
    energy_supply = m.OneToOneField(EnergySupply, on_delete=m.SET_NULL, null=True)

    def __str__(self):
        return self.title