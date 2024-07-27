# Package clrppy
# More Simple Printing With Color

import random
import time
import os

__version__ = '0.0.1'
__all__ = ['Fore', 'Back', 'NORMAL', 'LIGHT', 'LOWBRIGHT', 
           'UNDERLINE', 'FLICKER', 'INVERSE', 'BLANKING',
           'colorprint', 'showerror', 'showwarning', 'showinfo', 
           'rprint', 'rrprint']

_initialized = False

def _initcprint():
    """Initzlize."""
    global _initialized
    if not _initialized:
        _initialized = True
        os.system('')

def _make_prefix(fore, back, effect):
    prefix = '\033['
    if not (fore in styles or back in styles or effect in styles):
        raise ValueError('The values passed in are incorrect')
    
    prefix += ';'.join((effect, fore, back)) + 'm'
    return prefix

class Fore:
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    PURPLE = '35'
    CYAN = '36'
    WHITE = '37'
class Back:
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    PURPLE = '45'
    CYAN = '46'
    WHITE = '47'
NORMAL = '0'
LIGHT = '1'
LOWBRIGHT = '2'
UNDERLINE = '4'
FLICKER = '5'
INVERSE = '7'
BLANKING = '8'

styles = ['0', '1', '2', '4', '5', '7', '8'] + [str(i) for i in range(30, 38)] + [str(i) for i in range(40, 48)]

def colorprint(value, end: str='\n', fore: str=Fore.WHITE, 
           back: str=Back.BLACK, effect: str=NORMAL,
           reset: bool=True, flush: bool=False):
    """Print With Color.
    Usage::
    
     colorprint('ERROR!', fore=Fore.RED) # Red Foreground
     colorprint('GOT INFO', fore=Fore.Cyan, effect=FLICKER) # Cyan with a flicker effect

    Parameter `value` can be anything. If it isn't a string, it will be executed eval().\n
    Parameter `reset` indicates whether the style is reset after printing.
    """

    _initcprint()
    prefix = _make_prefix(fore, back, effect)
    ext = '\033[0m' if reset else ''
    if not isinstance(value, str):
        print(prefix+str(eval(value)), end=(ext+end), flush=flush)
    else:
        print(prefix+value, end=(ext+end), flush=flush)

def showerror(msg: str):
    """Show An Error."""
    colorprint(msg, fore=Fore.RED)

def showinfo(msg: str):
    """Show Information."""
    colorprint(msg, fore=Fore.CYAN)

def showwarning(msg: str):
    """Show Warning."""
    colorprint(msg, fore=Fore.YELLOW)

def clearscreen():
    os.system('cls')

###### NOTE: The following two functions are for entertainment only.

def rprint(msg: str, delay: float):
    """Output like a rainbow.(Typewriter)\n
    Parameter `delay` means the delay time for each character to be output.\n
    """

    fores = [str(fore) for fore in range(31, 38)]

    for idx, letter in enumerate(msg):
        colorprint(letter, end='', fore=fores[idx%7], flush=True)
        time.sleep(delay)
    print()

def rrprint(msg: str, delay: float):
    """Output with random color.(Typewriter)\n
    Parameter `delay` means the delay time for each character to be output.\n
    """

    fores = [str(fore) for fore in range(31, 38)]

    for letter in msg:
        colorprint(letter, end='', fore=random.choice(fores), flush=True)
        time.sleep(delay)
    print()