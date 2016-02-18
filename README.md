# Ren'Py Navigation
by kerickso at github

Four files made to help you set up a basic navigation system for Ren'Py. A little experiment I've made to practice using Python but also be prepped for game jam.

This is an example of the implementation of it. IMPORTANT:: To test, create a new Ren'Py project, add these files, and remove or comment out the start label in script.py.

## Overview
These files allow you to create a navigation system with buttons at the top, bottom, left, and right of the screen. Allows each system to have both a label name (should be the same as the label of the location - see init_locations.rpy) and a nickname that will display on the links to them.

Create one-way paths from an edge of one location to another location (independent of the edges on the second).

Note this is not a complete Ren'Py Project - only four files to add into a given project. To test, place in the game directory of a new Ren'Py project, then go to the start label in script.rpy, and add the line "jump location1".

## File 1: ui_nav.rpy
This is a file that creates a new screen for the User Interface for navigation. Sets up all the buttons and pretty print. Will need to be edited if you don't want buttons or if you want to change the size of the screen.

## File 2: navigation.rpy
This is a file that creates the Location class.

## File 3: init_locations.rpy
Sets up Location objects, connections, and location's labels. Edit directly for adding new locations.

## File 4: check_events.rpy
Has function check_location() that searches for an event at the given location. Also has labels specific to different events.
