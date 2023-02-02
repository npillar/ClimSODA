import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import xarray as xr
import xarray.plot as xplt
import shapefile
from shapely.geometry.polygon import Polygon
from cartopy.feature import ShapelyFeature

# open the netCDF file
ds = xr.open_dataset('soda3.3.2_cl_uvw_reg_1980-2018.nc')
u = ds.u
v = ds.v
w = ds.w
lon = ds.xu_ocean - 360
lat = ds.yu_ocean
x,y = np.meshgrid(lon,lat)

uu = u[6,0,:,:].values
vv = v[6,0,:,:].values
ww = w[6,0,:,:].values

shpname = 'shapefile/BR_UF_2020/BR_UF_2020.shp'

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-50,-10,-30,10], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=.5)
hcb = ax.contourf(x,y,ww,cmap='viridis')
hst = ax.streamplot(x,y,uu,vv,color='w',arrowstyle='-',density=3,linewidth=0.5)
shape_feature = ShapelyFeature(Reader(shpname).geometries(),ccrs.PlateCarree(), edgecolor='black')
ax.add_feature(shape_feature, linestyle='-', alpha=.5, facecolor='w')
plt.show()


import matplotlib.patches
ax = plt.gca()
for art in ax.get_children():
    if not isinstance(art, matplotlib.patches.FancyArrowPatch):
        continue
    art.remove()        # Method 1
    # art.set_alpha(0)  # Method 2

plt.show()

