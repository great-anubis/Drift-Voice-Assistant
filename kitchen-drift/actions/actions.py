from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import cohere
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

class ActionGetRecipe(Action):
    def name(self) -> str:
        return "action_get_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        user_input = tracker.latest_message.get('text')
        try:
            response = co.generate(
                model='command',
                prompt=(
                    "You are Drift, a highly knowledgeable kitchen assistant. "
                    "Your primary focus is to help with kitchen tasks, cooking advice, and recipes. "
                    "Please provide clear, concise, and practical advice related to the kitchen. "
                    f"Question: {user_input}"
                ),
                max_tokens=250,
                temperature=0.7
            )
            message = response.generations[0].text.strip()
            dispatcher.utter_message(text=message)
            return []
        except Exception as e:
            dispatcher.utter_message(text="I'm sorry, something went wrong while fetching the recipe.")
            return []

class ActionSetTimer(Action):
    def name(self) -> str:
        return "action_set_timer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        time = tracker.get_slot('time')
        dispatcher.utter_message(text=f"Timer set for {time} minutes.")
        # Additional logic to actually set a timer could go here
        return []

class ActionConvertUnits(Action):
    def name(self) -> str:
        return "action_convert_units"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        user_input = tracker.latest_message.get('text')
        try:
            response = co.generate(
                model='command',
                prompt=(
                    "You are Drift, a highly knowledgeable kitchen assistant. "
                    "Your primary focus is to help with kitchen tasks, cooking advice, and recipes. "
                    "Please provide clear, concise, and practical advice related to the kitchen. "
                    f"Convert the following: {user_input}"
                ),
                max_tokens=50,
                temperature=0.5
            )
            conversion = response.generations[0].text.strip()
            dispatcher.utter_message(text=f"The conversion is: {conversion}")
            return []
        except Exception as e:
            dispatcher.utter_message(text="I'm sorry, something went wrong while converting the units.")
            return []

class ActionGetSubstitute(Action):
    def name(self) -> str:
        return "action_get_substitute"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        ingredient = tracker.get_slot('ingredient')
        try:
            response = co.generate(
                model='command',
                prompt=(
                    "You are Drift, a highly knowledgeable kitchen assistant. "
                    "Your primary focus is to help with kitchen tasks, cooking advice, and recipes. "
                    f"Provide a substitute for {ingredient}."
                ),
                max_tokens=50,
                temperature=0.7
            )
            substitute = response.generations[0].text.strip()
            dispatcher.utter_message(text=f"A good substitute for {ingredient} is: {substitute}")
            return [SlotSet("ingredient", None)]
        except Exception as e:
            dispatcher.utter_message(text="I'm sorry, something went wrong while fetching the substitute.")
            return []

class ActionGetStorageTips(Action):
    def name(self) -> str:
        return "action_get_storage_tips"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        user_input = tracker.latest_message.get('text')
        try:
            response = co.generate(
                model='command',
                prompt=(
                    "You are Drift, a highly knowledgeable kitchen assistant. "
                    "Your primary focus is to help with kitchen tasks, cooking advice, and recipes. "
                    f"Give storage tips for: {user_input}"
                ),
                max_tokens=100,
                temperature=0.7
            )
            storage_tips = response.generations[0].text.strip()
            dispatcher.utter_message(text=f"Here are some storage tips: {storage_tips}")
            return []
        except Exception as e:
            dispatcher.utter_message(text="I'm sorry, something went wrong while fetching the storage tips.")
            return []
