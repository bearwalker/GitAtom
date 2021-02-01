#! /usr/bin/env python3
from pygit2 import Repository, Index
from pygit2 import GIT_STATUS_INDEX_NEW, GIT_STATUS_INDEX_MODIFIED


# Setting the working directory
repo = Repository('.')


# Returns the staged files in a list
# -note if you ADD a file then make new changes to it, it won't show up in the
# list

def git_staged_files(repo):
    index = Index()
    status = repo.status()
    staged_files = [] 
    for filepath, flags in status.items():
        if flags == GIT_STATUS_INDEX_NEW or flags == GIT_STATUS_INDEX_MODIFIED:
            staged_files.append(filepath)
    return staged_files

files = git_staged_files(repo)
print(files)


# diff_workdir and index_workdir both found in the test dir in the pygit2 repo
# they seem like cleaner ways to get list of files, but they don't do exactly
# what we are looking for

# Currently display all tracked files that have been modified
# so modified staged and unstaged files 
def diff_workdir(testrepo):
    repo = testrepo
    head = repo[repo.lookup_reference('HEAD').resolve().target]

    diff = head.tree.diff_to_workdir()
    files = [patch.delta.new_file.path for patch in diff]
    print(files)

    diff = repo.diff('HEAD')
    files = [patch.delta.new_file.path for patch in diff]
    print(files)


    


# Getting closer, now only looks at non added modified files just need to figure
# out how to just look at added modified files but It will likely look very
# similar to this

def index_workdir(testrepo):
    diff = testrepo.diff()
    files = [patch.delta.new_file.path for patch in diff]
    print(files)









# The stuff past this point is me testing random things trying to get addded
# files



# Head is the last commit added.
# Head^ is the commit before the last commit
# Head^^ is one more back from Head^
# Head~3 is to use a numberd amount - this works for git, unkown for pygit2


#diff = repo.diff('HEAD')

#print("Insertions" , diff.stats.insertions)
#print("files deleted" , diff.stats.deletions)
#print("files changed" , diff.stats.files_changed)

# This will print out the path of files that have been modified but not
# added/staged
# a good example would be to change the README.md and the GITATOMDOCS.md.
# This will print both file names if changes are made.



#diff2 = repo.diff(cached=False,flags=1)
#print("diff2 is a:", diff2)
#for i in diff2.deltas:
#    print("test", i.new_file.path)

#Prints out changes from the last commit - i think
# The text is the text of all the lines changed.


#patches = [p for p in diff]
#print(patches)
#for p in patches:
#    print(p.text)



# This gets the number of files added"
#print(diff.stats.files_changed)
#
#print(diff.stats.format(3, 3))





