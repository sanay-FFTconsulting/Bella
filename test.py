from colorama import Fore, Style, Back
from colorama import Fore, Style

def color_specific_characters(text, indices, color):
  """Colors specific characters in a string.

  Args:
    text: The string to color.
    indices: A list of indices (0-based) of characters to color.
    color: The color code from colorama.Fore (e.g., Fore.RED).

  Returns:
    The string with specified characters colored.
  """
  colored_text = ""
  for i, char in enumerate(text):
    if i in indices:
      colored_text += color + char + Style.RESET_ALL
    else:
      colored_text += char
  return colored_text

# Example usage:
my_string = "night"
indices_to_color = [0]
colored_string = color_specific_characters(my_string, indices_to_color, Fore.RED)
print(colored_string)
# Print text in different colors
print(Fore.RED + "This text is red" + Style.RESET_ALL)
print(Fore.GREEN + "This text is green" + Style.RESET_ALL)
print(Fore.BLUE + "This text is blue" + Style.RESET_ALL)
print(Fore.YELLOW + "This text is yellow" + Style.RESET_ALL)
print(Fore.MAGENTA + "This text is magenta" + Style.RESET_ALL)
print(Fore.CYAN + "This text is cyan" + Style.RESET_ALL)
print(Fore.WHITE + "This text is white" + Style.RESET_ALL)

# Use Style.BRIGHT for brighter colors
print(Fore.RED + Style.BRIGHT + "This text is bright red" + Style.RESET_ALL)

# Combine Fore and Back (background color)
print(Fore.BLACK + Back.YELLOW + "Black text on yellow background" + Style.RESET_ALL)

