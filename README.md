# SUNCORP
# Software Engineering Programming Exercise – Toy Robot

This repository provides an implementation for the Toy Robot exercise. This repository houses a set of modules that allow an operator to transverse a Toy Robot around a grid field using a limited set of commands.

## Overview

This guide aims to get a copy of the implementation running on your local computer for development, testing, and deployment purposes.

## Requirements

The Toy Robot modules were designed and validated using Python 2.7.9 on a Linux environment with access to the console command prompt. No external libraries nor modules are required.

## Design
The Toy Robot implementation is separated into a set of classes:

The Application class uses a message pump allowing a console operator to input a series of commands that are then processed by the Toy Robot. The Application class has a single static member function.

The Command class parses all of the input from the console operator. This class shall raise custom exceptions with detailed messages instead of printing error or logging messages. This ease's testing as it is more efficient to detect and measure an exception compared to a printed string. The Command class is used as input to the Robot class to control the Toy Robot.

There is a Compass module that contains a few utility functions for validating and printing compass headings.

A Robot class exists that processes actions from instances of the Command class. This class also raises custom exceptions with detailed messages instead of printing error or logging messages. The Robot class maintains the following state information:
* Current X and Y positioning
* Current compass heading
* Knowledge whether it has received and successfully actioned a placement command
* The size of the grid field

A design decision was made to accept and process Robot *move* actions when at the edge of the grid field without raising nor displaying an error. When a Robot is at the edge of the grid field and a *move* action is commanded, the Robot shall simply stay at it's current position.

There is also a standalone Test class. See section Running the tests for notes. 

All classes are loosely coupled, and dependencies have been minimised as a design focus.

## Installation

No installation required.

## Running the Tests
A Test module is included which runs a small set of positive and negative unit tests across the Toy Robot infrastructure. Running the tests is simple:

```
> python Test.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK

```

## Usage
The Toy Robot application supports the full range of navigation commands:
* PLACE X, Y, H
* MOVE
* TURN H
* REPORT

X = X co-ordinate on a grid field.
Y = Y co-ordinate on a grid field.
H = Heading - N, E, S, or W.

The commands can be input from the console command line one at a time. The commands are case insensitive. Upon the input of an invalid command, an error message shall be displayed and the application shall continue. To exit the application, use the CTRL-C key set.

## Example Run
```
> python Application.py


Welcome to the Toy Robot application.

Proceed to enter commands. Press CTRL-C to exit.

> place 2, 4 N
> report
The Toy Robot is at position 2,4 facing North
> turn W
> report
The Toy Robot is at position 2,4 facing West
> move
> move
> REport
The Toy Robot is at position 0,4 facing West
>
```

## Version

The release date of the modules is August 2018.

## Authors

* **Simon Flannery** - *Initial work*
