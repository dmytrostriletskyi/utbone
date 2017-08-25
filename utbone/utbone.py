"""
`utbone` package functionality.
"""
import os
import shutil
import sys

import cli.app


def get_bone_filename(name, topping):
    """
    Return file name with extension by bone name and number of `topping` flag.
    """
    bones = {
        'django0': 'django.py',
        'django1': 'django-toppings.py',
        'unittest0': 'unit.py',
        'unittest1': 'unit-toppings.py',
    }

    return bones[name + str(topping)]


@cli.app.CommandLineApp
def utbone(app):
    """
    Create test template by path to locate, test file name, bone name and optional `topping` flag.

    Explanations:
        - there is two types of templates: simple bone, bone with `mock` and `ddt` package inside.
        - flag `--topping` (or just `-t`) control which type of template need to be generated.
          Topping means additional `mock` and `ddt` packages initial.

    How it works:
        - Get particular template from `bones` directory.
        - Create python file with the same name to specified path (usually to tests folder in projects).
        - Copy template content to created file.
        - Rename new file with content (that was copied) to specified file name.
    """
    try:
        path, file_name, bone, topping = app.params.path, app.params.test_file_name, app.params.bone, app.params.topping
        bone_filename = get_bone_filename(bone, topping)

        srcfile = os.path.dirname(os.path.realpath(__file__)) + '/bones/' + bone_filename
        dstroot = os.getcwd() + '/' + path

        bone_to_copy = dstroot + '/' + bone_filename
        test_file_name = dstroot + '/' + file_name + '.py'

        with open(bone_to_copy, 'w+'):
            shutil.copy(srcfile, dstroot)
            os.rename(bone_to_copy, test_file_name)

    except Exception:  # pylint: disable=broad-except
        # RuntimeError
        print(
            'You are doing it wrong. Type `utbone --help` to see guide how to use this tool.'
        )  # pylint: disable=superfluous-parens
        sys.exit(0)


utbone.add_param('path')
utbone.add_param('test_file_name')
utbone.add_param('bone')
utbone.add_param(
    '-t',
    '--topping',
    help='Add mock and ddt packages imports for testing template',
    default=0,
    action="count"
)

utbone.run()
