from abc import abstractmethod,ABC






class Structure:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('expected {} arguments.'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self,name, value)
        for name in self._fields[len(args):]:
            setattr(self,name,kwargs.pop(name))

class AutoSaved:
    def __init__(self, storage_name):
        self.storage_name = storage_name
    def __get__(self, instance,owner):
        if instance is None:
            return self
        return instance.__dict__[self.storage_name]
    def __set__(self, instance, value):
        instance.__dict__[self.storage_name] = value
        
class Validate(ABC, AutoSaved):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance,value)

    @abstractmethod
    def validate(self, instance, value):
        """return validate value or value error"""


class NonBlank(Validate):
    def validate(self, instance, value):
        if not value.strip():
            raise ValueError('no empty value')
        return value
class NonInt(Validate):
    def validate(self, instance, value):
        if isinstance(value, int):
            raise TypeError('no int value')
        return value


class Descriptor:
    def __init__(self, name,**kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        

class Typed(Descriptor):
    expected_type = type(None)
    
    def __set__(self,instance,value):
        if not isinstance(instance, self.expected_type):
            raise TypeError('expected {} '.format(str(self.expected_type)))
        super().__set__(instance, value)
        


if __name__ == '__main__':
    class A:
        name = NonBlank('name')
        price=NonInt('price')
        def __init__(self, name,price):
            self.name = name
            self.price=price

    foo = A(' ',11)
    print(foo.name)    
    print(foo.price)    

