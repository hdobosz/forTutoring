1. clone repository
```
git clone https://github.com/Ayshyama/forTutoring
```
2. check remote
```
git remote -v
```
3. if remote is not Ayshyama/forTutoring, then add remote
```
git remote add origin https://github.com/Ayshyama/forTutoring.git
```

4. If you want to have the same repository inside your Git account, you can fork it.

- When you fork a project, you essentially create a copy of the original (upstream) repository under your own GitHub account. 
- This gives you full control over your forked repository, and you can push updates to it as you wish. 

### Here's how you can manage where to push your updates:

### Two Remote Repositories

- Origin: This is your forked repository. When you clone your fork to your local machine, 
- Git automatically names this remote "origin".

- Upstream: This is the original repository that you forked. 
- Generally, you would add this as a second remote named "upstream" to pull in changes from the original project.
Steps to Add Upstream and Decide Where to Push
Clone Your Fork: If you haven't already, clone your forked repository to your local machine.

bash
Copy code
git clone https://github.com/your_username/forked_repository.git
Check Current Remotes: You can view the current remotes to see where the code will be pushed or pulled from.

bash
Copy code
git remote -v
This will typically show "origin" pointing to your forked repository.

Add Upstream Remote: Navigate to your local repository directory and add the original repository as an "upstream" remote.

bash
Copy code
git remote add upstream https://github.com/original_owner/original_repository.git
Decide Where to Push: Now you have two remotes: "origin" and "upstream".

Push to your fork: git push origin <branch_name>
You generally can't push to upstream unless you are an authorized contributor.
Fetch and Merge Changes from Upstream: Before pushing new changes, it's often good to fetch and merge changes from the "upstream" repository so that your fork stays up-to-date.

bash
Copy code
git fetch upstream
git merge upstream/main
or in one command:

bash
Copy code
git pull upstream main
Push to Your Fork: After resolving any conflicts and committing your changes, you can push to your fork.

bash
Copy code
git push origin <branch_name>
By managing your remotes this way, you can decide whether to push your updates to your fork ("origin") or create a pull request to contribute changes back to the original project ("upstream"). Most often, you'll be pushing to your own fork and then creating a pull request to propose changes to the upstream project.

