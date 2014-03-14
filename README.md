
Ever go out to lunch and are running a simulation back in the lab? Want to see
if it's finished? With this tool, you can do just that. You get an image of
the finished simulation in your inbox!

To use, there are several steps.

1. Comment out `drawnow()` or `show()`. This hangs the script to run the
   simulation.
2. Instead use `saveas(h, '/path/to/simulation-email/simulation.png)` or
   `saveas('../../simulation.png)`
3. Run the simulation with `bash /path/to/simulation/test.py`. 
   You'll be emailed the final photo when done.

To send the email, there has to be some initialization for your
password/username. Edit the username and password arguments in the
`run_and_email.sh` file; they're plaintext. If I knew how to do keys, I would use
keys.

This script can run Python or Matlab scripts; comment out the appropriate lines
in `run_and_email.sh`. 

Some further small notes:
* instead of using `~`, I had to use `/Users/scott/`
* this script is dependent on having `MATLAB_R2013b.app`. If you have something
  else, change that line in `run_and_email.sh`.
