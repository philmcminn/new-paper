# LaTeX Repository for Writing New Software Engineering Papers with Empirical Evaluations

* [Introduction](#introduction)
* [Create a Repository for Your Own Paper by Copying the Contents of This One](#create-a-repository-for-your-own-paper-by-copying-the-contents-of-this-one)
* [Naming Your Repository](#naming-your-repository)
* [Setting up Your Writing Environment](#setting-up-your-writing-environment)
* [Building Your Paper at the Terminal](#building-your-paper-at-the-terminal)
* [File and Directory Naming – Use `kebab-case`](#file-and-directory-naming--use-kebab-case)
* [What Shouldn't Be in Your Paper Repository](#what-shouldnt-be-in-your-paper-repository)
  * [Types of Files That You Should Set Git to Ignore](#types-of-files-that-you-should-set-git-to-ignore)
  * [Put All Experimental Materials in a Separate Repository](#put-all-experimental-materials-in-a-separate-repository)
* [General Writing Tips](#general-writing-tips)
  * [Avoid Passive Voice](#avoid-passive-voice)
  * [British vs American Spelling](#british-vs-american-spelling)
  * [Numbers](#numbers)
* [Further Advice](#further-advice)
  * [What to Do If the Advice Conflicts](#what-to-do-if-the-advice-conflicts)

## Introduction

This repository is designed to be used by new researchers (e.g., PhD and Masters
students) when they want to start writing a new research paper for a software
engineering conference, journal, or an internal report.

It provides a skeleton set of files and folders in which you can write your own
material, and customise your paper with additional macros.

Each section provides advice as to how to go about writing it. This advice can
be deleted or commented out to make way for your own content.

The format assumes that you have researched a new technique that have
empirically evaluated. If you want to write a purely empirical paper, you may
need to tweak the sections. However, it is not really suitable for a paper that
involves only proofs and no empirical study.

## Create a Repository for Your Own Paper by Copying the Contents of This One

At the time of writing, GitHub does not allow you to fork a publicly-available 
repository like this one and then make it private. So assuming you want your
new paper to be a private repository, simply create a new repository of your
own, and having already cloned this one, copy the contents across (ensuring
you copy all of the files, including the `.gitignore` file, which may be hidden
by GUI-based directory browsing programs like Finder or Explorer).

If you _do_ want to fork the repository, then in the top-right hand corner of 
the main page for the repository, there should be a button named "Fork". Click 
this to fork the repository into your own space. The new repository will still 
be called "new-paper", which you will want to change. See the next section on
how to do this.

## Naming Your Repository

In terms of the name of your repository, choose one that is indicative of the
paper's *research content*, rather than the conference venue or journal you
intend to submit it to. For example, "search-based-testability" is a better name
than "icse2020". This is because you may decide later to submit your work to a
different venue. Or, your work may not be accepted to the first venue you submit
to, and you may need to revise your paper and submit it to another. In either
case, the original venue name will no longer be a suitable choice of name for
your repository.

For the same reasons as those
[detailed in the next section](#file-and-directory-naming), choose a name formatted
in "kebab-case" (i.e., all lower case with hyphens as word separators).

GitHub repositories can be re-named at any time. To do this, go the "Settings" tab.
Note that you may need to reclone the repository on your local machine after doing
this.

## Setting up Your Writing Environment

I suggest you set up a development environment similar to one that you'd use for
developing software, but which will automatically compile your LaTeX and build
a PDF.

There are plenty of tools around to assist you in this process, and I have used
a number over the years. Currently, I use [Visual Studio
Code](https://code.visualstudio.com/) (VSCode for short), which is free and
open source, with the [LaTeX
workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
plugin. Among other things this plugin automatically builds my PDF every time I
make a change to a `.tex` source file. With VSCode, I can display the PDF in an
editor tab so that I can see it while I am working on it, and have it update
while I edit it. Others prefer more "traditional" solutions such as Vim or
Emacs, but you can use whatever you prefer, and – so long as you do not [add any
settings or backup files produced by your editor to the
repository](#what-shouldnt-be-in-your-paper-repository) – your personal choice
can co-exist alongside that of your collaborators.

Whatever environment you use, ensure you have a spell checker installed! (Again,
VSCode has a plugin for one of these.) You will also find various other plugins
useful, for example those that manage tabs/spaces and remove trailing spaces in
your source text files.

## Building Your Paper at the Terminal

Even if you're using an integrated development environment to compile your paper,
you will probably at some point need to compile the paper from a terminal window.
If you're working with me, then I don't mandate that you use a Make file or any 
particular build tool, but I'm happy if that's what you want to do – so long as 
you leave some instructions if they're needed. Some students just include a build 
script in the root directory of their repository for convenience.

The root file is `paper.tex`, and typically you will need to run LaTeX and
BibTeX a couple of times to resolve all of the references properly in the
document:

```
pdflatex paper
bibtex *.aux
pdflatex paper
pdflatex paper
```

## File and Directory Naming – use `kebab-case`

Over time, you will be adding your own files and content to your paper. The
various files and examples in this repository demonstrate how to go about doing
that.

Please ensure you stick to the coding standards described in the comments of the
paper. This helps ensure everything is consistent, that other people working
with you (i.e., me, and possibly other collaborators) can find things easily (such as a
figure file referenced using a certain label in a section file), and in general
helps uphold the [Principle of Least
Surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)
for others when working on the paper.

In particular, the repository opts to use
"[kebab-case](https://wiki.c2.com/?KebabCase)" for naming files and directories.
All file and directory names following the kebab-case convention are
lower-cased, with words separated with hyphens. Using lower-casing and not using
spaces (i.e., by using hyphens instead) in file and directory names ensures good
cross-platform compatibility.

## What Shouldn't Be in Your Paper Repository

You can exclude files from the repository using the provided `.gitignore`file as
a starting point. This file lives in the repository's root directory, and
already covers some of the file types discussed next, although your particular
paper may develop to include some more.

### Types of Files That You Should Set Git to Ignore

Firstly, do not commit build files to the repository, in particular the target
PDF file (`paper.pdf`). You should also avoid committing:

* Temporary build files that LaTeX and BibTeX produce (e.g., `paper.aux`, etc.)

* Operating system files (e.g., `.DS_Store` on macOS) that can be particularly
  irritating for users of other systems.

* Editor backup files (e.g., `.bak` files), and editor settings files (e.g.,
  `.vscode`), if you can avoid them.

### Put All Experimental Materials in a Separate Repository

You should use a *separate* Git repository for all of your experimental data
and materials. That is, keep your paper repository for LaTeX files only,
or graphics/TikZ files etc. that are directly involved in the production
of your paper.

If the build of your paper needs to generate tables or figures from your raw
data, consider including it in the paper repository as a separate
[Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
instead. A Git submodule is just a way of using some other Git repository in
another, but where the two repositories can still be maintained independently.

## General Writing Tips

The text and comments embedded in the `.tex` files of this paper discuss how to
go about writing each section of the paper. Check them out! They also discuss
the conventions you should follow and contain a number of tips on how to write
good LaTeX.

What follows is a more general overview of writing style that applies throughout
your paper:

### Avoid Passive Voice

First of all, please avoid passive voice. When you write in passive voice,
you're excluding the "actor" from the sentence so that objects have things done
to them rather than someone/something doing the action. This makes your
sentences vague and imprecise. For example, it's important to know whether the
steps in your empirical study were manual or automated (did you do them, or was
it done automatically by your tool?). Passive voice often excludes these details
and can confuse readers and referees. Consider the sentence "test suites were
generated for the subjects 30 times" (passive voice) vs. "our tool generated
test suites for the subjects 30 times" (active voice). In multi-author papers,
using "we" to say "we did it" is preferred to writing that something "was done",
and to convey something in an experiment that was necessarily manual step, or
involved you making a choice from a series of possible options. Any of these
could apply to when you want to write about deriving an algorithm, implementing
a tool, choosing a particular aspect of an experiment's design, and so on.

Sometimes it is difficult to identify passive from active voice! This is where
the ["zombies"
tip](https://www.grammarly.com/blog/a-scary-easy-way-to-help-you-find-passive-voice/)
comes in useful: If you can add "by zombies" after the verb in the sentence, and
it still makes sense, you probably have a sentence in passive voice.

### British vs American Spelling

As I remarked earlier in these instructions, please ensure you use a spell
checker! Many text editors enable you to install a plugin so that you can see
any misspelled words while you're editing your document.

British English or American English? Check with your supervisor if there is a
potential decision to make here. If you're working with me, then I'm fine with
whichever, so long as everyone working on the paper knows (and doesn't keep
changing the spellings from one version of English to another).

For some publications, particularly American journals, the publisher will change
all British spellings to American anyway (e.g. IEEE, ACM). I often just go with
American even though I'm a Brit, because the spellings are often shorter – every
character of space in a paper is important! :-)

Note that there are some words that are still used in every day British English
that have disappeared from American English. These words sound odd and quaint to
the American ear (so you may find them silently corrected in your paper,
especially if working with an American collaborator). Top of this list is the
word "whilst". Just use "while" instead.

### Numbers

There are certain rules around writing numbers that just look "right" but
generally have no particular explanation, and are just part of generally
accepted scientific writing style. In general, numbers should appear as numbers,
but there are some special cases where you should write them out as words, for
example:

* At the start of sentence. Write "Thirty-seven of the subjects..." as opposed
  to "37 of the subjects...", or even better, just re-word the sentence so that
  the number doesn't appear at the start, as both look a little bit strange.

* Numbers less than or equal to ten in the middle of a sentence (this sentence
  is an example) – unless you're quoting actual data points from your
  experiment.

## Further Advice

There are a number of good resources on the web, that you should check out too.

See, the following links, for example:

* [Advice for Writing LaTeX Documents](https://github.com/dspinellis/latex-advice),
  extensive guidance on LaTeX style, by Diomidis Spinellis.

* [Things I Keep Repeating About Writing](https://clairelegoues.com/2016/08/23/things-i-keep-repeating-about-writing/),
  an excellent blog post by Claire Le Goues that covers more aspects and tips
  related to writing style than covered here.

* [My top ten presentation issues in other's papers](https://andreas-zeller.blogspot.com/2013/04/my-top-ten-presentation-issues-in.html),
  a collection of bug-bears in papers found by Andreas Zeller while reviewing
  papers, each of which you should avoid!

* [Guide to Punctuation](http://www.sussex.ac.uk/informatics/punctuation/toc) –
  a good and detailed guide to every punctuation symbol in English, and when to
  use it. Covers differences in American usages.

There are some popular text books that are worth looking at as well (you're welcome
to borrow them from me), these include:

* [BUGS in Writing: A Guide to Debugging Your Prose](https://www.goodreads.com/book/show/601222.Bugs_in_Writing), by Lyn Dupre.

* [Writing for Computer Science](https://www.goodreads.com/book/show/117973.Writing_for_Computer_Science), by Justin Zobel.

Finally, some good tutorial papers written by Mary Shaw. This are a little old
now, but the advice in them is still good and relevant!

* [Writing Good Software Engineering Papers.](https://www.cs.cmu.edu/~Compose/shaw-icse03.pdf)
_Proceedings of the International Conference on Software Engineering (ICSE), 2003._

* [What Makes Good Research In Software Engineering?](https://www.cs.cmu.edu/~Compose/ftp/shaw-fin-etaps.pdf)
_International Journal of Software Tools for Technology Transfer, vol. 4, no. 1, 2002._

### What to Do If the Advice Conflicts

Bear in mind that sometimes the advice given is subjective, and hence
contradictory, in which case you're free to make up your own mind — although
you may wish to discuss it with your supervisor first! If the route you take 
has a significant impact on the way you will write or structure your paper, 
you should discuss and get the agreement of all of your collaborators.

For example, this repository chooses to structure papers by splitting its
content across several files. This is because I think it is better to structure
LaTeX documents in a modular fashion, much like a computer program. This
approach will help you re-use components of your papers that you have written
when you start to work on your Masters dissertation, or PhD thesis. A common
objection to doing it this way is that it makes it harder to find specific text
later. But, if you structure your files in the way this repository suggests,
finding things again should not be difficult – in fact, it should be very easy.
Furthermore, if you get really stuck, then it is not hard to use the "Find"
feature of a good text editor, so long as you include all the relevant files in
the scope of the search.
