# UPN_bot
(1) Clone the project into your local directory.<br>
(2) Create a new virtual Python environment with python version 3.7.3 using command :<br>

```
virtualenv "new_env_name" -p pythonx.x.x
```
<br>
(3) Activate your new virtual environment.<br>

```
. "new_env_name"/bin/activate
```
<br>
(4) Install all required dependencies by going to root folder and run the command :<br>

```
pip install -r requirements.txt
```
<br>
(5) Install Spacy module with command: : <br>

```
python -m spacy download en
```
<br>
(6) To deploy application on local server go to root folder and run command:<br>

```
sh -x script.sh & sh -x bot.sh & sh -x main.sh & sh -x img.sh 
```
<br>
(7) Navigate to:  http://127.0.0.1:8000/ (Default hosting address)

## NOTE: In case you run the bot again, and it says that the port is already in use, then follow these steps on terminal:
 - sudo netstat -tlnp
 - Identify the row in column "Local Address" which contains that port number. Note the respective value from "PID/Program name" column.
 - sudo kill -9 <PID>

