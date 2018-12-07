"""Web & Network security"""

"""Injections"""
import subprocess


def trans_code_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # Wrong idea!


"""Parsing XML"""
# <?xml version="1.0"?>
# <!DOCTYPE lolz [
#  <!ENTITY lol "lol">
#  <!ELEMENT lolz (#PCDATA)>
#  <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
#  <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
#  <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
#  <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
#  <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
#  <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
#  <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
#  <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
#  <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
# ]>
# <lolz>&lol9;</lolz>


"""assert command"""
def foo(request, user):
    assert user.is_admin, "user does not have access"


"""pickle"""
import zmq

import cPickle as pickle


class Server(object):
    def __init__(self):
        context = zmq.Context()

        self.receiver = context.socket(zmq.PULL)
        self.receiver.bind("tcp://*:1234")

        self.sender = context.socket(zmq.PUSH)
        self.sender.bind("tcp://*:1235")

    def send(self, data):
        self.sender.send(pickle.dumps(data))

    def recv(self):
        data = self.receiver.recv()
        return pickle.loads(data)
