import arcade

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.
    Stereotype:
        Information Holder
    Attributes:
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
        _width (int): The actor's width
        _height (int): The actor's height
        _image (string): The file path of the image file (if present)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._text = ""
        self._position = 0
        self._velocity = 0
        self._width = 0
        self._height = 0
        self._image = ""

    def set_width(self, width):
        """Sets the actor's width.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._width = width

    
    def get_width(self):
        """Gets the actor's width.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Actor's width
        """
        return self._width
    
    def set_height(self, height):
        """Sets the actor's height.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._height = height

    def get_height(self):
        """Gets the actor's height.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Actor's height.
        """
        return self._height

    def set_image(self, image):
        """Sets the actor's image.
        
        Args:
            self (Actor): an instance of Actor.
        """
        self._image = image

    def get_image(self):
        """Gets the actor's image.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Actor's image.
        """
        return self._image

    def has_image(self):
        """Determine's if actor has an image or not.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Boolean.
        """
        return self._image != ""
        
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given position.
        """
        self._position = position

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def set_text(self, text):
        """Sets the actor's text.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            String: text.
        """
        self._text = text

    def get_text(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            string: The actor's textual representation.
        """
        return self._text


    def has_text(self):
        """Determine's if actor has text or not.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Boolean.
        """
        return self._text != ""

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            self (Actor): An instance of Actor.
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity