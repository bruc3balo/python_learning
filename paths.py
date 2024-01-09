from pathlib import Path

path = Path("emails")
exists = path.exists()
print()

#mkdir
if not exists:
    path.mkdir()

#rmdir
path.rmdir()


#Print files
project = Path()
project_files = project.glob("*.py")
for file in project_files:
    print(file.name)