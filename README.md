# CompoundNameNormer
## Build
From commandline:  
`docker build -t compound-normer`

## Run
### Default list
From commandline:  
`docker run compound-normer`

Expected output:

|   | org_form | normed_form |
|---| --- | --- |
| 0 | Adenosine | ADENOSINE |
| 1 | Adenocard | ADENOSINE |
| 2 | BG8967 | BIVALIRUDIN |
| 3 | Bivalirudin | BIVALIRUDIN |
| 4 | BAYT006267 | FLUCONAZOLE |
| 5 | diflucan | FLUCONAZOLE |
| 6 | ibrutinib | IBRUTINIB |
| 7 | PC-32765 | IBRUTINIB | 

### Custom list:
Update contents of [`COMPOUND_LIST`](main.py), then from commandline:  
`docker run compound-normer`