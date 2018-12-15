# coding: utf-8

import logging

import os

import subprocess

from django.core.exceptions import ImproperlyConfigured

from django.core.management.base import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    help = "Compile coffee files."

    def handle(self, **options):
        input_dir = getattr(
            settings,
            'COFFEEMACHINE_INPUT',
            None
        )
        output_dir = getattr(
            settings,
            'COFFEEMACHINE_OUTPUT',
            None
        )

        if not (input_dir or output_dir):
            raise ImproperlyConfigured(
                'Please specify COFFEEMACHINE_INPUT '
                'and COFFEEMACHINE_OUTPUT '
                'in your settings file!'
            )

        coffee_executable = getattr(
            settings,
            'COFFEEMACHINE_EXECUTABLE',
            'coffee'
        )

        cmd_line = [
            '--compile',
            '--output', output_dir,
            input_dir
        ]

        logging.info(subprocess.list2cmdline(cmd_line))
        os.execvp(coffee_executable, cmd_line)
