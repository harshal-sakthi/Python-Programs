from abc import ABC, abstractmethod

class FeaturePlan(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
    def check(self):
        pass
class WebApp(FeaturePlan):
    def login(self):
        print("Login to website")
    def logout(self):
        print("Logout from website")
w = WebApp()
w.login()
w.logout()