'''
Test application implementation package.
'''

from datetime import datetime
from pathlib import Path

import pytest
from click.testing import CliRunner
from jinja2 import Template

from gitlab_changelog_tool.cli import cli


@pytest.mark.parametrize(
    'expected_changelog_path',
    [
        Path(__file__).parent / 'templates' / 'CHANGELOG.md'
    ]
)
def test_generate_should_return_valid_changelog_content(
    expected_changelog_path: Path
):  # pylint: disable=C0301
    '''
    Test generating changelog content.

    Parameters:
        expected_changelog_path (Path): Expected changelog path.
    '''

    runner = CliRunner()
    result = runner.invoke(cli, ['generate'])

    changelog = result.output

    with open(expected_changelog_path, mode='r', encoding='utf-8') as file:
        source = file.read()

    expected_changelog = Template(
        source,
        keep_trailing_newline=True
    ).render(
        tag_timestamp=datetime.utcnow()
    )

    assert changelog == expected_changelog
