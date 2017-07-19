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
	
    def stop(self):
        pass
	
def create_skill():
    return PersonalitySkill1()
