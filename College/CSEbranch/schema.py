from graphene import ObjectType, Float, Field
from django.db.models import Avg, Max
from .models import Students

# Mention to print data in the Graphql server
class Student_avg_age(ObjectType):
    averageAGeStudent = Float()

# Actual method implementation in class
class ShowAvgAge(ObjectType):

    showavg = Field(Student_avg_age)

    def resolve_showavg(self, info):
        get_avg_age = Students.objects.aggregate(Avg('age'))
        return Student_avg_age(averageAGeStudent=get_avg_age.get('age__avg'))
