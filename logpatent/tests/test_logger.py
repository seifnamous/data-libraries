"""logger unit testing.
"""

import logpatent.logger as lg


def test_logging(caplog) -> None:
    logger = lg.Logger(
        log_format='%(asctime)s::%(env)s::%(levelname)s::%(message)s',
        job_name='drugs_analyzer',
        env='dev',
        log_level='INFO',
    )
    logger.info('my message')
    assert 'my message' in caplog.text
