**A Simple Licel TR controller python module**

**python_requires>=3.6**

usage:  


`python -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  

*Activate the virtual environment then locate the
package and run*

`pip install licel-controller-0.0.1.tar.gz`

*create a file exaḿple.py with the following content*

```
import licel_controller.settings
from licel_controller.interface import Controller

# override settings
licel_controller.settings.HOST = "localhost"
licel_controller.settings.PORT = 2055

if __name__ == '__main__':
    c = Controller()
    c.select(2, 3, 5)
    c.pmtgain(2, 980)
    c.mstart()
    c.mstop()
    c.run()
```

*run*

`python example.py`


** To test the package run: **

`pytest --pyargs licel_controller`
