# Augur Windows Installation

https://github.com/chaoss/augur/issues/403

## Dependencies

### Python and Virtualenv Setup

Begin by going to the [Python](https://www.python.org/downloads/windows/) website and installing the latest version.

Select the install now option (or at least make sure pip gets installed too).

Make sure "add Python to PATH" is selected. Otherwise you will need to do this manually through environment variables.

![install](./python1.png)

Now you should be able to run Python from the command line using the command "py".

Now run "pip install virtualenv" to get virtualenv.

### PostgreSQL Setup

Install [PostgreSQL](https://www.postgresql.org/download/windows/) for Windows. Make sure to get phpMyAdmin!

### Npm Setup

Grab Npm AND Node at the [same time](https://nodejs.org/en/download/)!

In the installer, make sure that you're intalling npm and node. Also make sure that "add to PATH" is selected again. Otherwise you'll have to do this manually too.

![node install](./node1.png)

You will be prompted to install other tools, which is optional.

### Vue Setup

Install [Vue](https://vuejs.org/) and [Vue CLI](https://cli.vuejs.org/) by running the commands below.

npm install -g vue

npm install -g @vue/cli

### GitBash Setup

Use [GitBash](https://gitforwindows.org/) to run the git commands necessary to clone the Augur repo. Of course this can also be done with any Windows git tool like GitHub Desktop.

### Make Setup

There's two ways to run the Augur installation. This can be done via NMAKE, the Windows equivalent to make, or through a program like GnuMake. We'll go over how to do both of these. NMAKE comes with Visual Studio which is convenient.

## Running Augur

First, create the virtual environment.
