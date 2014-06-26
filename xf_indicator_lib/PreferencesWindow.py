# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

### DO NOT EDIT THIS FILE ###

"""this window adjusts settings
"""

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('xf_indicator_lib')

from . helpers import get_builder, show_uri, get_help_uri

class PreferencesWindow(Gtk.Window):
    __gtype_name__ = "PreferencesWindow"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated PreferencesWindow object.
        """
        builder = get_builder('PreferencesXfIndicatorWindow')
        new_object = builder.get_object("preferences_xf_indicator_window")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initalizing should be called after parsing the ui definition
        and creating a PreferencesWindow object with it in order to
        finish initializing the start of the new PerferencesXfIndicatorWindow
        instance.
        
        Put your initialization code in here and leave __init__ undefined.
        """

        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.ui = builder.get_ui(self, True)

        # code for other initialization actions should be added here
