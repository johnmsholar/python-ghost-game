from dictionary_trie import Dictionary_Trie
from ghost_player import GhostBot, Human
from time import time, sleep
from ghost_exceptions import CallBluffException, HelpException, EndRoundException, OpponentCompletedWordException

class Match():
    opponents = ['1. Timmy (Vocabulary: 1000 Most Common English Words)',
                '2. Larry (Vocabulary: 10000 Most Common English Words as curated by Google)',
                '3. Sergey (Vocabulary: 20000 Most Common English Words as curated by Google)',
                '4. HAL (Vocabulary: UNIX Dictionary - 127142 Words of Pure Pain)']
    dictionaries = ['oneThousandMostCommonWords.txt',
                'tenThousandMostCommonWords.txt',
                'twentyThousandMostCommonWords.txt',
                'dictionary.txt']
    rules_text = 'Here\'s how it works:\n' + \
                        'In a game of GHOST, two players alternate saying letters, which are concatenated as play continues.\n' + \
                        'If a player completes a word, that player loses the game.\n' + \
                        'When it is your turn, you have three options:\n' + \
                        '\t1: Play a letter to be concatenated to the end of the current string.\n' + \
                        '\t\t(Do this in gameplay by entering a single letter.)\n' + \
                        '\t2: Call the bluff of the other player. If you think the other player is not moving towards a word,\n' + \
                        '\tyou may assert this. (Do this in gameplay by typing \'call bluff\').\n' + \
                        '\t\tCalling Bluff (Taking Your Opponent to the Book, \"Invoking Webster\", etc...):\n' + \
                        '\t\t\tIf you call the bluff of the other player, and they can provide a word in the dictionary\n' + \
                        '\t\t\t which starts with the current prefix, you lose. If they cannot, they lose!\n' + \
                        '\t3: You may ask for help at any time by typing \'help\'\n'

    def __init__(self):
        self.introduce()
        self.definitive_dictionary = Dictionary_Trie('dictionary.txt')
        self.create_player_character()
        self.create_ghost_bot()
        self.rounds_played = 0
        while self.human.letter_count < len(self.human.end_word) and self.ghost_bot.letter_count < len(self.ghost_bot.end_word):
            human_goes_first = (self.rounds_played % 2 == 0)
            self.active_round = Round(self.definitive_dictionary, self.human, self.ghost_bot, human_goes_first)
            self.active_round.play_to_completion()
            self.rounds_played += 1

    def introduce(self):
        print 'Let\'s play GHOST!'
        if raw_input('Would you like to know how? (y/n) ').lower().startswith('y'):
            print Match.rules_text
        else:
            print 'Already a pro, huh? Let\'s play!'

    def create_player_character(self):
        name = raw_input('But first... what\'s your name?\n')
        self.human = Human(name)
        print 'Hello there, ' + self.human.name + '! It\'s a pleasure to make your acquaintance.'

    def create_ghost_bot(self):
        self.ghost_bot = GhostBot(self.dictionaries[self.select_opponent()], 'BOT')

    def select_opponent(self):
        opponent_selection = ''
        while not self._verify_opponent_selection(opponent_selection, Match.opponents):
            opponent_selection = raw_input('Choose an opponent!\n' + reduce(lambda x, y: x+y, [('\t' + opponent + '\n') for opponent in Match.opponents]))
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
        while True:
            try:
                self.play_single_move()
            except EndRoundException:
                break
        self.conclude()

    # Should player be able to call other player out after every word? e.g. 'That's not a word!'
    # Probably going to go with the exception implementation.
    def play_single_move(self):
        try:
            self.word += self.active_player.play_letter(self.word)
        except CallBluffException:
            self.handle_bluff_call()
            raise EndRoundException
        except HelpException:
            self.active_player.help()
            self.word += self.active_player.play_letter(self.word)
        except OpponentCompletedWordException:
            self.handle_completed_word_assertion()
            raise EndRoundException
        # Evaluate if game is over???
        self.active_player, self.inactive_player = self.inactive_player, self.active_player # Swap active and inactive players

    def handle_bluff_call(self):
        success = self.active_player.call_bluff(self.inactive_player, self.word, self.definitive_dictionary)
        if success:
            self.active_player.win()
            self.inactive_player.lose()
        else:
            self.active_player.lose()
            self.inactive_player.win()

    def handle_completed_word_assertion(self):
        completed_word = self.definitive_dictionary.contains(self.word)
        if completed_word:
            self.active_player.win()
            self.inactive_player.lose()
        else:
            self.active_player.lose()
            self.inactive_player.win()

    def conclude(self):
        print 'This concludes the round.'
        print 'Game status:'
        print '\t' + self.player_1.name + ': ' + self.player_1.get_letters()
        print '\t' + self.player_2.name + ': ' + self.player_2.get_letters()

if __name__ == '__main__':
    Match()