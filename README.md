### **Simple db dictionary handler**

For work make easy **3** steps:
1) in cmd use in here directory: `pip install -r requirements.txt`
2) create db (default name is testms) and type sql command: 
`
CREATE TABLE 'main' (
  'id' int(11) NOT NULL,
  '_key' text NOT NULL,
  '_word' text NOT NULL
)
` 
3) run the command in cmd: `uvicorn app:app --reload`
