4.1 

git clone git@github.com:my-name/my-imaginary-repo.git
cd my-imaginary-repo
touch my_second_file.py
git add my_second_file.py
git commit -m "commiting the second python file"
git push

4.2

I developed on my VM, then pushed the code to Github, pulled it back down on the Pi using the display/mouse/keyboard that I have set up. It was terribly inefficient. Since I have a display, I shouldv'e just install 
Sublime on the rPi and worked exclusively through the GUI on the Pi. 

4.3

There is a constant delay, because inside the ultrasonicRead function (which is inside the GrovePi Python library) there is a delay of 200 ms. This delay exists for a good reason (actually two good reasons). The first of which is that the Raspberry Pi has to read and write through the I2C Protocol to communicate with the GrovePi, and thus with the Ultrasonic Ranger. We do not want to overload the I2C bus, which would be problematic. For that reason, the delay within the ultrasonicRead function exists. However, after nosing around on the GrovePi website, I found another reason why there exists a delay in the readings of the ultrasonic ranger, although this reason is relativley disassociated from the Pi and Python. In order to communicate that the ultrasonic ranger is sending a signal, it first spits out a frequency called a trigger signal for 10 micro seconds, which indicates that the ultrasonic sensor is about to start reading data. Now, I understand this is an unbelievably short time, but it still causes some marginal delay. I thought it was cool.