# Setting up the environment

### Requirements

The command lines below are for OS.X, and nly given as reference, please refer to the specific documentation for details

1. Python: Preferably 3.12 or higher

    ```
    $ python --version
    Python 3.12.2
    ```

2. A package manager, either `pip` or [`uv`](https://astral.sh/blog/uv)

    ```
    # To install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

3. Some version of Jupyter notebook. At this moment, I'm using `vscode` with the `Jupyter` pluggin


### Installing

1. Clone this repository
    ```
    git clone https://github.com/pcingola/building_applications_with_llms.git
    ```

2. Create a Python virtual environment called `.venv` (notice the dot at the begining)

    ```
    # Create a virtual environment called '.venv' inside the project's directory
    cd building_applications_with_llms
    uv venv .venv
    ```

3. Install dependencies
    ```
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```

4. When running the Jupyter Notebook, make sure you use the `.venv` environment you've created



