class Prompt(object):
  def __init__(self, prompt, action_map):
    self.action_map = action_map
    self.choices = list(action_map.keys())
    self.prompt = prompt + '\n'
    self.prompt = self.prompt + ('-' * 20) + '\n'
    for index, choice in enumerate(self.choices):
      self.prompt = self.prompt + f'{index + 1}: {choice}\n'
  
  def act(self):
    print(self.prompt)
    choice = self.safely_get_input() - 1
    if choice < 0 or choice >= len(self.choices):
      print(f'Choose a valid option between 1 - {len(self.choices) -1}\n')
      self.act()
    key = self.choices[choice]
    action = self.action_map[key]
    action()
  
  def safely_get_input(self):
    # Exception catch should be in its own function, as it is here.
    try:
      choice = int(input('>>> '))
    except:
      print('Please use a numeric value')
      self.safely_get_input()
    return choice
  
