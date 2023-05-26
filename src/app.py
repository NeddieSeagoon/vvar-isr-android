from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
from colorama import Fore


class Observation:
    def __init__(self):
        self.type = None
        self.status = None
        self.size = None
        self.location = None


class ObservationApp(App):

    # build gets called automatically on App.run()
    def build(self):
        self.page_index = 1
        self.main_layout = BoxLayout(orientation='vertical')

        self.type_button = Button(text='Report', on_release=self.show_type_page)
        self.main_layout.add_widget(self.type_button)

        return self.main_layout

    def show_type_page(self, instance):
        self.main_layout.clear_widgets()
    
        self.observation = Observation()

        self.type_label = Label(text='Type')
        self.main_layout.add_widget(self.type_label)

        self.ship_button = Button(text='Ship', on_release=self.show_status_page)
        self.main_layout.add_widget(self.ship_button)
        self.observation.type = 'Ship'


    def show_status_page(self, instance):
        self.main_layout.clear_widgets()

        self.status_label = Label(text='Status')
        self.main_layout.add_widget(self.status_label)

        self.hostile_button = Button(text='Hostile', on_release=lambda btn: self.select_status('Hostile'))
        self.main_layout.add_widget(self.hostile_button)

        self.friendly_button = Button(text='Friendly', on_release=lambda btn: self.select_status('Friendly'))
        self.main_layout.add_widget(self.friendly_button)

        self.neutral_button = Button(text='Neutral', on_release=lambda btn: self.select_status('Neutral'))
        self.main_layout.add_widget(self.neutral_button)

        self.unknown_button = Button(text='Unknown', on_release=lambda btn: self.select_status('Unknown'))
        self.main_layout.add_widget(self.unknown_button)

    def select_status(self, choice):
        self.observation.status = choice
        self.show_size_page()

    def show_size_page(self):
        self.main_layout.clear_widgets()

        self.size_label = Label(text='Size')
        self.main_layout.add_widget(self.size_label)

        self.small_button = Button(text='Small', on_release=lambda btn: self.select_size('Small'))
        self.main_layout.add_widget(self.small_button)

        self.medium_button = Button(text='Medium', on_release=lambda btn: self.select_size('Medium'))
        self.main_layout.add_widget(self.medium_button)

        self.large_button = Button(text='Large', on_release=lambda btn: self.select_size('Large'))
        self.main_layout.add_widget(self.large_button)

    def select_size(self, choice):
        self.observation.size = choice
        self.show_location_page()

    def show_location_page(self):
        self.main_layout.clear_widgets()

        self.location_label = Label(text='Location')
        self.main_layout.add_widget(self.location_label)

        self.tressler_button = Button(text='Tressler', on_release=lambda btn: self.select_location('Tressler'))
        self.main_layout.add_widget(self.tressler_button)

        self.om1_button = Button(text='OM-1', on_release=lambda btn: self.select_location('OM-1'))
        self.main_layout.add_widget(self.om1_button)

        self.om2_button = Button(text='OM-2', on_release=lambda btn: self.select_location('OM-2'))
        self.main_layout.add_widget(self.om2_button)

        self.om3_button = Button(text='OM-3', on_release=lambda btn: self.select_location('OM-3'))
        self.main_layout.add_widget(self.om3_button)

        self.om4_button = Button(text='OM-4', on_release=lambda btn: self.select_location('OM-4'))
        self.main_layout.add_widget(self.om4_button)

        self.om5_button = Button(text='OM-5', on_release=lambda btn: self.select_location('OM-5'))
        self.main_layout.add_widget(self.om5_button)

        self.om6_button = Button(text='OM-6', on_release=lambda btn: self.select_location('OM-6'))
        self.main_layout.add_widget(self.om6_button)

    def select_location(self, choice):
        self.observation.location = choice
        self.send_observation(debug=True)  # Print observation to console



    def send_observation(self, debug=False):
        if debug:
            status_color = ''
            if self.observation.status == 'Hostile':
                status_color = Fore.RED
            elif self.observation.status == 'Friendly':
                status_color = Fore.BLUE
            elif self.observation.status == 'Unknown':
                status_color = Fore.YELLOW
            elif self.observation.status == 'Neutral':
                status_color = Fore.GREEN

            observation_str = f"{status_color}New Observation:\n{self.observation.status} - {self.observation.type} - {self.observation.size} - {self.observation.location}"
            print(observation_str)
        else:
            # Replace 'http://yourserver.com/observations' with your server's URL
            request = UrlRequest('http://yourserver.com/observations',
                                on_success=self.on_request_success,
                                on_failure=self.on_request_failure,
                                req_body={'id': observation_id,
                                        'ship': self.observation.type,
                                        'status': self.observation.status,
                                        'size': self.observation.size,
                                        'location': self.observation.location})



    def on_request_success(self, req, result):
        print('Observation sent successfully.')

    def on_request_failure(self, req, result):
        print('Failed to send observation.')


if __name__ == '__main__':
    ObservationApp().run()
