# OSINTframework
OSINTframework: Fully modular OSINT framework kit.

### Changelog 12/05/22
- Updated IntelX module to reflect recent changes implemented by Phonebook.cz and IntelX.io (Phonebook.cz was experiencing abuse of their api key). Module now requires you to have your own IntelX api key (they have a free option) as the tool no longer grabs an api key from Phonebook.cz. 
- Updated BreachDB module to use the new Breachinator endpoint, still requires api key.  
- Updated osfconsole to implement new IntelX module setting.

### Description  
The goal of this tool is to provide a fully modular framework dedicated to OSINT and related subjects.  

### Features  
- Randomly generated banner at launch.
- Familiar interface inspired by Metasploit.
- Tab auto-complete when navigating the console.
- Local command execution with `shell` prefix.
- Shortcuts (i.e. `options` = `show options`).
- Feedback when setting options (i.e. `set foo bar` = `FOO => bar`).
- Spaces supported when setting options.
- Module specific settings with persistent value storage (until you terminate osfconsole).

### Setup  
```bash
git clone https://github.com/jgarcia-r7/OSINTframework
pip3 install -r requirements.txt
chmod +x osfconsole.py
./osfconsole.py
```

### Basic Usage  
When you launch the osfconsole, you will be greeted with a Metasploit-isque interface. Typing `help` will list available commands:  
<img width="546" alt="image" src="https://user-images.githubusercontent.com/81575551/163649746-b71993f1-d976-49da-af68-71cd9683275a.png">

Typing `list` will list out the currently available modules:  
<img width="735" alt="image" src="https://user-images.githubusercontent.com/81575551/163649793-00697d7c-f059-4521-82e3-74552c84e32b.png">

Loading a module is as simple as typing `use <type/module>`. This will cause your prompt to update:  
<img width="611" alt="image" src="https://user-images.githubusercontent.com/81575551/163649877-ccb57594-752d-400e-956c-77a84e389cc2.png">

Typing `show options` or `options` will list out that module's specific options:  
<img width="715" alt="image" src="https://user-images.githubusercontent.com/81575551/163649930-a86e139b-468e-4815-8aa3-1c5944b734b6.png">

Typing `set <option> <value>` will adjust that option, you can use uppercase or lowercase:  
<img width="644" alt="image" src="https://user-images.githubusercontent.com/81575551/163649985-f9b01ad5-8ab0-4a45-8584-0bb7ada1977d.png">

Typing `show options` or `options` again will show the reflected values:  
<img width="685" alt="image" src="https://user-images.githubusercontent.com/81575551/163650045-da59ad83-44dd-4533-a862-1316a5ea0e45.png">

Typing `run` will run the current module with the specfied settings:  
<img width="654" alt="image" src="https://user-images.githubusercontent.com/81575551/163650085-98d5afcf-21e4-4d84-8d2c-8cb8cd95eb0f.png">
