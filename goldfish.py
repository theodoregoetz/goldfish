#!/usr/bin/env python3
#
# Copyright (C) 2014-2015 Christopher Hewitt
#
# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

import platform
import sys

from ui_proc_list import MemViewUIProcListWindow
from reader import MemViewReader, MemViewError

if __name__ == '__main__':
    if platform.system() != 'Linux':
        print('this will probably not work unless you are using linux...')

    try:
        window = MemViewUIProcListWindow()
        reader = MemViewReader()

        window.update_process_liststore(reader.read_proc_stat_all())

        _, msg = reader.ptrace_scope_status()
        window.update_ptrace_label(msg)

        window.run()
    except MemViewError as err:
        print('error: {msg}'.format(msg=err))
        sys.exit(-1)
    except KeyboardInterrupt:
        pass

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python
