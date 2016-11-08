#!/bin/bash -xe

if [ ! -d "/home/vagrant/.pyenv" ]; then
    echo "Installing pyenv"
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    pyenv install 3.5.2
fi

if [ ! -d "/home/vagrant/.pyenv/plugins/pyenv-virtualenv" ]; then
    echo "Installing plugin pyenv-virtualenv"
    git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    eval "$(pyenv virtualenv-init -)"
    pyenv virtualenv 3.5.2 pycon
fi
