# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import unicode_literals

import os
import unittest

from StringIO import StringIO

from mach.main import Mach


class TestSettingsLoading(unittest.TestCase):
    def _get_mach(self):
        m = Mach(os.getcwd())
        m.define_category('test', 'test', 'test commands')
        common_path = os.path.join(os.path.dirname(__file__), 'common.py')
        m.load_commands_from_file(common_path, 'mach.commands.settings_test')

        stdout = StringIO()
        stderr = StringIO()
        stdout.encoding = 'UTF-8'
        stderr.encoding = 'UTF-8'

        return m, stdout, stderr

    def test_filename_precedence(self):
        # No arguments and no environment variables should result in empty
        # settings object.
        m, stdout, stderr = self._get_mach()
        result = m.run(['simple'], stdout, stderr)

        self.assertEqual(result, 0)
        self.assertIsNone(m.settings.filename)
        self.assertEqual(len(m.settings), 0)

