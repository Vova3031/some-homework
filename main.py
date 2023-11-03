import random
brands_of_car = {
    "BMW": {'fuel': 100, "strength": 100, 'consumption': 6},
    "Ford": {'fuel': 80, "strength": 80, 'consumption': 8},
    "Lada": {'fuel': 40, "strength": 20, 'consumption': 12},
    "Volvo": {'fuel': 60, "strength": 150, 'consumption': 10}
}
job_list = {
    "Java developer": {"salary": 50, "gladness_less": 20},
    "C++ developer": {"salary": 80, "gladness_less": 40},
    "Python developer": {"salary": 40, "gladness_less": 60},
    "Php developer": {"salary": 30, "gladness_less": 10},
}
class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0
class Car:
    def __init__(self, brand=None):
        self.brand = brand
        self.fuel = 0
        self.strength = 0
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job if job is not None else {}
        self.home = home if home is not None else Home()
        self.car = car if car is not None else Car()
    def eat(self):
        self.satiety += 10
        self.home.food -= 1
    def clean_home(self):
        self.home.mess -= 10
        self.gladness += 5
    def chill(self):
        self.gladness += 10
    def work(self):
        self.money += self.job["salary"]
        self.gladness -= self.job["gladness_less"]
    def to_repair(self):
        self.car.strength += 10
    def shopping(self, manage):
        if manage == "delicacies":
            self.money -= 20
            self.satiety += 10
    def get_car(self):
        brands = list(brands_of_car.keys())
        brand = random.choice(brands)
        self.car = Car(brand)
    def get_job(self):
        jobs = list(job_list.keys())
        job = random.choice(jobs)
        self.job = job_list[job]
    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
    def is_alive(self):
      if self.gladness < 0:
          print("Depression!")
          return False
      if self.satiety < 0:
          print("Dead.....")
          return False
      if self.money < -500:
          print('Bankrupt...')
          return False
      print(f"I don't have a job, I'm going to get a job with salary {self.job.get('salary', 0)}")
      dice = random.randint(1, 4)
      if self.satiety < 20:
          print("I'll go eat")
          self.eat()
      elif self.gladness < 20:
          if self.home.mess > 15:
              print("I want to chill, but there is so much mess...\nSo I will clean the house ")
              self.clean_home()
          else:
              print("Let's chill!")
              self.chill()
      elif self.money < 0:
          print("Start working")
          self.work()
      elif self.car.strength < 15:
          print("I need to repair my car")
          self.to_repair()
      elif dice == 1:
          print("Let's chill!")
          self.chill()
      elif dice == 2:
          print("Start working")
          self.work()
      elif dice == 3:
          print("Cleaning time!")
          self.clean_home()
      elif dice == 4:
          print("Time for treats!")
          self.shopping(manage="delicacies")
      if self.car.brand is None:
          self.get_car()
          print(f"I bought a car {self.car.brand}")
      if self.job.get('salary') is None:
          self.get_job()
          print(f"I don't have a job, I'm going to get a job {self.job} with salary {self.job.get('salary', 0)}")
      self.days_indexes("day")
if __name__ == "__main__":
    human = Human()
    human.is_alive()
