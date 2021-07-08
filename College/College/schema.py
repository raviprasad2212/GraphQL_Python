from graphene import Schema, ObjectType
from CSEbranch.schema import ShowAvgAge

class Query(ShowAvgAge, ObjectType):
    pass

schema = Schema(query=Query)