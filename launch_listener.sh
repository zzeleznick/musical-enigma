# usr/bin/bash

launch() {
    echo "Hopefully ultrahook is on your syspath and your api key is on path as well..."
    exec ultrahook github 8000/api/git
}

launch