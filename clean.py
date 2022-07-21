#!/usr/bin/env python3

# THE SOFTWARE IN THIS FILE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

# Purpose:
#
# This script can be used to clear out the content in the *.tex files of
# new-paper and remove example files, allowing you to get started with your own
# content without having to first remove what's already there.
#
# Run at the command line using `./clean.py` or `python3 clean.py` depending
# on your OS/setup.

import os
import sys
import shutil

# ensure we're in the directory of this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# remove certain files, including this one
os.remove("clean.py")
os.remove("LICENSE")
os.remove("README.md")

# removing unneeded directories
shutil.rmtree("figures")
shutil.rmtree("graphics")
shutil.rmtree("table-data")
shutil.rmtree("tables")

# remove text in tex files in the sections directory
os.chdir("sections")

keep_lines = (
    "\\begin{abstract}",
    "\\end{abstract}",
    "\\section",
    "\\subsection",
    "\\label",
)
add_blank_lines = ("\\begin{abstract}", "\\label")
for file in os.listdir("."):
    if file.endswith(".tex"):
        output = ""
        with open(file, "r") as input:
            for line in input:
                if line.startswith(keep_lines):
                    output += line
                    if line.startswith(add_blank_lines):
                        output += "\n"
    tex_file = open(file, "w")
    tex_file.write(output)
    tex_file.close()
