from graphene import ObjectType, Float, Field, Int
from django.db.models import Avg, Max
from .models import Students

# Mention to print data in the Graphql server
class Student_avg_age(ObjectType):
    averageAGeStudent = Float()
    maxage = Int()

# Actual method implementation in class
class ShowAvgAge(ObjectType):

    showavg = Field(Student_avg_age)

    def resolve_showavg(self, info):
        get_avg_age = Students.objects.aggregate(Avg('age'))
        max_age = Students.objects.aggregate(Max('age'))
        return Student_avg_age(averageAGeStudent=get_avg_age.get('age__avg'), maxage = max_age.get('age__max'))
