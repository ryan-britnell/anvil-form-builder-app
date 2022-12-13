from ._anvil_designer import TextBoxTemplate
from anvil import *

from ... import Globals

class TextBox(TextBoxTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.question_number_label.text = Globals.NUMBER_OF_QUESTIONS + 1
    self.item['question_number'] = Globals.NUMBER_OF_QUESTIONS + 1
