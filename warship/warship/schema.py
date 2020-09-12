import graphene


class Interceptor(graphene.ObjectType):
    name = graphene.String()

    def resolve_name(self, info):
        return 'hello, world!'


schema = graphene.Schema(query=Interceptor)