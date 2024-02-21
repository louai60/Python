class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("user details:")
        print("first name:", self.first_name)
        print("last name:", self.last_name)
        print("email:", self.email)
        print("age:", self.age)
        print("rewards member:", self.is_rewards_member)
        print("gold card points:", self.gold_card_points)
        print('-' *40)

    def enroll(self):
        if self.is_rewards_member:
            print("user already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("enrolled succesfully !!!")
        print('-' *40)

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{amount} points spent succesfully.")
        else:
            print("not enough points to spend.")
        print('-' *40)

#user instances
user1 = User("Louay", "Saafi", "louay.saafi@example.com", 25)
user2 = User("Hama", "Hama", "hama.hama@example.com", 30)
user3 = User("Aziz", "Kouki", "aziz.kouki@example.com", 35)

#display info
user1.display_info()
user2.display_info()
user3.display_info()

#enroll users
user1.enroll()
user2.enroll()

#spend points
user1.spend_points(50)
user2.spend_points(80)
user3.spend_points(40)

#display updated user info
user1.display_info()
user2.display_info()
user3.display_info()

#re-enroll the first user
user1.enroll()


user3.spend_points(40)
