from kivy.uix.screenmanager import SlideTransition, NoTransition
import time
import requests
def request(screen_manager_object, error_screen_object, current_screen, 
                        next_screen, next_screen_object, address):
    time.sleep(2)
    try:
        response = requests.get(address, params = self.params)
        response = eval(response)
        if respose[0] == 0:
            screen_manager_object.transition = SlideTransition(direction = "left")
            screen_manager_object.current = current_screen
        else:
            print("Go to Next screen")
            next_screen_object.transition = SlideTransition(direction = "left")
            next_screen_object.current = next_screen_object
    except:
        print("Go to error screen")
        print("This object is : ", screen_manager_object)
        screen_manager_object.transition = SlideTransition(direction = "left")
        screen_manager_object.current = "error_screen"
        error_screen_object.previous_screen = current_screen