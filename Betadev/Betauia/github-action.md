# Github actions

There is currently one github action. Whenever it detects a commit to the `gatsby` branch,
it builds the website and pushes the static content to the gh-pages branch. The file can be found in `.github/workflows/main.yml` on the `gatsby` branch.

It looks like this:

```
name: gh-pages-deploy

on:
  push:
    branches: [ gatsby ]
    
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
      
    - name: Install and build
      run: |
        npm install
        npm run build
    
    - name: Deploy
      uses: JamesIves/github-pages-deploy-action@releases/v3
      with:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        BRANCH: gh-pages
        FOLDER: public
```

Documentation for the `Deploy` command can be found [here](https://github.com/marketplace/actions/deploy-to-github-pages). Specific to our configuration is the `BRANCH` setting, which determines which branch to push the built website to, and the `FOLDER` option, which determines which folder the static files are stored in after building.