For RV-Predict and Jlint
1. Download the [benchmark](https://github.com/buptsseGJ/ComRaDe/tree/master/benchmark-suite) and copy it to the dataset folder. Structure should look like below
```
Jbench
\__dataset
         \__benchmark-suite
                            \__account
                            \__airlinetickets
                            \__...
```
2. Set environment variable
```
export jbench="/your/directory/softwaretesting/JBench"
```
3. Under the /scripts folder, run 
```
./evaluate.sh
```
It will automatically run the tool and generate a result.txt file.