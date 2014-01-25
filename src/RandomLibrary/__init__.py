from keywords import RandomKeywords

class RandomLibrary(RandomKeywords):
    """ RobotFramework-Random (RF-Random)is a keyword library that includes
    a bunch of random utilities that aren't found in the default libraries.
    https://github.com/svyzz/robotframework-random

    We wrote a bunch of custom keywords to fit the needs of our project and
    realized later on that this would be incredibly useful to others too.
    This, however, is a work in progress. We intend to create pull requests and push
    specific keywords from this library to any other applicable library when the
    need arises.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'