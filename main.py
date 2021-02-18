import time


def logger(func):
  def wrapper(*args, **kwargs):
    file = open(kwargs.get('path'), "a")
    lagr = []
    for arg in args:
      lagr.append(arg)
    local_time = time.localtime()
    date_and_time = str(local_time.tm_mday) + "." + str(local_time.tm_mon) + "." + str(local_time.tm_year) + " " + str(local_time.tm_hour) + ":"
    if(local_time.tm_min < 10): 
      date_and_time += "0" + str(local_time.tm_min)
    else:
      date_and_time += str(local_time.tm_min)
    file.write("Время выполнения функции: {}".format(date_and_time) + "\n")
    file.write("Название функции: {}".format(func.__name__) + "\n")
    file.write("Аргументы и переменные функции: {}".format(lagr) + "\n")
    result = func(*args)
    file.write("Результат выполнения: {}".format(str(result)) + "\n")
    file.write("------\n")
  return wrapper


class Goose:
  eggs = 0
  voice = 'Гуси гогочут' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice)


class Cow:
  milk = 0
  voice = 'Коровы мычат' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.milk += food // 2
  
  def colect(self):
    print('Собрано', self.milk, 'литров молока')
    self.milk = 0

  def song(self):
    print(self.voice)


class Sheep:
  wool = 0
  voice = 'Овцы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.wool += food // 2
  
  def colect(self):
    print('Собрано', self.wool, 'килограммов шерсти')
    self.wool = 0

  def song(self):
    print(self.voice)


class Chicken:
  eggs = 0
  voice = 'Курица кудахчет' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice)


class Goat:
  milk = 0
  voice = 'Козы блеют' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.milk += food // 2
  
  def colect(self):
    print('Собрано', self.milk, 'литров молока')
    self.milk = 0

  def song(self):
    print(self.voice)


class Duck:
  eggs = 0
  voice = 'Утка крякает' 
  
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  
  def eat(self, food):
    self.weight += food
    self.eggs += food // 2
  
  def colect(self):
    print('Собрано', self.eggs, 'яиц')
    self.eggs = 0

  def song(self):
    print(self.voice) 

@logger
def max_weight(dict):
  max = 0
  name_max = ''
  for animal in animals:
    if animal.weight > max:
      max = animal.weight
      name_max = animal.name
  print(name_max)
  return name_max

@logger
def total_weight(dict):
  total_weight = 0
  for animal in animals:
    total_weight += animal.weight
  print('Общий вес всех животных', total_weight)
  return total_weight


white = Goose('Белый', 3)
gray = Goose('Серый', 4)
manka = Cow('Манька', 400)
lamb = Sheep('Барашек', 100)
curly = Sheep('Кудрявый', 90)
coco = Chicken('Ко-ко', 2)
kuka = Chicken('Кукареку', 1)
horns = Goat('Рога', 70)
hooves = Goat('Копыта', 90)
mallard = Duck('Кряква', 1)

animals =(white, gray, manka, lamb, curly, coco, kuka, horns, hooves, mallard)

max_weight(animals, path = "logger.txt")
total_weight(animals, path = "logger.txt")