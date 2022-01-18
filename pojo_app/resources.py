from import_export import resources
from . models import Pojo_Data

class PojoResource(resources.ModelResource):
    class meta:
        model = Pojo_Data