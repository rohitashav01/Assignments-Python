class Employee:
    _name = None

    def __new__(cls):
        if cls._name is None:
            print("Creating object using new")
            cls._name = super().__new__(cls)
            return cls._name
        else:
            raise Exception('class can have only one object')
            
obj1=Employee()
print(obj1)

#obj2=Employee()
#print(obj2)