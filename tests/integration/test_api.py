'''
Test application implementation package.
'''

from pathlib import Path

import pytest
from click.testing import CliRunner

from gitlab_changelog.cli import cli


@pytest.mark.parametrize(
    'expected_changelog_path',
    [
        Path(__file__).parent / 'changelogs' / 'CHANGELOG.md'
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
        expected_changelog = file.read()

    assert changelog == expected_changelog
