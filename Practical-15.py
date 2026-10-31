
import gc

# Enable garbage collection
gc.enable()

print("Garbage Collection Enabled:", gc.isenabled())

# Create a class
class Demo:
    def __init__(self, name):
        self.name = name

# Create objects
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

print("\nObjects created successfully.")

# Create circular references
obj1.ref = obj2
obj2.ref = obj1

# Delete references
del obj1
del obj2

print("\nObjects deleted.")

# Display garbage collection count
print("Garbage before collection:", gc.get_count())

# Perform manual garbage collection
collected = gc.collect()

print("Garbage collected:", collected)

# Disable garbage collection
gc.disable()

print("\nGarbage Collection Enabled:", gc.isenabled())

# Enable garbage collection again
gc.enable()

print("Garbage Collection Enabled:", gc.isenabled())