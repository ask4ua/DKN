Webapp Service In Kuber
===
### Intro

Prepare web application solution for one-shot deployment to kubernetes cluster.

### Assumptions

#### Web app

Use precompiled vovolkov/webapp:fix docker image.

1. Web app should always be deployed from the latest image version.
1. Web app should consists of no less then 2 instances after successfull redeployment. 
1. Web app should be redeployed keeping no less than 1 instance running during redeployment.
1. Web app instances should be distributed as much as possible between different cluster nodes.
1. ~~Web app should be able to get via kuber API how many instances of Webapp exist now based on count of pods with app:webapp label.~~
1. Web app should be available via URL: webapp.k8s.ask4ua.com and pathes (# - student number):
 * /student# -> webapp: /student#
 * /api/st# -> webapp: ~~/api~~/st#
 * /api/st#/wqesd -> webapp: ~~/api~~/st#/wqesd
 

#### DB

Use precompiled vovolkov/db docker image.

1. DB part of service should contain only 1 instance.
1. DB part should be redeployed in recreate mode.

#### Common Assumptions

1. Application should be secured enough using non-default image secrets.

### Output Format

As output should be provided 2 files:
 - 1 yaml manifest with all kuberenetes entitites desribed in one file splitted by "---" yaml file separator,
 - curl output log for calling webapp by URL.

