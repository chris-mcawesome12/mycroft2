from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'chrismcawesome'

LOGGER = getLogger(__name__)

class PersonalitySkill1(MycroftSkill):

    def __init__(self):
        super(PersonalitySkill1, self).__init__(name="PersonalitySkill1")
		
	def initialize(self):
        matt_or_dave_intent = IntentBuilder("MattOrDaveIntent").\
            require("MattOrDaveKeyword").build()
        self.register_intent(matt_or_dave_intent, self.handle_matt_or_dave_intent)

        freddy_or_jason_intent = IntentBuilder("FreddyOrJasonIntent").\
            require("FreddyOrJasonKeyword").build()
        self.register_intent(freddy_or_jason_intent, self.handle_freddy_or_jason_intent)
		
		bay_doors_intent = IntentBuilder("BayDoorsIntent").\
            require("BayDoorsKeyword").build()
        self.register_intent(bay_doors_intent, self.handle_bay_doors_intent)
		
		meaning_of_life_intent = IntentBuilder("MeaningOfLifeIntent").\
            require("MeaningOfLifeKeyword").build()
        self.register_intent(meaning_of_life_intent, self.handle_meaning_of_life_intent)
		
		shaymus_intent = IntentBuilder("ShaymusIntent").\
            require("ShaymusKeyword").build()
        self.register_intent(shaymus_intent, self.handle_shaymus_intent)
		
		kate_intent = IntentBuilder("KateIntent").\
            require("KateKeyword").build()
        self.register_intent(kate_intent, self.handle_kate_intent)

        good_morning_intent = IntentBuilder("GoodMorningIntent").\
            require("GoodMorningKeyword").build()
        self.register_intent(good_morning_intent,
                             self.handle_good_morning_intent)

        good_afternoon_intent = IntentBuilder("GoodAfternoonIntent").\
            require("GoodAfternoonKeyword").build()
        self.register_intent(good_afternoon_intent,
                             self.handle_good_afternoon_intent)

        good_evening_intent = IntentBuilder("GoodEveningIntent").\
            require("GoodEveningKeyword").build()
        self.register_intent(good_evening_intent,
                             self.handle_good_evening_intent)

        good_night_intent = IntentBuilder("GoodNightIntent").\
            require("GoodNightKeyword").build()
        self.register_intent(good_night_intent,
                             self.handle_good_night_intent)

		who_you_intent = IntentBuilder("WhoYouIntent").\
            require("WhoYouKeyword").build()
        self.register_intent(who_you_intent, self.handle_who_you_intent)

		who_i_intent = IntentBuilder("WhoIIntent").\
            require("WhoIKeyword").build()
        self.register_intent(who_i_intent, self.handle_who_i_intent)
		
	def handle_matt_or_dave_intent(self, message):
        self.speak_dialog("matt.dave")

    def handle_freddy_or_jason_intent(self, message):
        self.speak_dialog("freddy.jason")
		
	def handle_bay_doors_intent(self, message):
        self.speak_dialog("bay.doors")

	def handle_meaning_of_life_intent(self, message):
        self.speak_dialog("meaning.life")
		
	def handle_shaymus_intent(self, message):
        self.speak_dialog("shaymus")
		
	def handle_kate_intent(self, message):
        self.speak_dialog("kate")
		
    def handle_good_morning_intent(self, message):
        self.speak_dialog("good.morning")

    def handle_good_afternoon_intent(self, message):
        self.speak_dialog("good.afternoon")

    def handle_good_evening_intent(self, message):
        self.speak_dialog("good.evening")

    def handle_good_night_intent(self, message):
        self.speak_dialog("good.night")

    def handle_who_you_intent(self, message):
        self.speak_dialog("who.you")
		
    def handle_who_i_intent(self, message):
        self.speak_dialog("who.i")
		
	def stop(self):
        pass
	
def create_skill():
    return PersonalitySkill1()
