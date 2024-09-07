# git_assignment_HeroVired

Question - 1

a. Create a repository name: git_assignment_HeroVired

b. Create a ‘dev’ branch and add the calculator code.

c. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.

d. Add any of your classmates as collaborators.

e. Implement a feature by creating a new branch called ‘feature/sqrt’. f. Add the ‘sqrt’ code to it.

g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: def divide(self, a, b):

if b == 0:

raise ValueError("Cannot divide by zero.")

return a / b

h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.

i. Request a code review from a team member and make any necessary improvements based on the review feedback.

j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.

k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.

Question - 2

 For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly.

In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.

Question - 3

In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

Workflow Steps:

a. Create a New Branch:
- Create a new branch named "feature/circle-area" to work on the circle area feature

b. Stash Changes for Circle Area Feature:
- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

c. Create a New Branch for Rectangle Area Feature:
- Create a new branch named "feature/rectangle-area" to work on the rectangle area

d. Stash Changes for Rectangle Area Feature:
- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

e. Switch Back to Circle Area Branch:

- Switch back to the "feature/circle-area" branch to continue working on the circle area feature.

- Retrieve the stashed changes

- Complete the circle area feature implementation and save the changes.

f. Commit and Push Circle Area Feature:

g. Switch Back to Rectangle Area Branch:

- Switch back to the "feature/rectangle-area" branch to continue working on the rectangle area feature.

- Retrieve the stashed changes

- Complete the rectangle area feature implementation and save the changes. 

h. Commit and Push Rectangle Area Feature

i. Create Pull Requests:

- Create a pull request to the ‘dev’ branch.

j. Review and Merge

- Have another team member or reviewer review your pull requests. - After receiving approval, merge both pull requests into the main branch.
