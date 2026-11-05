from unittest import mock

from pyas2 import settings
from pyas2.utils import _run_command


@mock.patch("pyas2.utils.subprocess.run")
def test_post_processing_command_does_not_invoke_a_shell(mock_run):
    mock_run.return_value.returncode = 0
    malicious_filename = "payload; touch /tmp/should-not-exist"

    _run_command(
        'processor "$filename"',
        {"filename": malicious_filename},
    )

    mock_run.assert_called_once_with(
        ["processor", malicious_filename],
        check=False,
        timeout=settings.COMMAND_TIMEOUT,
    )


@mock.patch("pyas2.utils.subprocess.run")
def test_invalid_post_processing_command_is_not_executed(mock_run):
    _run_command('processor "unterminated', {})

    mock_run.assert_not_called()
