from faker import Faker
fake = Faker()

def get_registered_user():
    return{
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


#Incase if you want to print
if __name__ == "__main__":
    print(get_registered_user())