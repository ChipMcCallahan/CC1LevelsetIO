# CC1LevelsetIO
Reader, Writer, and Importer for CC1 DAT and CCX files. Converts to CC1LevelsetProto format.

Try the [Colab notebook](https://github.com/ChipMcCallahan/CC1LevelsetIO/blob/main/cc1_levelset_io.ipynb) to get started.

Or, use these code snippets.

```
!pip install git+https://github.com/ChipMcCallahan/CC1LevelsetIO.git
```

```python
from cc1_levelset_io.cc1_levelset_reader import CC1LevelsetReader
from cc1_levelset_io.cc1_levelset_writer import CC1LevelsetWriter


reader = CC1LevelsetReader()

cclp3 = reader.import_and_read("CCLP3.dat")
print(f"Found {len(cclp3.levels)} levels in {cclp3.name}")
print(f"Found {len(cclp3.stories)} story elements in {cclp3.name}")
po100t = reader.import_and_read("ajmiam-pit-of-100-tiles-v1008.dat")
print(f"Found {len(po100t.levels)} levels in {po100t.name}")
print(f"Found {len(po100t.stories)} story elements in {po100t.name}")
```

```
Successfully retrieved https://bitbusters.club/gliderbot/sets/cc1/CCLP3.dat.
Successfully retrieved https://storage.googleapis.com/file-hosting-abcdef/chips/CCLP3.ccx
Found 149 levels in Chip's Challenge Level Pack 3
Found 24 story elements in Chip's Challenge Level Pack 3
Successfully retrieved https://bitbusters.club/gliderbot/sets/cc1/ajmiam-pit-of-100-tiles-v1008.dat.
Found 100 levels in ajmiam-pit-of-100-tiles-v1008.dat
Found 0 story elements in ajmiam-pit-of-100-tiles-v1008.dat
```

```python3
writer = CC1LevelsetWriter()

# get the DAT format in bytes
dat = writer.write(cclp3)
with open("CCLP3.dat", "wb") as f:
    f.write(dat)

# write the DAT directly to disk
writer.write(po100t, filename="po100t.dat")
```
