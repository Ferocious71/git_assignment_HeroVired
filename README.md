# git_assignment_HeroVired

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