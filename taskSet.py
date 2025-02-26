from locust import User, between, task, SequentialTaskSet, TaskSet

class SearchProduct(SequentialTaskSet):
    @task(4)
    def search_men_products(self):
        print("Searching men products")

    @task(1)
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]