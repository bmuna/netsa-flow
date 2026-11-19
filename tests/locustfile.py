
import random as random_module
from locust import HttpUser, task, between
# import random


# class LoginUser(HttpUser):
#     wait_time = between(0, 0)

#     ip_addresses = [
#         "192.168.1.10",
#         "192.168.1.20",
#         "192.168.1.30",
#     ]

#     @task
#     def login(self):
#         simulated_ip = random.choice(self.ip_addresses)

#         self.client.post(
#             "/api/login/",
#             headers={
#                 # "X-Test-Client-IP": simulated_ip,
#                 "X-Test-Client-IP": "192.168.1.99",
#             },
#             json={
#                 "username": "ip_throttle_test_user",
#                 "password": "WrongPassword123!"
#             }
#         )




# class LoginUser(HttpUser):
#     wait_time = between(0, 0)

#     ip_addresses = [
#         "192.168.1.10",
#         "192.168.1.20",
#         "192.168.1.30",
#     ]

#     @task
#     def login(self):
#         simulated_ip = random.choice(self.ip_addresses)

#         self.client.post(
#             "/api/login/",
#             headers={
#                 "X-Test-Client-IP": simulated_ip,
#             },
#             json={
#                 "username": "distributed_test_user",
#                 "password": "WrongPassword123!"
#             }
#         )








class LoginUser(HttpUser):
    host = "http://127.0.0.1"
    wait_time = between(0, 0)

    @task
    def login(self):
        port = random_module.choice([8000, 8001])

        # simulated_ip = "192.168.250.10"
        simulated_ip = f"192.168.250.{random_module.randint(1, 200)}"

        # self.client.post(
        #     f"http://127.0.0.1:{port}/api/login/",
        #     headers={"X-Test-Client-IP": simulated_ip},
        #     json={
        #         "username": "concurrent_test_user",
        #         "password": "WrongPassword123!"
        #     }
        # )
        with self.client.post(
            f"http://127.0.0.1:{port}/api/login/",
            headers={"X-Test-Client-IP": simulated_ip},
            json={
                "username": "concurrent_test_user",
                "password": "WrongPassword123!"
            },
            catch_response=True
        ) as response:

            if response.status_code == 401:
                response.success()
            else:
                response.failure(
                    f"Unexpected status code: {response.status_code}"
                )
            
    
    # @task
    # def concurrent_mfa_replay(self):
    #     port = random_module.choice([8000, 8001])

    #     self.client.post(
    #         f"http://127.0.0.1:{port}/api/mfa/complete-login/",
    #         json={
    #             "challenge_token": "eyJ1c2VyX2lkIjoxLCJwdXJwb3NlIjoibWZhX2xvZ2luIiwianRpIjoiODlhMDQzOTJmOTgzNGRmZmI0ZjljMzJkYTVmN2I1MmYifQ:1xRaWA:IwFZxVtPLC3ETmPjpbfx1ZFTD1YLI8D8joK1e8vtgzo",
    #             "code": "831801"
    #         },
    #         name="/api/mfa/complete-login/"
    #     )


    # def on_start(self):
    #     self.sent_mfa_request = False

    # @task
    # def concurrent_mfa_replay(self):
    #     if self.sent_mfa_request:
    #         return

    #     self.sent_mfa_request = True

    #     port = random_module.choice([8000, 8001])

    #     self.client.post(
    #         f"http://127.0.0.1:{port}/api/mfa/complete-login/",
    #         json={
    #             "challenge_token": "eyJ1c2VyX2lkIjoxLCJwdXJwb3NlIjoibWZhX2xvZ2luIiwianRpIjoiMDU0MDM4YTQ4YjYyNGRiMjliMDgzYWM5MmJiMTIwMTMifQ:1xRaku:_25rgeDWS1_JChu3p1piAg6dnAg37-hPvyfPVKjIArE",
    #             "code": "877149"
    #         },
    #         name="/api/mfa/complete-login/"
    #     )
