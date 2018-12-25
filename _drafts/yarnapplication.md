---
layout: post
title: Writing YARN Applications
---
# Yarn

The general concept is that an *application submission client* submits an *application* to the YARN ResourceManager (RM). This can be done through setting up a YarnClient object. After YarnClient is started, the client can then set up application context, prepare the very first container of the application that contains the ApplicationMaster (AM), and then submit the application. You need to provide information such as the details about the local files/jars that need to be available for your application to run, the actual command that needs to be executed (with the necessary command line arguments), any OS environment settings (optional), etc. Effectively, you need to describe the Unix process(es) that needs to be launched for your ApplicationMaster.

