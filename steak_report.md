How Americans like their steak
================
Peer Christensen
24/1/2017

Steak preparation preference by region
--------------------------------------

``` r
steak_reg=prop.table(table(steak_survey$region,steak_survey$steak_prep),1)
steak_reg=steak_reg[,order=c(5,4,3,2,1)]
par(mfrow=c(3,3),mar=c(3,3,3,3))
cols=brewer.pal(5,"OrRd")
for (i in seq(9)) {barplot(steak_reg[i,],main=dimnames(steak_reg)[[1]][i],col=cols)}
```

![](steak_report_files/figure-markdown_github/unnamed-chunk-2-1.png)

By gender
---------

``` r
steak_gen=prop.table(table(steak_survey$female,steak_survey$steak_prep),1)
steak_gen=steak_gen[,order=c(5,4,3,2,1)]
par(mfrow=c(1,2))
```

barplot(steak\_gen[2,],col=brewer.pal(5,"RdPu"),main="Women") barplot(steak\_gen[1,],col=brewer.pal(5,"Blues"),main="Men")

Smokers vs. non-smokers
-----------------------

``` r
steak_smoke=prop.table(table(steak_survey$smoke,steak_survey$steak_prep),1)
steak_smoke=steak_smoke[,order=c(5,4,3,2,1)]
par(mfrow=c(1,2))
barplot(steak_smoke[2,],col=brewer.pal(5,"Greys"),main="Smokers")
barplot(steak_smoke[1,],col=brewer.pal(5,"Greens"),main="Non-smokers")
```

![](steak_report_files/figure-markdown_github/unnamed-chunk-4-1.png) barplot(steak\_smoke[2,],col=brewer.pal(5,"Greys"),main="Smokers") barplot(steak\_smoke[1,],col=brewer.pal(5,"Greens"),main="Non-smokers")

Gamblers vs. non-gamblers
-------------------------

``` r
steak_gamble=prop.table(table(steak_survey$gamble,steak_survey$steak_prep),1)
steak_gamble=steak_gamble[,order=c(5,4,3,2,1)]
par(mfrow=c(1,2))
```

barplot(steak\_gamble[2,],col=brewer.pal(5,"Spectral"),main="Gamblers") barplot(steak\_gamble[1,],col=brewer.pal(5,"PiYG"),main="Non-gamblers")

Drinkers vs. non-drinkers
-------------------------

``` r
steak_alcohol=prop.table(table(steak_survey$alcohol,steak_survey$steak_prep),1)
steak_alcohol=steak_alcohol[,order=c(5,4,3,2,1)]
par(mfrow=c(1,2))
```

barplot(steak\_alcohol[2,],col=brewer.pal(5,"BuPu"),main="Drinkers") barplot(steak\_alcohol[1,],col=brewer.pal(5,"PuRd"),main="Non-drinkers")

By age
------

``` r
steak_age=prop.table(table(steak_survey$age,steak_survey$steak_prep),1)
steak_age=steak_age[,order=c(5,4,3,2,1)]
par(mfrow=c(1,4),mar=c(3,3,3,3))
cols=brewer.pal(5,"YlGn")
```

for (i in seq(4)) {barplot(steak\_age[i,],main=dimnames(steak\_age)[[1]][i],col=cols)}

By household income group
-------------------------

``` r
steak_hhold_income=prop.table(table(steak_survey$hhold_income,steak_survey$steak_prep),1)
steak_hhold_income=steak_hhold_income[,order=c(5,4,3,2,1)]
par(mfrow=c(1,5),mar=c(3,3,3,3))
cols=brewer.pal(5,"Reds")
```

for (i in seq(5)) {barplot(steak\_hhold\_income[i,],main=dimnames(steak\_hhold\_income)[[1]][i],col=cols)}

By level of education
---------------------

``` r
steak_educ=prop.table(table(steak_survey$educ,steak_survey$steak_prep),1)
steak_educ=steak_educ[,order=c(5,4,3,2,1)]
par(mfrow=c(1,4),mar=c(3,3,3,3))
cols=brewer.pal(5,"GnBu")
#drop less than High school level - only one respondent
```

for (i in seq(2,5)) {barplot(steak\_educ[i,],main=dimnames(steak\_educ)[[1]][i],col=cols)}

Separating smokers, gamblers and drinkers from the rest
-------------------------------------------------------

For this visualization, we create a new variable to distinguish people who enjoy smoking, gambling and drinking, from those who do not like fun. All respondents who do not fit into these categories are disregarded.

``` r
steak_survey$champs=with(steak_survey,
                         ifelse(gamble==T & smoke==T & alcohol==T,T,NA))
steak_survey$champs[steak_survey$gamble==F & 
                steak_survey$smoke==F & steak_survey$alcohol==F] = F
steak_champs=prop.table(table(steak_survey$champs,steak_survey$steak_prep),1)
steak_champs=steak_champs[,order=c(5,4,3,2,1)]
par(mfrow=c(1,2))
```

barplot(steak\_champs[2,],col=brewer.pal(5,"YlOrBr"),main="Champs") barplot(steak\_champs[1,],col=brewer.pal(5,"Purples"),main="Non-champs")
