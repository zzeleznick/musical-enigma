# usr/bin/bash

message()
{ # This will print out to the user what the program is doing
  echo "We will be make a curl post to our listener."
  echo curl -X POST -d '{"fizz": "buzz", "foo": "bar", "url": "http://127.0.0.1:8000/"}' http://github.zzz.ultrahook.com -H "Content-Type: application/json"
}

post ()
{
    # we need to sleep a little bit to prevent blocking
    sleep 2
    # throw a post to our local endpoint!
    curl -X POST -d '{"fizz": "buzz", "foo": "bar", "url": "http://127.0.0.1:8000/"}' http://github.zzz.ultrahook.com -H "Content-Type: application/json"
}

message
post