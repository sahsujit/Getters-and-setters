class myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"The value is : {self._value}")
    # Getters
    @property
    def ten_value(self):
        return 10* self._value
    # Setters
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/5
obj=myclass(10)
obj.show()
obj.ten_value=100
print(obj.ten_value)

        
    
