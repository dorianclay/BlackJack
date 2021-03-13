import sys


class Prompt:

    def __init__(self, prompt, menu):
        self.prompt = prompt
        self.menu = menu

    def get_choice_index_from_menu(self):
        choice_index = self.get_input_from_menu()
        if self.is_choice_out_of_bounds(choice_index):
            print(
                f'Choose a valid option between 1 - {len(self.choice_index) -1}\n'
            )
            return self.get_choice_index_from_menu()
        return choice_index

    def get_input_from_menu(self):
        self.display_prompt()
        user_input = input('>>> ')
        self.check_for_exit_command(user_input)
        return self.safely_get_input_from_menu(user_input)

    def safely_get_input_from_menu(self, user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print('Please use a numeric value')
            self.get_input_from_menu()
        return user_input - 1

    def is_choice_out_of_bounds(self, choice):
        return choice < 0 or choice >= len(self.menu.choices)

    def display_prompt(self):
        print(self.prompt)
        print('-' * 20)
        print(self.menu)

    def check_for_exit_command(self, user_input):
        if user_input.lower() == 'q':
            sys.exit(0)
