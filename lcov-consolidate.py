#!/usr/bin/env python

"""
mbed SDK
Copyright (c) 2011-2016 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author: Conor Keegan <Conor.Keegan@arm.com>
"""

import argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="Tool to generate a single lcov info file")

parser.add_argument('-a', '--add-file',
                    required=True,
                    dest='all_files',
                    action='append',
                    help='Add multiple lcov info files to be joined into a single output file')

parser.add_argument('-o', '--output-file',
                    required=True,
                    dest='output_file',
                    help='Path of the output file to put the results of all of the specified info files')

options, remainder = parser.parse_known_args()

# Need the first fiel to generate the output file
call_list = ["lcov -a %s -o %s %s"% (options.all_files[0],
                                     options.output_file,
                                     " ".join(remainder))]

for file in options.all_files[1:]:
    call_list.append("lcov -a %s -a %s -o %s %s"% (options.output_file,
                                                   file,
                                                   options.output_file,
                                                   " ".join(remainder)))

# Call each of the commands individually
for call in call_list:
    print ("lcov command: %s" % call)

    _stdout, _stderr, ret = None, None, -1
    try:
        p = Popen(call, stdout=PIPE, stderr=PIPE, shell=True)
        _stdout, _stderr = p.communicate()
        ret = p.returncode
    except OSError as e:
        print (str(e))
        ret = -1

    if _stdout:
        print _stdout
    if ret:
        print ("lcov exited with error: %d, dumping stderr..." % ret)
        print _stderr