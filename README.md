<h1 align='center'>YAToDB. Yet another Truth or Dare Discord bot, made in Python and PyCord.</h1>

![LICENSE](https://img.shields.io/github/license/PyBotDevs/YAToDB)
![Stars](https://img.shields.io/github/stars/PyBotDevs/YAToDB)
[![Discord](https://img.shields.io/discord/880409977074888714?color=%235865F2&label=Discord&logo=discord&logoColor=%23FFFFFF)](https://discord.gg/b5pz8T6Yjr)

YAToDB is a simple and easy-to-use truth or dare Discord bot, developed in Python with the PyCord API wrapper library. **If you want to use this bot in your server, invite it [here.](https://discord.com/api/oauth2/authorize?client_id=1103327777467420723&permissions=274877908992&scope=bot%20applications.commands)** 

### Command List
* **/truth**: Gives a truth based question.
* **/dare**: Gives a dare based question.
* **/suggest**: Suggest a new question for truth or dare game modes.

## How to run
<ol>
<li>
  Go to your bot folder in your file manager. Go to the <code>config</code> folder and open the <code>startup.json</code> file.
  
  Now go ahead and insert your Discord bot token in the `token` part of the file. If you don't have one, go to <b>https://discord.com/developers</b> and make a new application.
  
  ![Screenshot_20230506_231226](https://user-images.githubusercontent.com/72265661/236639057-c4eace3d-d422-4e6e-b5d4-0e9190945521.png)
  
  After pasting the token, copy your Discord user ID and paste it into the `owner_id` part of the file. Save the file to apply changes.
</li>

<li>Open your terminal emulator (command prompt in Windows, terminal in Linux and MacOS). <b>Do not open as administrator as elevated permissions are not required.</b></li>
<br>
<li>Move to the directory in which the bot source is located. For example, if my bot folder is located in my Desktop folder, this should be run:

Windows:
```bat
cd C:\Users\{your username}\Desktop\YAToDB-main
```

Linux/MacOS:
```bash
cd ~/Desktop/YAToDB-main
```
</li>
<br>
<li>Type in the following command to start the bot.

```bash
python main.py
```

If `poetry` is installed on your machine, the `py-cord` library will be automatically installed, along with all of its dependencies. If not, run these two commands:

```bash
python -m pip install py-cord
python main.py
```
</li>
<br>
<li>If you see this in your terminal emulator,

```
[client] Bot client successfully signed into API. (startup time)
```

That means you're all set!</li>
</ol>
