#!/bin/bash

# Script to set up dependencies for Django on Vagrant.

# Installation settings

# Install essential packages from Apt

apt-get update -y
apt-get upgrade -y

# Python dev packages
sudo apt-get install -y \
autotools-dev      \
blt-dev            \
bzip2              \
dpkg-dev           \
g++-multilib       \
gcc-multilib       \
libbluetooth-dev   \
libbz2-dev         \
libexpat1-dev      \
libffi-dev         \
libffi6            \
libffi6-dbg        \
libgdbm-dev        \
libgpm2            \
libncursesw5-dev   \
libreadline-dev    \
libsqlite3-dev     \
libssl-dev         \
libtinfo-dev       \
mime-support       \
net-tools          \
netbase            \
python-crypto      \
python-mox3        \
python-pil         \
python-ply         \
quilt              \
tk-dev             \
zlib1g-dev         \
git                \
nginx              \
debconf-utils      \
pv                 \
htop               \
enchant            \
libjpeg-dev        \
libjpeg8-dev       \
libpq-dev          \
redis-server       \
# to fix pip install pylibmc
libmemcached-dev   \
zlib1g-dev

# Or for Ubuntu 64bit:
# ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# Or for Ubuntu 32bit:
# ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/
# ln -s /usr/lib/i386-linux-gnu/libfreetype.so.6 /usr/lib/
# ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/
