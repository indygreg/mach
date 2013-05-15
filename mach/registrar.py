# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import unicode_literals

from StringIO import StringIO

from .base import MachError


class MachRegistrar(object):
    """Container for mach command and config providers."""

    def __init__(self):
        self.command_handlers = {}
        self.commands_by_category = {}
        self.categories = {}
        self.settings_sections = {}

    def register_command_handler(self, handler):
        name = handler.name

        if not handler.category:
            raise MachError('Cannot register a mach command without a '
                'category: %s' % name)

        if handler.category not in self.categories:
            raise MachError('Cannot register a command to an undefined '
                'category: %s -> %s' % (name, handler.category))

        self.command_handlers[name] = handler
        self.commands_by_category[handler.category].add(name)

    def register_category(self, name, title, description, priority=50):
        self.categories[name] = (title, description, priority)
        self.commands_by_category[name] = set()

    def register_setting(self, section, option):
        self.settings_sections.setdefault(section, []).append(option)

    def configspec(self):
        """Obtain a ConfigObj config spec for registered settings."""
        s = StringIO()
        for section, options in self.settings_sections.items():
            s.write('[%s]\n' % section)
            s.writelines(options)

        return s


Registrar = MachRegistrar()

