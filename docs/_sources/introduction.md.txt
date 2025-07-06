Introduction
============

Motivation
----------
Very often in labs you need to monitor a particular device which has an old seven segment display or the like that if it falls outside of a given parameter the experiment is no longer valid. This includes -80's that keep things cool and prevents degradation of samples and incubators which are needed to grow samples for a specified amount of time. The idea of Lab Partner is to have a Raspberry Pi with a USB camera pointed at the display and it uses Machine Learning to

1. read the display to monitor this range to either let you know that this situation has occurred to tell you that you need to start again or
2. to notify you as it happens so you can salvage your experiment before it is unsalvageable.
