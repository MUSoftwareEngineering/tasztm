# Augur Collab Role-play

## Brainstorm
- Software system that analyzes open-source software metrics
    - how well collab is working on project
    - health of project for investors and easing business/engineer communication
    -

### Requirements
- the metrics should be tracked and automated updates and notifications should be relayed to people working on the project
- Investors
    - Investors need a UI to see data visualized simply
- Developers
    - Devs would need access to a database to store metrics data
- Users
    - Users should be able to implement the API into any part of the system
    - Users want better visualizations of metrics
        - System needs multiple user endpoints (API) to access specific metrics for what is important to respective roles
    - Users need version control implemented to track timestamps of commits, issues, pull requests, etc.

- things to track
    - rate of commits
    - volume of commits
    - time between
    - amount of people working on branches
    - track code re-use

# Functional Requirements

- monitor commits/pulls/forks over time, average size of commits, etc
- monitor developer interaction (how much are people talking?)
- crawl through repository to get metrics
- sort projects by similarity to project success
- find and "rate" project similarity
- UI system to display metrics in different ways

# System Requirements

- massive database system
