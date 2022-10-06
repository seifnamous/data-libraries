# Logging library

Logger wrapper to be used for console logging.

## Description

Common interface for console logging that can be extended to cover file logging.

## Getting Started

### Installing
* Library pushed to pypi: https://pypi.org/project/logpatent/
* To install:

```
pip install logpatent
```

### How to use
```
import logpatent.logger as lg
logger = lg.Logger(
            log_format='%(asctime)s::%(env)s::%(levelname)s::%(message)s',
            job_name='drugs_analyzer',
            env='dev',
            log_level='INFO',
)
logger.info('my message')
```

## Version History
* 0.1.0
    * Initial Release

