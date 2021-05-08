'''
Adopted from namegenerator 1.0.6: https://pypi.org/project/namegenerator/
MIT license
2021 Yoginth <yoginth@zoho.com>
'''

import random

CENTER = [
    'amber', 'aqua', 'azure', 'beige', 'black', 'blue', 'brass', 'brown',
    'buff', 'coral', 'corn', 'cream', 'cyan', 'denim', 'ecru', 'flax', 'gold',
    'green', 'grey', 'ivory', 'jade', 'khaki', 'lemon', 'lilac', 'lime',
    'linen', 'mauve', 'ochre', 'olive', 'peach', 'pear', 'pink', 'plum', 'puce',
    'red', 'rose', 'ruby', 'rust', 'sepia', 'smalt', 'tan', 'taupe', 'teal',
    'wheat', 'white', 'zucchini'
]

LEFT = [
    'baggy', 'beady', 'boozy', 'bumpy', 'chewy', 'cozy', 'dorky', 'flaky',
    'foggy', 'fuzzy', 'gamy', 'geeky', 'gimpy', 'goopy', 'gummy', 'hasty',
    'hazy', 'hilly', 'homey', 'jumpy', 'lanky', 'leaky', 'lousy', 'lumpy',
    'messy', 'muggy', 'muzzy', 'nerdy', 'nippy', 'pasty', 'pokey', 'randy',
    'ready', 'scaly', 'seedy', 'shaky', 'silly', 'slimy', 'sunny', 'surly',
    'tacky', 'tasty', 'ugly', 'whiny', 'wiggy', 'wimpy', 'woozy', 'zippy'
]

RIGHT = [
    'akita', 'ant', 'barb', 'bat', 'bear', 'bee', 'bird', 'bison', 'blue',
    'boar', 'bongo', 'booby', 'camel', 'cat', 'chin', 'chow', 'civet', 'clam',
    'coati', 'coral', 'corgi', 'cow', 'crab', 'crane', 'dane', 'deer', 'devil',
    'dhole', 'dingo', 'dodo', 'dog', 'duck', 'eagle', 'eel', 'emu', 'fish',
    'fly', 'fossa', 'fowl', 'fox', 'frise', 'frog', 'gar', 'gecko', 'goat',
    'goose', 'guppy', 'hare', 'heron', 'horse', 'hound', 'husky', 'hyena',
    'hyrax', 'ibis', 'indri', 'kiwi', 'koala', 'kudu', 'lemur', 'liger', 'lion',
    'llama', 'loon', 'lynx', 'macaw', 'mau', 'mist', 'mole', 'molly', 'moose',
    'moth', 'mouse', 'mule', 'newt', 'okapi', 'olm', 'otter', 'owl', 'panda',
    'pig', 'quail', 'quoll', 'rat', 'ray', 'robin', 'saola', 'seal', 'shark',
    'sheep', 'shrew', 'skunk', 'sloth', 'slug', 'snail', 'snake', 'spitz',
    'squid', 'stoat', 'swan', 'tang', 'tapir', 'tetra', 'tiger', 'toad', 'tzu',
    'vole', 'wasp', 'whale', 'wolf', 'worm', 'yak', 'zebra', 'zebu', 'zorse'
]


def gen(repeatParts=False, separator='-', lists=(LEFT, CENTER, RIGHT)):
    name = []
    for word in lists:
        part = None
        while not part or (part in name and not repeatParts):
            part = random.choice(word)
        name.append(part)
    return separator.join(name)
