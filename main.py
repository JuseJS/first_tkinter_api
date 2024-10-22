from controllers.api_controller import APIController
from controllers.main_app import MainApp

if __name__ == "__main__":
    api_response = APIController.fetch_api_data()
    if api_response:
        main_app = MainApp("Primera API Tkinter", "1000x600", api_response)
