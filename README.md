# DriveHenrico

## Development Requirements
<details>
  <summary>docker</summary>

  Realistically, you really only need the docker cli. Docker makes development and production easier and more reproducible between environments.

  #### Usage
  ```bash
  docker compose up --build # Starts the project... but so does "just start"
  ```

  #### Installation
  ```bash
  sudo pacman -S extra/docker # On arch

  # Or
  sudo pacman -S yay && yay -S extra/docker
  ```
  > Im like 99% sure the bottom one will always work... not sure about the top one
</details>

<details>
  <summary>siblink</summary>

  A custom built python package linker to make our jobs just a little bit easier. Instead of running scripts with python, we'd use the siblink wrapper like so

  #### Usage
  ```bash
  siblink run main.py 
  ```

  #### Installation
  ```bash
  pip install siblink

  # Or

  pip install pipx && pipx install siblink # On linux machines this is best, especially arch
  ```

  To be honest, we probably won't have to ever directly work with siblink unless something catastrophic happens but siblink has some useful commands for managing the python environment so its a good to have.
</details>

<details>
  <summary>just</summary>

  Command runner... its just easier.

  #### Usage
  ```bash
  just start # That simple.... as long as you have docker installed
  ```

  #### Installation
  ```bash
  npm i -g rust-just
  ```
</details>


## Commands
Run `just -l` in the terminal to view them


## Configuration
Everything needed to know to configure different parts of this application. Most of it should be in `yaml` format but some of it *especially credentials* will be in a `.env` file. But other things that are only used in the backend will be in `yaml` format


### Yaml Config
This project requries a config.yaml file to be present. this file dictates most of the function of the backend so its crucial. Take from config.example.yml

### Routing Configurations
<details>
  <summary>Expand</summary>

  Routing configuration options

  #### Environment Variables
  <details>
   <summary>APP_DOMAIN</summary>
  
   Domain used throughout the application, mainly useful in development. recommended values include:
   - 127.0.0.1.nip.io
   - localdev.com *only if you setup dnsmasq and don't mind certain... issues*
   - actualdomain.xyz *for production only*
  </details>

</details>

&nbsp;

---

### Backend Configurations
<details>
  <summary>Expand</summary>

  Backend configuration options
</details>

&nbsp;

---

### Frontend Configuration
<details>
  <summary>Frontend</summary>

  Frontend configuration options
</details>

&nbsp;
