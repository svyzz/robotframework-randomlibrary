# Set the virtual environment home, relative to your Jenkins workspace
# The name could be '.pyenv' or anything else that you want
PYENV_HOME=$WORKSPACE/.pyenv

# Delete/Remove your previously built virtual environment
if [ -d $PYENV_HOME ]; then
rm -rf $PYENV_HOME
fi

# Create a new virtualenv and install all the necessary packages
virtualenv -p python2.7 $PYENV_HOME
. $PYENV_HOME/bin/activate

# You could also run "pip install --quiet $WORKSPACE/" where your setup.py file lives
pip install --quiet robotframework
pip install --quiet robotframework-httplibrary
pip install --quiet robotframework-selenium2library

# Specify the display here since we're using Xvfb (Xvfb :99 -ac -screen 0 1280x1024x24 +extension RANDR)
# 99 is the display ID and we're making this the default display
export DISPLAY=:99

#Execute our tests!
pybot -L TRACE tests