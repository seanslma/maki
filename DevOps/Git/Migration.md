# Migration
Here is the summry of migrating repos from github to azure devops.

## Do not do it
- Using `git clone` instead of `--mirror`: will lose tags, refs, or hidden branches
- Adding files to the Azure repo before push:causes conflicts and diverging history
- Email mismatch: Commits still exist, but user linking in ADO may not auto‑resolve; Fix via user email mapping in Azure DevOps

## Best‑practice: Git mirror migration
- Preserves commit history
- Preserves authors, timestamps, commit SHAs
- Preserves branches, tags, and refs
- git blame works exactly as before
- No vendor lock‑in tooling required
- Works for GitHub Enterprise Server and Cloud

### Create an empty repo in Azure DevOps
- Project -> Repos -> New repository
- Do not add README, .gitignore, or license

### Clone the GitHub repo as a mirror
```sh
git clone --mirror https://github.enterprise.example.com/org/repo.git
cd repo
```

### Push the mirror to Azure DevOps
```sh
git remote set-url --push origin https://dev.azure.com/org/project/_git/repo
git push --mirror
```

### What not preserved
- Pull Requests: Need migration tool
- PR comments & reviews: Need migration tool
- Issues: Need migration tool
- Wiki: Separate repo
- GitHub Actions: Must be rewritten as Azure Pipelines
- Repo permissions: Must be recreated
