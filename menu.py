# Designed by Mike Susut, (ZippidyZap, MikeSusutZZ)
import math

class Menu():
    """
    A class that represents a Menu with various menu items.

    Attributes:
    ----------
    _items : list
        A list containing menu items.
    _open : str
        The opening message for the menu.
    _close : str
        The closing message or prompt for the menu.
    _type : str
        The type of menu - either 'let' or 'num'.
    """
    
    def __init__(self, open, close = "Which do you choose: ", inputType = "num", breakAfterEx = True):
        """
        Initializes a new Menu instance.

        Parameters:
        ----------
        open : str
            The opening message for the menu.
        close : str, optional
            The prompt for the input.
        items : list, optional
            The list of items in the menu if you already have MenuItems initialized
        inputType : str, optional
            The type of menu input - either 'let' for letters or 'num' for numbers.
            ex. A) B) C) or 1) 2) 3)
        breakAfterEx : boolean, optional

        When X is given, it will always exit the menu
        """
        self._items = []
        self._open = open
        self._close = close
        if inputType != 'let' and inputType != 'num':
            raise ValueError("Invalid inputType")
        self._type = inputType
        self.breakAfterEx = breakAfterEx

    def addItem(self, statement, action):
        """
        Adds an item to the menu.

        Parameters:
        ----------
        statement : str
            The statement or description of the menu item.
        action : callable
            The action to perform when this menu item is selected.
        """
        self._items.append(MenuItem(statement, action))

    def addOptionalItems(self, statementList, actionList, keys):
        """
        Adds a group of items to the menu, designed for situations where depending on circumstances
        one or more

        Parameters:
        ----------
        statementList : list
            List of statements or descriptions for the menu items.
        actionList : list
            List of actions to perform for the respective menu items.
        keys : list
            List of keys corresponding to each menu item.
        """
        itemList = []
        for i in range(len(statementList)):
            itemList.append(MenuItem(statementList[i], actionList[i]))
        self._items.append(OptionalMenuItems(itemList, keys))

    def addOptionalRepeatedItems(self, objectList, action, showWhenFun, getNameFun):
        """
    Adds a group of items to the menu from a provided list of objects.

    This method is designed for situations where there's a variable-sized list 
    of objects that all share the same method, but the visibility of each item 
    in the menu depends on a specific boolean condition determined by the 
    showWhenFun function.

    Parameters:
    ----------
    - objectList (list): A list of objects to be added to the menu.
    - action (function): The common method or action that will be performed 
                         on the selected object.
    - showWhenFun (function): A function that determines the visibility of 
                              each item in the menu. It should return a boolean 
                              value for each object in objectList.
    - getNameFun (function): A function that returns the name (as a string) of 
                             each object in objectList, which will be displayed 
                             in the menu.

    """
        self._items.append(OptionalRepeatedItems(objectList, action, showWhenFun, getNameFun))
            
            
        
    def addRepeatedItems(self, objectList, action, getNameFun):
        """
    Adds a group of items to the menu from a provided list of objects.

    This method is designed for situations where there's a variable-sized list 
    of objects that all share the same method, and all items should be displayed 
    in the menu.

    Parameters:
    ----------
    - objectList (list): A list of objects to be added to the menu.
    - action (function): The common method or action that will be performed 
                         on the selected object.
    - getNameFun (function): A function that returns the name (as a string) of 
                             each object in objectList, which will be displayed 
                             in the menu.

    """
        self._items.append(RepeatedItems(objectList, action, getNameFun))


    def menu(self, keys, *args):
        """
        Display and handle the menu operations.

        Parameters:
        ----------
        keys : list of lists
            List of the list of keys for menu options.
        *args : tuple
            Additional arguments for the menu items' actions.
        """
        while True:
            print(f"\n{self._open}")
            convertedList = []
            keyIndex = 0
            for item in self._items:
                if isinstance(item, OptionalMenuItems):
                    convertedList.extend(item.getItems(keys[keyIndex]))
                    keyIndex += 1
                elif isinstance(item, OptionalRepeatedItems) or isinstance(item, RepeatedItems):
                    convertedList.extend(item.getItems())
                else: convertedList.append(item)
            for i, item in enumerate(convertedList):
                index = i + 1
                if self._type == 'let':
                    index = chr(i + 65)
                print(f"{index}) {item.getStatement()}")
            print("X) Exit")
            inp = input(self._close).upper()
            if inp == 'X': return False
            print()
            orgInp = inp
            if self._type == 'num':
                inp = int(inp) - 1
            else:
                inp = ord(inp) - 65
            try:
                convertedList[inp].doAction(args)
                if self.breakAfterEx: return True
            except Exception as e:
                print(f"Error: {e}")
                print(f"{orgInp} is not a valid entry")


class MenuItem():
    """
    A class that represents an individual Menu Item.

    Attributes:
    ----------
    _statement : str
        The statement or description of the menu item.
    _action : callable
        The action to perform when this menu item is selected.
    _indexForRepeated : int
        For repeated items, holds the index of the list it was from
    """
    def __init__(self, statement, action, indexForRepeated = None):
        self._statement = statement
        self._action = action
        self._index = indexForRepeated

    def getStatement(self):
        return self._statement
    
    def doAction(self, *args):
        if self._index is not None:
            # print(f"Trying to do an indexed")
            self._action(*args, self._index)
        else:
            self._action(*args)

    def getAction(self):
        return self._action
    
class RepeatedItems:
    def __init__(self, objectList, getNameFun, action):
        self.objectList = objectList
        self.action = action
        self.getName = getNameFun

    def getItems(self):
        retList = []
        for i, obj in enumerate(self.objectList):
            retList.append(MenuItem(self.getName(obj, i), self.action, i))
        return retList


class OptionalMenuItems:
    def __init__(self, items, keys):
        if len(keys) == len(items):
            self.itemList = dict(zip(keys, items))
        else:
            raise ValueError("Invalid input")

    
    def getItems(self, keys):
        return [self.itemList[key] for key in keys if key in self.itemList]
    
class OptionalRepeatedItems:
    def __init__(self, objectList, action, determinorBooleanFun, getNameFun):
        self.objectList = objectList
        self.action = action
        self.deter = determinorBooleanFun
        self.getName = getNameFun

    def getItems(self):
        retList = []
        for i, obj in enumerate(self.objectList):
            if self.deter(obj, i):
                retList.append(MenuItem(self.getName(obj, i), self.action, i))
        return retList

class BlockedText:
    """
    Represents a text-based grid where elements are organized in rows and columns.

    Attributes:
        elements (list): A list of BTElement objects representing the elements in the grid.
        text (str): A string containing the formatted text grid.
    """

    def __init__(self, elements=[]):
        """
        Initializes a BlockedText instance.

        Args:
            elements (list, optional): A list of BTElement objects to initialize the grid with. Defaults to an empty list.
        """
        self.elements = elements

    def display(self, width=3, outline=False, charWidth=None, wSpacing=4, hSpacing=1):
        """
        Formats and displays the elements in a text grid.

        Args:
            width (int, optional): The number of elements to display in each row. Defaults to 3.
            outline (bool, optional): Whether to outline the grid. Defaults to False.
            charWidth (int, optional): The desired character width for the grid. Defaults to None.
            wSpacing (int, optional): The horizontal spacing between elements. Defaults to 4.
            hSpacing (int, optional): The vertical spacing between rows. Defaults to 1.

        Returns:
            str: The formatted text grid.
        """
        text = ""
        block_width = 0
        for element in self.elements:
            if element.longestLine > block_width:
                block_width = element.longestLine
        if charWidth:
            width = math.ceil(charWidth / block_width)
        block_height = 0
        for element in self.elements:
            if len(element.lines) > block_height:
                block_height = len(element.lines)
        rows = math.ceil(len(self.elements) / width)

        for element in self.elements:
            # make all blocks the same height
            for _ in range(0, block_height - len(element.lines)):
                element.addLine("")

        for row in range(rows):
            for block_height_count in range(block_height):
                for block_width_count in range(width):
                    try:
                        element = self.elements[block_width_count + row * width]
                        line = element.lines[block_height_count]
                        text += line
                        padding = block_width + wSpacing - len(line)
                        if padding > 0:
                            text += " " * padding
                    except Exception:
                        pass
                text += "\n"
            text += "\n" * hSpacing
        # Add vertical spacing

        return text

    def buildElement(self, title, string):
        """
        Creates a new BTElement and adds it to the elements list.

        Args:
            title (str): The title of the element.
            string (str): The content of the element.
        """
        self.elements.append(BTElement(title, string))

    def addElement(self, BTElement):
        """
        Adds an existing BTElement to the elements list.

        Args:
            BTElement (BTElement): The BTElement object to add.
        """
        self.elements.append(BTElement)


class BTElement:
    """
    Represents an element within a BlockedText grid.

    Attributes:
        lines (list): A list of strings representing the lines of text in the element.
        longestLine (int): The length of the longest line in the element.
    """

    def __init__(self, title, string=None):
        """
        Initializes a BTElement instance.

        Args:
            title (str): The title of the element.
            string (str, optional): The initial content of the element. Defaults to None.
        """
        self.lines = [title]
        self.longestLine = len(title)
        if string:
            self.addLine(string)

    def addLine(self, string):
        """
        Adds a line of text to the element.

        Args:
            string (str): The line of text to add.
        """
        strings = string.split("\n")
        self.lines.extend(strings)
        length = len(max(strings, key=len))
        if length > self.longestLine:
            self.longestLine = length


    

    # def appendLine(self, string, index=-1, space=True):
    #     if index == -1:
    #         index = len(self.lines) - 1
    #     if space:
    #         string = f" {string}"
    #     self.lines[index] += string
    #     length = len(self.lines[index])
    #     if length > self.longestLine:
    #         self.longestLine = length
			
	
		
		








        
            