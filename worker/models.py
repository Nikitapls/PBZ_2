from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)
    min_salary = models.FloatField()

    def __str__(self):
        return self.name


class Level(models.Model):
    level_number = models.IntegerField(unique=True)
    rate = models.FloatField()

    def __str__(self):
        return str(self.level_number)


class Tax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return self.name


class Premium(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField()

    def __str__(self):
        return self.name


class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey(to=Position, on_delete=models.SET_NULL, null=True)
    part_of_special_community = models.BooleanField()
    level = models.ForeignKey(to=Level, on_delete=models.SET_NULL, blank=True, null=True)
    taxes = models.ManyToManyField(to=Tax, swappable=True, blank=True)
    premiums = models.ManyToManyField(to=Premium, swappable=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_month_payroll(self, amount_of_month=1):
        salary_max = (self.position.min_salary * (
            self.level.rate)) + self.position.min_salary if self.level else self.position.min_salary
        salary = salary_max
        for tax in self.taxes.all():
            salary -= (salary_max * tax.rate)
        for premium in self.premiums.all():
            salary += (salary_max * premium.rate)
        if self.part_of_special_community:
            salary -= salary_max * 0.01
        return salary * amount_of_month

    def get_dict(self):
        return {
            'name': self.first_name + ' ' + self.last_name,
            'position': {'name': self.position.name, 'min_salary': self.position.min_salary},
            'part_of_special_community': self.part_of_special_community,
            'level': None if not self.level else {'number': self.level.level_number, 'rate': self.level.rate * 100},
            'payroll': self.get_month_payroll(),
            'id': self.id
        }
