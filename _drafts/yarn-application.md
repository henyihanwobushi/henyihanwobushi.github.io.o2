---
layout: post
title: yarn-application
---

构建Yarn应用

# 目的

本文是为了尝试搭建一个Yarn服务，尝试一下*Yarn*服务开发。

# 概念和流程

简单来讲，就是应用提交程序提交应用到*Yarn*服务的 *Resource Manager*

## Yarn Client

This can be done through setting up a *YarnClient* object. After *YarnClient* is started, the client can then set up *application context*, prepare the very first *container* of the application that contains the *ApplicationMaster* (AM), and then submit the application.

You need to provide information such as:

* the details about the local files/jars that need to be available for your application to run
* the actual command that needs to be executed (with the necessary command line arguments)
* any OS environment settings (optional)
* etc.

Effectively, you need to describe the Unix process(es) that needs to be launched for your ApplicationMaster.

## Resource Manager

The YARN *ResourceManager* will then launch the *ApplicationMaster* (as specified) on an *allocated container*.

The *ApplicationMaster* communicates with YARN cluster, and handles application execution. It performs operations in an asynchronous fashion. During application launch time, the main tasks of the ApplicationMaster are:

* communicating with the ResourceManager to negotiate and allocate resources for future containers, and
* after container allocation, communicating YARN *NodeManager*s (NMs) to launch application containers on them.

Task a) can be performed asynchronously through an *AMRMClientAsync* object, with event handling methods specified in a *AMRMClientAsync.CallbackHandler* type of event handler. The event handler needs to be set to the client explicitly.

Task b) can be performed by launching a runnable object that then launches containers when there are containers allocated. As part of launching this container, the AM has to specify the ContainerLaunchContext that has the launch information such as command line specification, environment, etc.

## Execution

During the execution of an application, the *ApplicationMaster* communicates NodeManagers through *NMClientAsync* object. All container events are handled by *NMClientAsync.CallbackHandler*, associated with *NMClientAsync*. A typical *callback handler* handles client start, stop, status update and error. ApplicationMaster also reports *execution progress* to *ResourceManager* by handling the *getProgress()* method of *AMRMClientAsync.CallbackHandler*.

# Interface

Following are important Interfaces:

    * Client <--> ResourceManageer: by using YarnClient objects
    * ApplicationMaster <--> ResourceManager: by using AMRMClientAsync objects, handling events asynchronously by AMRMClientAsync.CallbackHandler.
    * ApplicationMaster <--> NodeManager: Launch containers. Communicate with NodeManagers by using NMClientAsync objects, handling container events by NMClientAsync.CallbackHandler.

----
Node
    * The three main protocols for YARN application:
        1. ApplicationClientProtocol
        2. ApplicationMasterProtocol
        3. ContainerManagementProtocol
    are still preserved. The 3 clients wrap these 3 protocols to provide simpler programming model for YARN applications.

    * Under very rare circumstances, programmer may want to directly use the 3 protocols to implement an application. However, note that such behaviors are *no longer encouraged* for general use cases.

# Writing a Simple Yarn Application
