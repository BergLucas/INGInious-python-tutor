# INGInious-python-tutor

INGInious-python-tutor is a plugin for INGInious that adds [Python Tutor](https://pythontutor.com/) visualisation.

- **Downloads page:** https://github.com/BergLucas/INGInious-python-tutor/releases

## Requirements

The application requires:

- [Python](https://www.python.org/) ~= 3.9
- [pip](https://pip.pypa.io/en/stable/)

## Download & Installation

There are two ways to download and install the application:

### Using Git

You can install the application using Git by running the following command:

```bash
pip install git+https://github.com/BergLucas/INGInious-python-tutor.git
```

### Using the GitHub releases

You can download the application on the [downloads page](https://github.com/BergLucas/INGInious-python-tutor/releases). Then, you can install the application by running the following command:

```bash
pip install inginious_python_tutor-X.X.X-py3-none-any.whl
```

(Note: The X.X.X must be replaced by the version that you want to install.)

## Usage

Once installed, add the plugin to your INGInious configuration file:

```yaml
plugins:
-   plugin_module: inginious_python_tutor
```

You can then use the `python-tutor` directive in your task.
It works like `code-block` and renders an interactive [Python Tutor](https://pythontutor.com/) iframe.
All the options are settable and have default values:

```rst
.. python-tutor:: 311
    :width: 800
    :height: 500
    :frameborder: 0
    :code-div-height: 400
    :code-div-width: 350
    :cur-instr: 0

    print("Hello World!")
```

## License

All code is licensed for others under a MIT license (see [LICENSE](https://github.com/BergLucas/INGInious-python-tutor/blob/main/LICENSE)).
