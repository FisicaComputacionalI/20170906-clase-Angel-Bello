import numpy as np
import matplotlib.pyplot as plt
x = [6000,7000,8000,9000,10000]
y = [73, 80, 85, 87, 89]
x2 =[6000,7000,8000,9000,10000]
y2 = [73, 80, 85, 87, 89]
plt.plot(x,y,'r--')
plt.plot(x2,y2,'ro')
x1 = [7000,8000,9000,10000,11000]
y1 = [80, 83, 85, 86, 88]
plt.plot(x1,y1,'bs')
plt.plot(x1,y1,'b--')
plt.title("RPCs")
plt.xlabel("Voltaje [V]")
plt.ylabel ("Eficiencia [%]")
plt.savefig ('clase6.png')
plt.show()
