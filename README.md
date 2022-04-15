# Sylvestris

Ionic React TS & ASP.NET Core + FastAPI tech stack project.

## Installation

> Every installation part will start from root folder.

### Client app - Ionic React TS

```
cd app
npm install
```

_If there is an error about not found **NPM** you can read NPM install guide at the Q&A part_

### Main Api - ASP.NET Core

```
cd api/main_service
dotnet restore
```

_If there is an error about not found **Dotnet** you can read Dotnet install guide at the Q&A part_

### Hum Api - FastAPI

```
cd api/hum_service
poetry shell
poetry install
```

_If there is an error about not found **Poetry** you can read Poetry install guide at the Q&A part_

## Run app in development

> Every run part will start from root folder.

### Client app - Ionic React TS

```
cd app
ionic serve
```

_If there is an error about not found **Ionic** you can read Ionic install guide at the Q&A part_

### Main Api - ASP.NET Core

```
cd api/main_service
dotnet watch run
```

### Hum Api - FastAPI

> Every time you re-open project in any IDE you need to run following command to re-create the virtual environment:

```
cd api/hum_service
poetry shell
```

-   Run development server:

```
cd api/hum_service
uvicorn hum_service.app:app --reload
```

## Q & A

-   Install NodeJS - NPM included

Read [this link](https://nodejs.org/en/download/) for further information to install NodeJS

-   Install Ionic CLI

> You must have NPM installed on your computer before install Ionic CLI.

Read [this link](https://ionicframework.com/docs/cli/install) for further information to install Ionic CLI

-   Install Poetry

Read [this link](https://python-poetry.org/docs/) for further information to install Poetry

-   Install Dotnet

Read [this link](https://dotnet.microsoft.com/en-us/download) for further information to install Dotnet

-   Install Docker

Read [this link](https://docs.docker.com/get-docker/) for further information to install Docker
