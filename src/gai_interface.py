

class GenAIconnector:
    """
    A class to connect and interact with the OpenAI API. Potential to to choose between different APIs
    
    Attributes:
    ----------
    key : str
        The API key for authentication.
    """
    
    def __init__(self, key):
        """
        Initializes the GenAIconnector with the provided API key.
        
        Parameters:
        ----------
        key : str
            The API key for authentication.
        """
        self.key = key
        
    def OpenAIconnect(self, request):
        """
        Connects to the OpenAI API and sends a chat completion request.
        
        Parameters:
        ----------
        request : str
            The content of the user's request.
        
        Returns:
        -------
        dict
            The response from the OpenAI API.
        """
        from openai import OpenAI

        # Initialize the OpenAI client with the provided API key
        client = OpenAI(
            api_key=self.key
        )

        # Create a chat completion request
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Specify the model to use
            store=True,           # Store the response
            messages=[
                {"role": "user", "content": request}  # User's message
            ]
        )
        return completion


