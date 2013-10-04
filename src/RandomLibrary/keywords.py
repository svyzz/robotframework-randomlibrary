import urllib
import datetime

class RandomKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def obtain_timestamp(self):
      '''
        Description:   Returns the current timestamp in the YYYY-MM-DD(T)HH-MM-SS format. 
                       Use this to generate timestamps that can then be appended to
          		       generate unique identifiers.
        Returns:       string
      '''
      utctime = datetime.datetime.utcnow().strftime("%Y-%m-%d" + "T" + "%H-%M-%S")
      return utctime


    def calculate_percentage(self, m, n):
      '''
        Description:   Returns the percentage of number m as a measure of number n; 
                       For example,  calculate percentage (1, 10) would return 10
        Returns:       int
      '''
      ret=float(p1)/float(100) * float(p2)
      if(ret < 1):
        result=1
      else:
        result=ret

      return int(result)


    def remove_newline(self, str):
      '''
          Description:   Removes the trailing new line character (\n) from a given string 
          Returns:       string
      '''
      return str.rstrip('\n')


    def remove_extra_spaces(self, str):
      '''
          Description:   Removes all extra spaces from a given string. 
                         For example, <string>\s\s<string> is corrected to <string>\s<string>
          Returns:       string
      '''
      return str.strip()


    def encode_url(self, url):
      '''
        Description:     Encodes the given url that would (probably) contain characters outside the ASCII set into a valid ASCII format
        Returns:         string
      '''
      return urllib.quote_plus(url)


    def decode_url(self, url):
      '''
        Description:     Decodes the given url back into their single-character equivalent
        Returns:         string
      '''
      return urllib.unquote_plus(url)