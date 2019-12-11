#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Car(object):
    def __init__(self, brand) -> None:
        self.brand = brand


# In[13]:


class CarsLazyInit(object):
    def __init__(self):
        self.list = {}
    
    def get_car(self, car):
        if car not in self.list:
            print("Carro não existe, criando carro...")
            self.list[car] = Car(car)
        
        return "Memory Address: {} | Carro criado: {}".format(self.list[car], self.list[car].brand)


# In[17]:


class Cars(object):
    def __init__(self):
        self.list = {}
    
    def get_car(self, car):
        if car not in self.list:
            print("Carro não existe, criando carro...")
            self.list[car] = Car(car)
        
        return "Memory Address: {} | Carro criado: {}".format(self.list[car], self.list[car].brand)


# In[18]:


if __name__ == '__main__':
    cars = CarsLazyInit()


# In[19]:


print(cars.get_car('Fiat'))
print(cars.get_car('Fiat'))
print(cars.get_car('Honda'))


# In[ ]:




