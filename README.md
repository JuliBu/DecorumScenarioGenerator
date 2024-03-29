# DecorumScenarioGen
## Repo is Work in progress!
- With this repository you can generate your own random scenarios for the boardgame "Decorum" in german and english.
- At the moment there are not that many different conditions possible, but I will try to let the collection of possible conditions grow.
## Start playing new scenarios
- In new_scenarios/pdfs, there are some examples of generated scenarios if you just want to play a new scenario.
- All scenarios use the back-side of the board where the players live in the two bedrooms.
- For playing it could be useful to print every sheet two times, s.t. each player receives one sheet for his own and can cut the second one in snippets to forward them to the other players after every 5 rounds.
- There is also one possible solution per scenario calculated and given in the pdfs folder.
## Functionality
If you want to create new scenarios, you need to pip-install `fpdf` for generating the pdf output, as well as `tqdm` for displaying a progress bar.
### Config
There are multiple parameters you can set within the config:
- SET_SEED: You can set a seed in the config to your favourite number
- NR_TRIES: How many tries you want to do in total (with the default parameters ~1% of the total tries results in a playable scenario)
- Most of the other parameters set the probability distribution of the different conditions 
### Run
If using PyCharm, after setting up the config you can just run the run.py and your generated scenarios should appear in new_scenarios/pdfs
Otherwise you need to specify some more things:

`cd <path-to-project-root> # Go into project's root directory`

`python -m venv .venv # Create a virtual environment in .venv`

`source .venv/bin/activate # Activate virtual environment for the current session`

`export PYTHONPATH=<path-to-project-root> # Add search path, s.t. import-statements work`

`cd commands # For now, since relative paths are used in code`
python run.py`

The activation of the virtual environment and the PYTHONPATH update must happen every time a new terminal session is started.

Only tested for Python 3.9.

## Feedback
I would be happy on every feedback, how your games were and what should be improved. Feel free to open an issue!
