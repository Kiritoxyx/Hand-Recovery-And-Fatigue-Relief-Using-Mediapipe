# Hand-Recovery-&-Fatigue-Relief-Using-Mediapipe
Innovation Project, Zhengzhou University, 11, 2023
> 🛠️ This project aims to relieve hand fatigue through gaming with hand gestures
## Requirements:
_Make sure your `python` version >= `3.7.0`_
```shell
pip install opencv-python
pip install mediapipe
pip install pygame
```
## How to run the game
### ChallengeMode:
```shell
cd ChallengeMode/
python main.py
```
### NormalMode:
```shell
cd NormalMode/
python main.py
```

💡: We code this project mainly using `IDEA`, so if you are encountering `import` errors like :
`could not find NormalMode.enmey` 

_you could delete the ~`NormalMode`~ like this:_
```python
import NormalMode.enemy
# If you are encountering import errors, change the previous line to the following:
import enemy
# should work perfectly
```
