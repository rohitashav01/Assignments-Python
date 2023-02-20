
class Mercedes:
    def  __init__(self,model):
        self.model=model
    
    def Price(self):
        if self.model=="Base":
            return "Price: 35Lacs"
        if self.model=="Middle":
            return "Price: 50Lacs"
        if self.model=="Top":
            return "Price: 70Lacs"

    def mileage(self):
        if self.model=="Base":
            return "Mileage:15Kmpl"
        if self.model=="Middle":
            return "Mileage:12Kmpl"
        if self.model=="Top":
            return "Mileage:10Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Automatic Thermal Management"

class Bmw:
    def  __init__(self,model):
        self.model=model
    
    def Price(self):
        if self.model=="Base":
            return "Price: 40Lacs"
        if self.model=="Middle":
            return "Price: 60Lacs"
        if self.model=="Top":
            return "Price: 90Lacs"

    def mileage(self):
        if self.model=="Base":
            return "Mileage:14Kmpl"
        if self.model=="Middle":
            return "Mileage:11Kmpl"
        if self.model=="Top":
            return "Mileage:9Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return " Thermal Management uses coolant and refrigerator circuits"
    

class Porsche:
    def  __init__(self,model):
        self.model=model
    
    def Price(self):
        if self.model=="Base":
            return "Price: 40Lacs"
        if self.model=="Middle":
            return "Price: 65Lacs"
        if self.model=="Top":
            return "Price: 95Lacs"

    def mileage(self):
        if self.model=="Base":
            return "Mileage:13Kmpl"
        if self.model=="Middle":
            return "Mileage:11Kmpl"
        if self.model=="Top":
            return "Mileage:7Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return " Automatic Thermal Management with coolant"
    

class Bentley:

    def  __init__(self,model):
        self.model=model
    
    def Price(self):
        if self.model=="Base":
            return "Price: 35Lacs"
        if self.model=="Middle":
            return "Price: 55Lacs"
        if self.model=="Top":
            return "Price: 78Lacs"

    def mileage(self):
        if self.model=="Base":
            return "Mileage:17Kmpl"
        if self.model=="Middle":
            return "Mileage:13Kmpl"
        if self.model=="Top":
            return "Mileage:12Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Thermal Management uses refrigerator circuits and coolant"
    

class Chrysler:
    def  __init__(self,model):
        self.model=model
    
    def Price(self):
        if self.model=="Base":
            return "Price: 30Lacs"
        if self.model=="Middle":
            return "Price: 45Lacs"
        if self.model=="Top":
            return "Price: 80Lacs"

    def mileage(self):
        if self.model=="Base":
            return "Mileage:15Kmpl"
        if self.model=="Middle":
            return "Mileage:12Kmpl"
        if self.model=="Top":
            return "Mileage:10Kmpl"

    def interior_sound(self):
        return "Interior sound powered with JBL sounds with extra bass"
    
    def thermal_mgmt(self):
        return "Thermal Management uses coolant"
    
    
def Factory(cars,model):
    # return eval(headphone)()

    cls_dict = {
        "mercedes":Mercedes(model),
        "bmw":Bmw(model),
        "porsche":Porsche(model),
        "bentley":Bentley(model),
        "chrysler":Chrysler(model)
    }
    return cls_dict[cars.lower()]


car_lst=[Mercedes,Bmw,Porsche,Bentley,Chrysler]
for x in car_lst:
    print("Price for Base Model:{} and Mileage:".format(x('Base').Price()),x('Base').mileage())
    print("Price for Middle Model:{} and Mileage:".format(x('Middle').Price()),x('Middle').mileage())
    print("Price for Top Model:{} and Mileage:".format(x('Top').Price()),x('Base').mileage())
  

