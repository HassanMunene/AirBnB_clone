# AirBnB Clone Project

Welcome to the AirBnB clone project!

## Overview

This project is the first step towards building a full web application: The AirBnB clone. The initial focus is on creating a command interpreter to manage AirBnB objects. The features and structure developed in this project will be used in subsequent projects involving HTML/CSS templating, database storage, API integration, front-end integration, and more.

## Table of Contents

- [Features](#features)
- [Command Interpreter](#command-interpreter)
- [Classes](#classes)
- [Storage Engine](#storage-engine)
- [Unit Tests](#unit-tests)
- [Usage](#usage)
- [Installation](#installation)
- [Contributing](#contributing)


## Features

This project includes the following features:

- A parent class (`BaseModel`) to handle initialization, serialization, and deserialization of instances.
- A serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File.
- Several classes (`User`, `State`, `City`, `Place`) that inherit from `BaseModel`.
- An abstracted storage engine: File storage.
- Unit tests to validate all classes and the storage engine.

## Command Interpreter

The command interpreter is similar to a Shell but customised to managing objects specific to this project. It provides the following functionalities:

- **Create**: Create a new object (e.g., a new `User` or a new `Place`).
- **Retrieve**: Retrieve an object from a file, database, etc.
- **Operations**: Perform operations on objects (e.g., count, compute stats).
- **Update**: Update attributes of an object.
- **Destroy**: Destroy an object.

## Classes

The project includes the following classes:

- **BaseModel**: The parent class that handles initialization, serialization, and deserialization.
- **User**: Inherits from `BaseModel`.
- **State**: Inherits from `BaseModel`.
- **City**: Inherits from `BaseModel`.
- **Place**: Inherits from `BaseModel`.

## Storage Engine

The storage engine is responsible for abstracting file storage. It includes functionalities to:

- Serialize instances to JSON strings and save them to a file.
- Deserialize JSON strings from a file to instances.

## Unit Tests

Unit tests are created for all classes and the storage engine to ensure the correctness and reliability of the project components.

## Usage

To use the command interpreter, run the following command:

```sh
./console.py

