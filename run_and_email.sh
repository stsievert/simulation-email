#!/bin/bash

# to have the command line command `matlab` in your $PATH
# edit this for the proper R<YEAR><a,b>.app filename
export PATH="/Applications/MATLAB_R2013a.app/bin":$PATH

# run in either matlab or python. save the figure to
# /path/to/simulation-email/screenshot.png and comment out
# `show()`/`drawnow()`.

ipython $1
export MATLAB_BEG="run "
export MATLAB_END="; exit"
export MATLAB_COMMAND=$MATLAB_BEG$1$MATLAB_END
#matlab -nodisplay -nosplash -r "$MATLAB_COMMAND"
echo "Done with simulation"

# and email it. the username should be the first argument and the password the
# second. if I knew keys, I would use a key instead of plain text. I use quotes
# so you don't have to escape.
python email_w_attach.py "sieve121@umn.edu" "password"
echo "Done sending email"
