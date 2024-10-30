class ToolBox:
    def __init__(self):
        self._tools_info = ""

    @property
    def tools_info(self):
        """
        Returns the tools_info field
        """
        return self._tools_info.strip()
    
    def recreate_tools_info(self, functions_list):
        """
        Recreates and returns tools into object as string.
        The str object holds the name and documentation of each function in the given list.

        Parameters:
        functions_list (list): List of function objects to build tools info form.

        Returns:
        str: Dictionary of function names (keys) and their documentation (values) as a string.
        """
        if len(functions_list) == 0:
            self._tools_info = ""
            return self.tools_info
        
        tools_info_dict = {}
        for func in functions_list:
            tools_info_dict[func.__name__] = func.__doc__
        
        self._tools_info = ""
        for name, doc in tools_info_dict.items():
            self._tools_info += f"{name}: \"{doc}\"\n"
            
        return self.tools_info
