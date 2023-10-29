## Description 
HolbertonBnB is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## Storage 🛄

The above classes are handled by the abstracted storage engine defined in the FileStorage

Every time the backend is initialized, HolbertonBnB instantiates an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instances are created, updated, or deleted, the `storage` object is used to register corresponding changes in the `file.json`.

## Console 💻

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the `storage` object defined above).

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$

```

Alternatively, to use the HolbertonBnB console in interactive mode, run the file `console.py` by itself:

```
$ ./console.py

```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 

```

To quit the console, enter the command `quit`, or input an EOF signal (`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$

```

```
$ ./console.py
(hbnb) EOF
$

```

## Testing 📏

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests

```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py

```

## Authors ✒️

-   **Nahuel Acosta** <[acostanahuel](https://github.com/acostanahuel)>
-   **Brian de Leon** <[Kiwizacxs](https://github.com/Kiwizacxs)>
