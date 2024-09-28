# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    # The generated goal option will not keep your defined values or documentation string you'll need to add them here:
    # To automatically convert your own goal to alias of the generated goal uncomment the lines below and replace 'Goal' with your own option of type Choice

    # your_goal_class = Goal #Your Goal class here
    # generated_goal = options.get('goal', {})
    # if generated_goal and issubclass(your_goal_class, Choice) and not issubclass(generated_goal, your_goal_class):
    #     goals = {'option_' + i: v for i, v in generated_goal.options.items() if i != 'default'}
    #     for option, value in your_goal_class.options.items():
    #         if option == 'default':
    #             continue
    #         goals[f"alias_{option}"] = value
    #     options['goal'] = type('goal', (Choice,), goals)
    #     options['goal'].default = your_goal_class.options.get('default', generated_goal.default)
    #     options['goal'].__doc__ = your_goal_class.__doc__ or options['goal'].__doc__
    return options

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Option]]) -> dict[str, list[Option]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
