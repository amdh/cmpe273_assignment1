from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):            
        return {obj: getattr(self, obj) for obj in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(objlist):
      
        return [obj.serialize() for obj in objlist]