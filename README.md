# LaTeX Repository for Writing New Papers

This repository is designed to be forked by PhD students when they want to start
writing a new research paper for a conference, journal, or an internal report.

It provides a skeleton set of files and folders in which you can write your own
material, and customise your paper with additional macros.

Each section provides advice as to how to go about writing it. This advice can
be deleted or comment out to make way for your own content.

## Creating a Repository for Your Own Paper by Forking This One

In the top-right hand corner of the GitHub page for the repository, there should
be a button named "Fork". Click this to fork the repository into your own space.

The new repository will still be called "new-paper", which you will want to
change. To do this, go the "Settings" tab and rename it. Choose a name that is
indicative of the paper's *research content*, rather than the conference venue
or journal you intend to submit it to. For example, "search-based-testability"
is a better name than "icse2020".

For the same reasons as [detailed next](#file-and-directory-naming), choose a name
formatted in "kebab-case" (i.e., all lower case with hyphens as word separators).

## File and Directory Naming

Over time, you will be adding your own files and content to your paper The
various files and examples in this repository show you how to go about doing
that.

Please ensure you stick to the coding standards described in the comments of the
paper. This helps ensure everything is consistent, that other people working
with you (me, and and other collaborators) can find things easily (such as a
figure file referenced using a certain label in a section file), and in general
helps uphold the [Principle of Least
Surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)
for others when working on the paper.

In particular, the repository opts to use
"[kebab-case](https://wiki.c2.com/?KebabCase)" for naming files and directories.
All file and directory names following the kebab-case convention are
lower-cased, with words separated with hyphens. Using lower-casing and not using
spaces in file and directory names ensures good cross-platform compatibility.

## Further LaTeX Tips

The comments of this paper offer a number of tips on how to write good
LaTeX. There is a lot of other good advice on the web, too. See, for example,
the following links:

* [Advice for Writing LaTeX Documents](https://github.com/dspinellis/latex-advice),
  by Diomidis Spinellis
* [John's Small Collection of LaTeX Tips](https://john.regehr.org/latex/),
  by John Regehr

Bear in mind that sometimes the advice given is subjective, and hence
contradictory.

You should follow the guidelines specified by this repository over others if you
find that they are contradictory to advice given elsewhere.

For example, this repository chooses to structure papers by splitting its
content across several files. This is because I prefer to structure papers in a
modular fashion, much like a computer program. It is not hard to find things
using text search in a good text editor, so long as you include all the relevant
files in the scope of the search.
