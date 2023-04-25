from pathlib import Path

path = Path(r"hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
