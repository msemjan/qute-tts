# Text-To-Speech User Script for Qutebrowser

This is a simple script that adds a text-to-speech to Qutebrowser using a [user script](https://qutebrowser.org/doc/userscripts.html).

## Install

**1. Install dependencies**

You need Python 3, and Google Text To Speech [Python library](https://gtts.readthedocs.io/en/latest/index.html#) which can be easily installed using PIP:
```
pip install gTTS
```

You also need some program that can play audio. I use `mpv`, so you may need to change `AUDIO_PLAYER` variable, if you want to use something else.

**2. Clone this repo**

```
git clone https://github.com/msemjan/qute-tts.git
```

**3. Copy the user script**

Then copy the `gTTS.py` file to the folder with user scripts:
```
cp qute-tts.py $HOME/.local/share/qutebrowser/userscripts/
```

Make the script executable with:
```
chmod u+x $HOME/.local/share/qutebrowser/userscripts/qute-tts.py
```

If you haven't created this directory, you need to create it before running the command above:
```
mkdir $HOME/.local/share/qutebrowser/userscripts
```

**4. Run the script**

The script will read whatever text is currently selected by the user. To run it, simply use the following command:
```
:spawn --userscript qute-tts.py
```

**5. (Optional) Create a keyboard shortcut**

It is a little bit cumbersome to have to type the command every time you want to run it, so I recommend to bind this script to a keyboard shortcut.

Open the configuration file with `:config-edit` command, and add the following code at the end of the file:
```python
config.bind('xt', 'spawn --userscript qute-tts.py')
```

After saving the file, you should be able to run the script by clicking `xt` in normal mode. 

## Limitations

At the moment, the script will speak only English (UK). You can modify the script to speak a different local ['accent'](https://gtts.readthedocs.io/en/latest/module.html#localized-accents), if you want to. Just follow the link, and find the "Top-level domain" for the language you are interested in. Then change `tld` variable in the Python code. 

The second important note is that this script uses Google's API, so you need to be connected to the internet. You should also be comfortable with the fact that Google will know what you are doing online.
