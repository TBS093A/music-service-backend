from django.db import models

class OneToManyModel(models.Model):

    def fromDict(self, dict):
            self.__dict__.update(dict)
        
    def create(self, dict):
        new_object = self()
        new_object.fromDict(dict)
        new_object.save()
        return new_object

    def update(self, dict):
        self.fromDict(dict)
        self.save()
        return self

    class Meta:
        abstract = True