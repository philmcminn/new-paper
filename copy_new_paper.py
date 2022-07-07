#!/usr/bin/env python3

# THE SOFTWARE IN THIS FILE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import sys
import shutil

if len(sys.argv) < 2:
    sys.exit("USAGE: python copy_new_paper.py [TARGET_DIR]")

src_path = os.path.dirname(os.path.realpath(__file__))
dest_path = sys.argv[1]

if os.path.isdir(dest_path):
    sys.exit(
        'Target directory "%s" already exists. Delete it first if you want to create a new paper there.'
        % dest_path
    )

# copy the contents of the new_paper directory to the new one
shutil.copytree(src_path, dest_path)

# change directory to the new directory
os.chdir(dest_path)

# remove certain files
os.remove("copy_new_paper.py")
os.remove("LICENSE")
os.remove("README.md")

# remove certain directories
shutil.rmtree(".git")
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
