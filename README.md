# DecorumScenarioGen
## Repo is Work in progress!
- With this repository you can generate your own random scenarios for the boardgame "Decorum" in german and english.
- At the moment there are not that many different conditions possible, but I will try to let the collection of possible conditions grow.
## Start playing new scenarios
- In new_scenarios/pdfs, there are some examples of generated scenarios if you just want to play a new scenario.
- All scenarios use the back-side of the board where the players live in the two bedrooms.
- For playing it could be useful to print every sheet two times, s.t. each player receives one sheet for his own and can cut the second one in snippets to forward them to the other players after every 5 rounds.
## Functionality
If you want to create new scenarios, you need to pip-install `fpdf` for generating the pdf output, as well as `tqdm` for displaying a progress bar.
### Config
There are multiple parameters you can set within the config:
- SET_SEED: You can set a seed in the config to your favourite number
- NR_TRIES: How many tries you want to do in total (with the default parameters ~1% of the total tries results in a playable scenario)
- Most of the other parameters set the probability distribution of the different conditions 
### Run
After setting up the config you can just run the run.py and your generated scenarios should appear in new_scenarios/pdfs

## Feedback
I would be happy on every feedback, how your games were and what should be improved. Feel free to open an issue!