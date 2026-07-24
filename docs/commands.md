# AI Home Lab Assistant Command Reference

## Python

### Create Virtual Environment
```powershell
py -m venv .venv
```

### Activate Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Requirements
```powershell
py -m pip install -r requirements.txt
```

### Run Application
```powershell
py src/main.py
```

---

## Git

### Status
```powershell
git status
```

### Add Files
```powershell
git add .
```

### Commit
```powershell
git commit -m "message"
```

### Push
```powershell
git push
```

---

## Google Cloud

### Current Project
```powershell
gcloud config get-value project
```

### List Projects
```powershell
gcloud projects list
```

### Switch Project
```powershell
gcloud config set project PROJECT_ID
```

### Application Default Login
```powershell
gcloud auth application-default login
```

### List Enabled APIs
```powershell
gcloud services list --enabled
```

### Enable Vertex AI
```powershell
gcloud services enable aiplatform.googleapis.com
```