import numpy as np
import matplotlib        as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import xarray.plot as xplt
import shapefile
from cartopy.io.shapereader import Reader
from shapely.geometry.polygon import Polygon
from cartopy.feature import ShapelyFeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

# colormap
upper = mpl.cm.jet(np.arange(256))
lower = np.ones((int(256/4),4))
for i in range(3):
  lower[:,i] = np.linspace(1, upper[0,i], lower.shape[0])
cmap = np.vstack(( lower, upper ))
cmap = mpl.colors.ListedColormap(cmap, name='myColorMap', N=cmap.shape[0])
clev = np.arange(0,1.1,0.1)

# open the netCDF file
ds = xr.open_dataset('soda3.3.2_cl_uvw_reg_1980-2018.nc')
u = ds.u
v = ds.v
w = ds.w
lon = ds.xu_ocean - 360
lat = ds.yu_ocean
x,y = np.meshgrid(lon,lat)

shpname = 'shapefile/BR_UF_2020/BR_UF_2020.shp'

uu = u[6,0,:,:].values
vv = v[6,0,:,:].values
ww = w[6,0,:,:].values

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-50,-10,-30,10], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=.5)
shape_feature = ShapelyFeature(Reader(shpname).geometries(),ccrs.PlateCarree(), edgecolor='black')
ax.add_feature(shape_feature, linestyle='-', alpha=.5, facecolor='w')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlines = False
gl.ylines = False
gl.xlocator = mticker.FixedLocator([-45,-35,-25,-15])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax.set_title('JULY')

#hst = ax.streamplot(x,y,uu,vv,color=ww,cmap=cmap,arrowstyle='wedge',density=3,linewidth=1)
#cbar = fig.colorbar(hst.lines)

hcb = ax.contourf(x,y,ww,levels=clev,cmap=cmap,extend='both')
hst = ax.streamplot(x,y,uu,vv,color='k',arrowstyle='wedge',density=3,linewidth=0.5)
cbar = fig.colorbar(hcb)

cbar.ax.set_ylabel('Current Velocity [m/s]')
plt.savefig('soda_clim_jul.tif',dpi=300,bbox_inches='tight')
plt.show()

uu = u[10,0,:,:].values
vv = v[10,0,:,:].values
ww = w[10,0,:,:].values

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
ax.set_extent([-50,-10,-30,10], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=.5)
shape_feature = ShapelyFeature(Reader(shpname).geometries(),ccrs.PlateCarree(), edgecolor='black')
ax.add_feature(shape_feature, linestyle='-', alpha=.5, facecolor='w')
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlines = False
gl.ylines = False
gl.xlocator = mticker.FixedLocator([-45,-35,-25,-15])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
ax.set_title('NOVEMBER')

#hst = ax.streamplot(x,y,uu,vv,color=ww,cmap=cmap,arrowstyle='wedge',density=3,linewidth=1)
#cbar = fig.colorbar(hst.lines)

hcb = ax.contourf(x,y,ww,levels=clev,cmap=cmap,extend='both')
hst = ax.streamplot(x,y,uu,vv,color='k',arrowstyle='wedge',density=3,linewidth=0.5)
cbar = fig.colorbar(hcb)

cbar.ax.set_ylabel('Current Velocity [m/s]')
plt.savefig('soda_clim_nov.tif',dpi=300,bbox_inches='tight')
plt.show()
