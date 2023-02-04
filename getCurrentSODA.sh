
for year in {1980..2016} ; do
    wget -r --no-parent -A 'soda3.12.2_5dy_ocean_reg_'$year'*' https://dsrs.atmos.umd.edu/DATA/soda3.12.2/REGRIDED/ocean/
    for f in 'dsrs.atmos.umd.edu/DATA/soda3.12.2/REGRIDED/ocean/soda3.12.2_5dy_ocean_reg_'$year'*' ; do
        suffix=$(echo $f | cut -d '_' -f 5-7)
        cdo select,name=u,v $f soda3.12.2_uv_$suffix
    done
done
