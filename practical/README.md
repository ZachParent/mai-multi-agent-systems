# Emergency Planner - MAI IMAS Practical 2024

## How to run

1. create a conda environment with python 3.12
```
conda create -n mas python=3.12
```

2. activate the environment
```
conda activate mas
```

3. install crewai 0.95.0    
```
pip install 'crewai[tools]==0.95.0'
```

4. install the dependencies
```
crewai install
```

5. run the flow
```
crewai flow kickoff
```

Note that the flow may sometimes fail to produce the outputs in the required pydantic format. You may rerun the flow until it succeeds.

The output will be saved in `data/outputs/emergency_report.md`.
