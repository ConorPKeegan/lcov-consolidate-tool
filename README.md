# Table of Contents
* [Summary](#summary)
* [Parameters](#parameters)
* [Examples](#examples)

# Summary
This is a very simple Python tools to consolidate lcov INFO files into a single INFO file.
All of the files are combined individually to ensure that even if some of the files are corrupt, that an INFO file with the rest will be included.

# Parameters
* `-a`, `--add-file`: This option can be used multiple times to specify all of the files that are to be consolidated
* `-o`, `--output-file`: This option specifies the file that will be all of the other files consolidated.
* `*`: Any additional command line options that are specified, will be added to the end of the lcov command that is run. This allows for things such as adding `--gcov-tool` to the end of the commands.

# Examples
```
$ python lcov-consolidate.py -a file1.info -a file2.info -a file3.info -o output.info --gcov-tool my-gcov-tool
```