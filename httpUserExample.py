from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1-3 seconds between tasks
    
    @task
    def post_item(self):
        # POST request to the items endpoint
        payload = {"name": "test"}
        headers = {"Content-Type": "application/json"}
        
        with self.client.post(
            "/items", 
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:
            if response.status_code == 200 or response.status_code == 201:
                response.success()
            else:
                response.failure(f"Failed with status code: {response.status_code}")

# To run this script:
# locust -f locust_file.py --host=http://stress.qaclan.com


# from locust import between, task, SequentialTaskSet, HttpUser


# class ViewCart(SequentialTaskSet):
#     @task
#     def get_all_cart_tem(self):
#         with self.client.get("/index.php?controller=order", catch_response=True) as response:
#             if response.status_code != 200:
#                 response.failure("Failed to get all cart items, StatusCode: " + str(response.status_code))
#             else:
#                 if "Shopping-cart summary" in response.text:
#                     response.success()
#                 else:
#                     response.failure("Failed to get all cart items, Text: " + response.text)

#     @task
#     def exit_navigation(self):
#         self.interrupt()


# class MyUser(HttpUser):
#     wait_time = between(1, 2)
#     tasks = [ViewCart]




