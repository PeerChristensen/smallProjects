# Turning plots into sound with audiolyzR demo

install.packages("audiolyzR")
library(audiolyzR)

#random plot
a=runif(100)
b=runif(100)
df=data.frame
plot(df)
audioScatter("a","b",data=df) #Note the  ""

#negative correlation
a2=seq_len(100)
b2=seq(-1,-100)
df2=data.frame(a2,b2)
plot(df2)
audioScatter("a2","b2",data=df2)

#Average Monthly Temperatures at Nottingham, 1920-1939
b3=seq_len(length(nottem))
df3=data.frame(b3,nottem)
plot(df3,type="l")
audioScatter("b3","nottem",data=df3)




 