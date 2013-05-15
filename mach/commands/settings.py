# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import print_function, unicode_literals

from mach.decorators import (
    CommandArgument,
    CommandProvider,
    Command,
)


@CommandProvider
class Settings(object):
    """Interact with settings for mach.

    Currently, we only provide functionality to view what settings are
    available. In the future, this module will be used to modify settings, help
    people create configs via a wizard, etc.
    """
    def __init__(self, context):
        self.settings = context.settings

    @Command('config', category='devenv',
        description='Show and manipulate config settings.')
    @CommandArgument('--global', action='store_true', dest='on_global',
        help='Operate on the global config file.')
    @CommandArgument('action', choices=['get', 'set', 'show'])
    def config(self, on_global=False, action=None):
        print(action)

