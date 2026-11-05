# -*- coding: utf-8 -*-
import logging
import os
import shlex
import subprocess
from string import Template

from pyas2 import settings

logger = logging.getLogger("pyas2")


def _run_command(command, variables):
    """Run a configured command without invoking a shell."""
    try:
        arguments = [
            Template(argument).safe_substitute(variables)
            for argument in shlex.split(command)
        ]
    except ValueError:
        logger.exception("Invalid AS2 post-processing command.")
        return

    if not arguments:
        return

    try:
        result = subprocess.run(
            arguments,
            check=False,
            timeout=settings.COMMAND_TIMEOUT,
        )
    except (OSError, subprocess.TimeoutExpired):
        logger.exception("Failed to execute AS2 post-processing command.")
        return

    if result.returncode:
        logger.error(
            "AS2 post-processing command exited with status %s.",
            result.returncode,
        )


def run_post_send(message):
    """Execute command after successful send, can be used to notify
    successful sends"""

    command = message.partner.cmd_send
    if command:
        logger.debug(f"Execute post successful send command {command}")
        variables = {
            "filename": os.path.basename(message.payload.name),
            "sender": message.organization.as2_name,
            "receiver": message.partner.as2_name,
            "messageid": message.message_id,
        }
        variables.update(message.as2message.headers)

        _run_command(command, variables)


def run_post_receive(message, full_filename):
    """Execute command after successful receive, can be used to call the
    edi program for further processing"""

    command = message.partner.cmd_receive
    if command:
        logger.debug(f"Execute post successful receive command {command}")

        variables = {
            "filename": os.path.basename(full_filename),
            "fullfilename": full_filename,
            "sender": message.partner.as2_name,
            "receiver": message.organization.as2_name,
            "messageid": message.message_id,
        }
        variables.update(message.as2message.headers)

        _run_command(command, variables)
