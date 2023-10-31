class Worker:
    name = str,
    age = int,
    zp = int,
    hours = int

    def zarplata(zp, hours):
        return zp * hours
    
aldiyar = Worker(
    name = 'aldiyar', age = 14, zp = 5000, hours = 8 
)

print(aldiyar.zarplata)
    
