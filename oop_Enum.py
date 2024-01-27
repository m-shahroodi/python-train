import enum
class Color(enum.Enum):
    Red = 1
    Blue = 2
    Green = 3
    Yellow = 4

print(Color.Yellow)
print(Color.Yellow.value)
print(Color.Yellow.name)