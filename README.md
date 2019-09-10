To install the requirements run "pip install -r requirements.txt". This only needs to be done once.

You will also need to create a file called "secrets.txt" and paste your access token in there. This can be found in
LastPass.

Once you have done this, open the currency_pairs.txt file and add each currency pair that you would like on a new line.
An example of a pair is "GBPUSD". 

Once you are happy with your list run 
`$ python tradermade.py`

The output file with the last year of FX rates for each pair will be inside the files folder. 

