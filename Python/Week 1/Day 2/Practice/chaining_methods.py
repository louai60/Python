class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("user Information:")
        print(f"first Name: {self.first_name}")
        print(f"last Name: {self.last_name}")
        print(f"e-mail: {self.email}")
        print(f"age: {self.age}")
        print(f"rewards member: {self.is_rewards_member}")
        print(f"gold card points: {self.gold_card_points}")
        return self  
    
    def enroll(self):
        if self.is_rewards_member:
            print("user already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self  
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("not enough points.")
        else:
            self.gold_card_points -= amount
            print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
        return self  


print("\nUser 1:")
user1 = User("Louay", "Saafi", "louay.saafi@example.com", 30)
user1.display_info().enroll().spend_points(50).display_info()

print("\nUser 2:")
user2 = User("Aziz", "Kouki", "aziz.kouki@example.com", 25)
user2.enroll().spend_points(80).display_info()
