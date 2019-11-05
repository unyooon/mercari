import sys
#import src.mercari
from src.mercari import Mercari

args = sys.argv
word = args[1]
eng_word = args[2]
rumba = Mercari(word)
rumba.get_informations()

Mercari(args[1], args[2]).get_informations()
