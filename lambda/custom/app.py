import json
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model.ui import simple_card, SimpleCard

# Skill builder object

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# request handlers launch bstython with bstpy lambda.py.lambda_function.handler
# pip install -e /home/ric/Python-Projects/ALEXA_SDK/bst_python/bstpy

def _load_apl_document(file_path):
    # type: (str) -> Dict[str, Any]
    """Load the apl json document at the path into a dict object."""
    with open(file_path) as f:
        return json.load(f)


@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    speechText = 'Welcome to the the Food Pyramid skill. You can ask about ' \
                 'the different tiers or a specific food group!'
    return(
        handler_input.response_builder.speak(speechText)
        .ask(speechText)
        .set_card(SimpleCard("Food Pyramid", speechText))
        .add_directive(
            RenderDocumentDirective(document=_load_apl_document("lambda/custom/homepage.json")
         )
    ).set_should_end_session(False)
        .response
    )


@sb.request_handler(can_handle_func=is_intent_name('GrainsIntent'))
def grains_intent_handler(handler_input):
    speechText = 'These foods provide complex carbohydrates, which are a ' \
                 'good source of energy but provide little nutrition.'
    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Grains - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/grains.json")
                )
        )
            .response
    )


@sb.request_handler(can_handle_func=is_intent_name('VegetablesIntent'))
def vegetables_intent_handler(handler_input):
    speechText = 'A vegetable is a part of a plant consumed by humans that is generally savory but is not sweet. A vegetable is not considered a grain, fruit, nut, spice, or herb.'

    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Vegetables - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/vegetables.json")
                )
        )
            .response
    )



@sb.request_handler(can_handle_func=is_intent_name('FruitsIntent'))
def fruits_intent_handler(handler_input):
    speechText = 'Fruits are the sweet-tasting seed-bearing parts of plants, or occasionally sweet parts of plants which do not bear seeds.'

    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Fruits - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/fruits.json")
                )
        )
            .response
    )


@sb.request_handler(can_handle_func=is_intent_name('DairyIntent'))
def dairy_intent_handler(handler_input):
    speechText = 'Dairy products are produced from the milk of mammals. They include milk, yogurt and cheese.'

    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Dairy - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/dairy.json")
            )
        )
            .response
    )



@sb.request_handler(can_handle_func=is_intent_name('MeatsIntent'))
def meats_intent_handler(handler_input):
    speechText = 'Meat is the tissue – usually muscle – of an animal consumed by humans. Since most parts of many animals are edible, there is a vast variety of meats.'

    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Meats - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/meats.json")
            )
        )
            .response
    )



@sb.request_handler(can_handle_func=is_intent_name('FatsIntent'))
def fats_intent_handler(handler_input):
    speechText = 'These foods provide calories, but not much nutrition. These foods include salad dressings, sugars, soft drinks, candies, and desserts.'

    return (
        handler_input.response_builder.speak(speechText)
            .ask(speechText)
            .set_card(SimpleCard("Fats - Food Pyramid", speechText))
            .add_directive(
            RenderDocumentDirective(
                document=_load_apl_document("lambda/custom/fats.json")
            )
        )
            .response
    )


handler = sb.lambda_handler()