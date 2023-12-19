from experta import *

class Answer(Fact):
    answer_1 = Field(str, default="")
    answer_2 = Field(str, default="")
    answer_3 = Field(str, default="")

# answers_physical_impairment = [Answer('Yes', 'Hard of Hearing'), Answer('Yes', 'Vision Impaired'),
# Answer('Yes, Problem with Memory')]
class HRA(KnowledgeEngine):
    @Rule(Answer('Yes', 'Hard of Hearing') | Answer('Yes', 'Vision Impaired') | Answer('Yes', 'Problem with Memory'))
    def physical_impairment_barrier(self):
       if (Answer('Yes', 'Hard of Hearing')):
            self.declare(Answer("Yes", "B - Hearing Disorder"))
            self.declare(Answer('B - Hearing Disorder'))
       elif (Answer('Yes', 'Vision Impaired')):
            print('hi')
            self.declare(Answer("Yes", "B - Vision Disorder"))
            self.declare(Answer('B - Vision Disorder'))


    @Rule(Answer('Yes', 'B - Hearing Disorder') | Answer('Yes', 'B - Vision Disorder') | Answer('Yes', 'B - Problem with Memory'))
    def physical_impairment_intervention(self): 
        if (Answer('Yes', 'B - Hearing Disorder')):
            print("Voice line should be TTY-supported")
        elif (Answer('Yes', 'B - Vision Disorder')):
            print("Send an alert to CM to confirm support from family or caregiver")


    @Rule(Answer('B - Hearing Disorder'))
    def physical_impairment_action(self):
        print('Patient will use equipment approved by health plan')




engine = HRA()
engine.reset()
engine.declare(Answer('Yes', 'Vision Impaired'))
engine.run()