### Simple Terminal Parser

This is no <a href="http://codezen.org/canto-ng/2012/07/18/canto-0-8-0/">Canto</a>.

Just a simple feed reader with

    * no fancy UI
    * no interaction
    * but also no configuration files and nothing.

Suitable for guys reading news at terminal like pretending to work.

Just scroll the feed and save to your <a href="http://getpocket.com/a/">pocket</a> for later read.


### Dependencies

* <a href="https://docs.python.org/dev/library/argparse.html">argparse</a>

* <a href="https://pythonhosted.org/feedparser/basic.html">feedparser</a>

    $ pip install argparse
    $ pip install feeparser

### Usage

    $ python feedparser.py -w <i>website-initials</i>

### Default configured websites

    * Product Hunt
    * Hacker News
    * Growth Hackers
    * Researcher IO
    * Designer News
    * Side Bar
    * Slash Dot
    

### I want to add more websites.

Go ahead and modify **website_list** dictionary list.