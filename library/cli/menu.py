class Menu:

    def __init__(self, choices):
        self.choices = choices

    def make_choice(self, index):
        self.choices[index].action()

    def __str__(self):
        menu_list = []
        for index, choice in enumerate(self.choices):
            menu_list.append(f'{index + 1}: {choice}')
        return '\n'.join(menu_list)
