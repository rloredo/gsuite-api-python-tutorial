Overview
https://developers.google.com/workspace/guides/getstarted-overview

Create a project and enable the API
https://developers.google.com/workspace/guides/create-project#create_a_new_google_cloud_platform_gcp_project

Enable a Google Workspace API
https://developers.google.com/workspace/guides/create-project#enable-api
Repeat the process and enable all gsuite apis:
 -Drive
 -Sheets
 -Docs
 -Slides
 -Calendar


 Create service credentials for servers and windowless apps
 https://developers.google.com/workspace/guides/create-credentials#createsvc
 https://developers.google.com/workspace/guides/create-credentials#obtain_service_account_credentials

You'll need to give access to all the resources you want to use to the email of the service account. For example, share the calendar with that email if you want to use the calendar functions. Also, give access to a drive folder or to a sheets if you want to use it with the api. 




