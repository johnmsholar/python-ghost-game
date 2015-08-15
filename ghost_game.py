from dictionary_trie import Dictionary_Trie
from ghost_player import GhostBot, Human
from time import time, sleep

class Match():
    opponents = ['1. Timmy (Vocabulary: 1000 Most Common English Words)',
                '2. Larry (Vocabulary: 10000 Most Common English Words as curated by Google)',
                '3. Sergey (Vocabulary: 20000 Most Common English Words as curated by Google)',
                '4. HAL (Vocabulary: UNIX Dictionary - 127142 Words of Pure Pain)']
    dictionaries = ['oneThousandMostCommonWords.txt',
                'tenThousandMostCommonWords.txt',
                'twentyThousandMostCommonWords.txt',
                'dictionary.txt']
    # TODO: should probably add a rules description here

    def __init__(self):
        self.introduce()
        self.definitive_dictionary = Dictionary_Trie('dictionary.txt')
        self.create_player_character()
        self.create_ghost_bot()
        self.rounds_played = 0
        while self.human.letter_count < len(self.human.end_word) and self.ghost_bot.letter_count < len(self.ghost_bot.end_word):
            human_goes_first = (rounds_played % 2 == 0)
            self.active_round = Round(self.definitive_dictionary, self.human, self.ghost_bot, human_goes_first)
            self.active_round.play_to_completion() # or something to that effect

    def introduce(self):
        print 'Let\'s play GHOST!'

    def create_player_character(self):
        name = raw_input('But first... what\'s your name?\n')
        self.human = Human(name)
        print 'Hello there, ' + human.name + '! It\'s a pleasure to make your acquaintance.'

    def create_ghost_bot(self):
        self.ghost_bot = GhostBot(self.dictionaries[self.select_opponent()])

    def select_opponent(self):
        opponent_selection = ''
        while not self._verify_opponent_selection(opponent_selection, opponents):
            opponent_selection = raw_input('Choose an opponent!\n' + reduce(lambda x, y: x+y, [('\t' + opponent + '\n') for opponent in opponents]))
        return int(opponent_selection) - 1

    def _verify_opponent_selection(self, opponent_selection, opponents):
        if opponent_selection == '':
            return False
        try:
            num_selection = int(opponent_selection) - 1
            if num_selection not in range(len(opponents)):
                print 'That\'s not a valid number.'
                return False
            else:
                return True
        except ValueError as error:
            print 'I don\'t understand that input.'
            return False

# TODO: Extend the round class to support two arbitrary players, rather than a human and a ghost_bot
# I don't think I'll extend to support more than 2 players. It seems to spit in the face of the game.
class Round():
    def __init__(self, definitive_dictionary, player_1, player_2, player_1_goes_first):
        self.word = ''
        self.definitive_dictionary = definitive_dictionary
        self.player_1 = player_1
        self.player_2 = player_2
        if player_1_goes_first:
            self.active_player = self.player_1
            self.inactive_player = self.player_2
        else:
            self.active_player = self.player_2
            self.inactive_player = self.player_1

    def play_to_completion(self):
        self.begin()

    # Should player be able to call other player out after every word? e.g. 'That's not a word!'
    # Probably going to go with the exception implementation.
    def play_single_move(self):
        """
        action = self.active_player.choose_action(word)
        if action.__name__ == 'call_bluff':
            self.handle_bluff_call()
        elif action.__name__ == 'help':
            self.active_player.help()
        """
        try:
            self.word += self.active_player.move(self.word)
        except CallBluffException:
            self.active_player.call_bluff(self.inactive_player, self.word)
        except HelpException:
            self.active_player.help()
            self.word += self.active_player.move(self.word)
        # Evaluate if game is over???
        self.active_player, self.inactive_player = self.inactive_player, self.active_player # Swap active and inactive players

    def handle_bluff_call(self):


    def player_move(self):
        move = ''
        while not verify_human_letter(move):
            move = raw_input('It\'s your move! What letter will you play? ')
        self.word += move.lower()
        if self.definitive_dictionary.contains(self.word)
            lose()
            return True
        return False

    def ghostBot_move():
        move = ghostBot.play(self.word)
        if move == None:
            print 'I don\'t think you\'re moving towards an English word!'
            print 'But if you can tell me a word that starts with ' + self.word + ' then you win!'
            target = raw_input('What word were you thinking of? ')
            if self.definitive_dictionary.contains(target) and target.lower().startswith(self.word):
                print 'Wow! You got me! You win!'
            else:
                print 'That word isn\'t in the definitive dictionary. You lose!'
            # Handle here
            win()
        print 'I play...', move
        word += move.lower()
        if self.definitive_dictionary.contains(self.word)
            return True
        return False

def play(is_player_turn):
    while True:
        if is_player_turn:
            if player_move():
                break
        else:
            if ghostBot_move():
                break
        is_player_turn = not is_player_turn
        print 'The current word is:', word

def lose():
    global word
    print 'You have completed a word! You lose!'
    word = ''

def win():
    global word
    print 'Your opponent has completed a word! You win!'
    word = ''

def end():
    print 'Thank you for playing!'

if __name__ == '__main__':
    introduction()
    select_opponent()
    begin_game()
    end()