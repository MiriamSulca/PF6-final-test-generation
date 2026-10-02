import json 
import requests

def dish_fetch(num):
    response= requests.get("https://api-colombia.com/api/v1/TypicalDish")
    Typical_Dishes =json.loads(response.content)
    if 1 <= num <= len(Typical_Dishes):
        return {Typical_Dishes[num - 1]["name"]}
    else:
        return {}

def main():
  print("Hello learners!")
  num = int(input("ingresa un número"))
  dish = dish_fetch(num)
  if dish:
     print(f"Typical Dish: {dish}")
  else:
     print("elija otro número")
if __name__=="__main__":
  main()



  
  