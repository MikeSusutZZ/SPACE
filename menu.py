# Designed by Mike Susut, (ZippidyZap, MikeSusutZZ)

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
        for obj in self.objectList:
            retList.append(MenuItem(self.getName(obj), self.action))
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








        
            
