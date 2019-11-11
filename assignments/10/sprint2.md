# For the Grader

What is this mess?
I'm trying to write out a way to install Augur in Windows. There's two approaches to setting this up: put everything on Windows and run the commands in the Linux Subsystem, or put everything in the Linux subsystem and run the commands there as well. The first approach is right below this and the second is below the "redesign" title. Hopefully this all makes some sort of sense.

# Augur Windows Installation

https://github.com/chaoss/augur/issues/403

### PostgreSQL Setup

Install [PostgreSQL](https://www.postgresql.org/download/windows/) for Windows. Make sure to get phpMyAdmin!

### Npm Setup

Grab Npm AND Node at the [same time](https://nodejs.org/en/download/)!

In the installer, make sure that you're intalling npm and node. Also make sure that "add to PATH" is selected again. Otherwise you'll have to do this manually too.

![node install](./node1.png)

You will be prompted to install other tools, which is optional.

### Vue Setup

Install [Vue](https://vuejs.org/) and [Vue CLI](https://cli.vuejs.org/) by running the commands below.

```
npm install -g vue
npm install -g @vue/cli
```

### GitBash Setup

Use [GitBash](https://gitforwindows.org/) to run the git commands necessary to clone the Augur repo. Of course this can also be done with any Windows git tool like GitHub Desktop.

If you do end up using GitBash, you have to use "Shift+Insert" to paste rather than Ctrl+C. You're welcome.

### Make Setup

#### GnuMake and Linux Subsystem

GnuMake - Install from [here](http://gnuwin32.sourceforge.net/install.html). Select the package that says "Complete package, except sources". Make note of where it installs the program. Now add the make program to PATH in environment variables.

You will also need to enable bash in Windows. Navigate to control panel and find "Turn Windows features on or off". Now enable Windows Subsystem for Linux. (You may need to restart your machine after doing this).

![linux](./windowsbash.png)

After restarting, test the bash command in a new command window. You may get an error that looks like this:

![bashError](./bashError.png)

Sometimes this fixes itself after a while.

## Running Augur

First, create the virtual environment. In your home directory (C:\Users\<Yourname>) or somewhere similar, run the following:

```
mkvirtualenv Augur_env
```

To exit the environment, simply type "deactivate". To start it, you can run
```
Envs\Augur_env\Scripts\activate
```
This will need to be done from where you created the environment. If you named your environment something else, replace "Augur_env" with that.

Now you'll need to exit the environment and clone the [Augur](https://github.com/chaoss/augur) repository somewhere.

# REDESIGN

## Enable Linux Subsystem

First, you will need to enable bash in Windows. Navigate to control panel and find "Turn Windows features on or off". Now enable Windows Subsystem for Linux. (You may need to restart your machine after doing this).

![linux](./windowsbash.png)

Before you can use the subsystem in the command line, you'll need to install a Linux distro in the Microsoft store as well. I'll be using [Ubuntu](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab) for this example.

![ubuntu](./ubuntu.png)

Now that you have the subsystem enabled, and a distro to use, you can launch the subsystem using the "wls" command.

## Install Dependencies

In the command prompt, use wls to launch the linux subsystem. Now you'll want to run the following commands to get the dependencies necessary to install augur.

```

```

## PostgreSQL Setup

Install [PostgreSQL](https://www.postgresql.org/download/windows/) for Windows. Make sure to get phpMyAdmin!

Link to the assignment with the database creation: https://github.com/computationalmystic/sengfs19/blob/master/lecture-labs/rw2-lab.md

## Getting Augur

Still need to test whether this should be installed on the windows side or the linux side.
Clone Augur from the repository.

If done in windows, change .sh files to unix line endings

## Installation

Congratulations, you now have everything you need to install and run Augur. Let's hope this works!
First we'll get the virtual environment running:

Launch the subsystem with wsl, and then cd to a directory you'll remember (like your Windows home directory).
