# Any functions included in this file are small but important features condensed into these reusable library functions

import random

def gatherNumberInput(prompt="Please enter a number (FALLBACK): "):
    # AUTHOR: Jacob Duty
    # This function accepts 1 argument, prompt (falling back to a generic string if none is provided)
    # It will ask the user the inputted prompt, then verify the input is a number
    # When the input is verified succesfully it will return that value
    # ---- EXAMPLE:
    # value = gatherNumberInput("Example prompt: ")

    value = "a"
    # Use a while loop and proposal variable to validate the input
    while value.isalpha():
        proposal = input(prompt)
        # If the number is numeric ONLY then we can set the value to the proposed value
        if str(proposal).isnumeric():
            value = proposal
        else:
            # Explanation for whats going wrong
            print("Please input ONLY a POSITIVE number.\n")

    return int(value)

def gatherStringInput(prompt="Please enter a value (FALLBACK):"):
    # AUTHOR: Jacob Duty
    # This function accepts 1 argument, prompt (falling back to a generic string if none is provided)
    # It will ask the user the inputted prompt, then gather that input and return it
    # ---- EXAMPLE:
    # value = gatherStringInput("Example prompt: ")

    # Significantly simpler than the previous number function
    value = input(prompt)
    # No validation required, just return the value
    return str(value)