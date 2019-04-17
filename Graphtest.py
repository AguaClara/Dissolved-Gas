from aguaclara.play import*
from matplotlib import style
style.use('ggplot')

x, y = np.loadtxt('Test.txt', unpack=True, delimiter=' ')

plt.plot(x, y)
plt.title('Volume of Water on Chain at \nDifferent Flow Rates')
plt.xlabel('Flow Rate (mL/s)')
plt.ylabel('Volume of Water on Chain (mL)')
plt.savefig('/Users/sbernaber/desktop')
plt.show()
