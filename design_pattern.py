
class Mercedes:
    def  __init__(self):
        self.model = None
    
    def Price(self):
        if self.model=="Base".lower():
            return "Price: 35Lacs"
        if self.model=="Middle".lower():
            return "Price: 50Lacs"
        if self.model=="Top".lower():
            return "Price: 70Lacs"

    def mileage(self):
        if self.model=="Base".lower():
            return "Mileage:15Kmpl"
        if self.model=="Middle".lower():
            return "Mileage:12Kmpl"
        if self.model=="Top".lower():
            return "Mileage:10Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Automatic Thermal Management"

class Bmw: 
    def  __init__(self):
        self.model = None
    
    def Price(self):
        if self.model=="Base".lower():
            return "Price: 40Lacs"
        if self.model=="Middle".lower():
            return "Price: 60Lacs"
        if self.model=="Top".lower():
            return "Price: 90Lacs"

    def mileage(self):
        if self.model=="Base".lower():
            return "Mileage:14Kmpl"
        if self.model=="Middle".lower():
            return "Mileage:11Kmpl"
        if self.model=="Top".lower():
            return "Mileage:9Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return " Thermal Management uses coolant and refrigerator circuits"
    

class Porsche:
    def  __init__(self):
        self.model=None
    
    def Price(self):
        if self.model=="Base".lower():
            return "Price: 40Lacs"
        if self.model=="Middle".lower():
            return "Price: 65Lacs"
        if self.model=="Top".lower():
            return "Price: 95Lacs"

    def mileage(self):
        if self.model=="Base".lower():
            return "Mileage:13Kmpl"
        if self.model=="Middle".lower():
            return "Mileage:11Kmpl"
        if self.model=="Top".lower():
            return "Mileage:7Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return " Automatic Thermal Management with coolant"
    

class Bentley:
    def __init__(self):
        self.model=None
    
    def Price(self):
        if self.model=="Base".lower():
            return "Price: 35Lacs"
        if self.model=="Middle".lower():
            return "Price: 55Lacs"
        if self.model=="Top".lower():
            return "Price: 78Lacs"

    def mileage(self):
        if self.model=="Base".lower():
            return "Mileage:17Kmpl"
        if self.model=="Middle".lower():
            return "Mileage:13Kmpl"
        if self.model=="Top".lower():
            return "Mileage:12Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Thermal Management uses refrigerator circuits and coolant"
    

class Chrysler: 
    def __init__(self):
        self.model= None
    
    def Price(self):
        if self.model=="Base".lower():
            return "Price: 30Lacs"
        if self.model=="Middle".lower():
            return "Price: 45Lacs"
        if self.model=="Top".lower():
            return "Price: 80Lacs"

    def mileage(self):
        if self.model=="Base".lower():
            return "Mileage:15Kmpl"
        if self.model=="Middle".lower():
            return "Mileage:12Kmpl"
        if self.model=="Top".lower():
            return "Mileage:10Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Thermal Management uses coolant"
    
    
def Factory(cars):

    cls_dict = {
        "mercedes":Mercedes(),
        "bmw":Bmw(),
        "porsche":Porsche(),
        "bentley":Bentley(),
        "chrysler":Chrysler()
    }
    return cls_dict[cars.lower()]


car_lst=["mercedes","bmw","porsche","bentley","chrysler"]
for x in car_lst:
    obj=Factory(x)
    print("---------------------------Base Models of All Brands---------------------------------------------")
    obj.model="base"
    print("Price for Base Model:{} and Mileage:{}".format(obj.Price(),obj.mileage()))

    print("---------------------------Mid Models of All Brands----------------------------------------------")
    obj.model="middle"
    print("Price for Middle Model:{} and Mileage:{}".format(obj.Price(),obj.mileage()))

    print("---------------------------Top Models of All Brands----------------------------------------------")
    obj.model="top"
    print("Price for Top Model:{} and Mileage:{}".format(obj.Price(),obj.mileage()))
  

