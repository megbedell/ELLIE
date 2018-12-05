import matplotlib.pyplot as plt
from eleanor.source import Source
from eleanor.targetdata import TargetData
from eleanor.visualize import Visualize


star = Source(tic=261136901)  # this is a binary of two bright stars separated by ~2 pixels
data = TargetData(star)
vis = Visualize(data)
vis.mark_gaia_sources()



star = Source(tic=261136246)  # this is a binary of two bright stars separated by 186 arcsec.
# The brighter star is not the target star
data = TargetData(star, height=15, width=15)
vis = Visualize(data)
vis.mark_gaia_sources()  # this shows the tpf, right?


# Multiple Sectors
star = Source(tic=25155310, sector=[1,2])
data0 = TargetData(star[0])
data1 = TargetData(star[1])
plt.plot(data0.time, data0.corr_flux, 'k')
plt.plot(data1.time, data1.corr_flux, 'r')
plt.show()

# Only gets one sector
star = Source(tic=25155310, sector=1)
data = TargetData(star)
plt.plot(data0.time, data0.corr_flux, 'k')
plt.plot(data.time , data.corr_flux , 'g')
plt.show()

# Gets for all sectors available
star = Source(tic=25155310, sector='all')
print(star[0].sector, star[1].sector)

# Gets for most recent sector observed
star = Source(tic=25155310, sector='recent')
data = TargetData(star)
plt.plot(data1.time, data1.corr_flux, 'k')
plt.plot(data.time , data.corr_flux , 'r')
plt.show()