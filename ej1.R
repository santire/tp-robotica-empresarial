library(tuneR)
library(seewave)

guitar <- readMP3("guitar.mp3")
rain <- readMP3("rain_short.mp3")
speak <- readMP3("speak.mp3")

# Ejercicio 1A.1
oscillo(guitar)
oscillo(rain)
oscillo(speak)

# Ejercicio 1A.2
oscillo(guitar, from = 1, to = 1.01)
oscillo(rain, from = 1, to = 1.005)
oscillo(speak, from = 1.004, to = 1.01)

# Ejercicio 1A.3
speak_b <- normalize(speak, unit = "16", level = 0.1)
oscillo(speak, from = 1.004, to = 1.01)
axis(side = 2, las = 2)
oscillo(speak_b, from = 1.004, to = 1.01)
axis(side = 2, las = 2)


# Ejercicio 2A.1
spec(guitar)
axis(side = 2, las = 2)

spec(rain)
axis(side = 2, las = 2)

spec(speak)
axis(side = 2, las = 2)

# Ejercicio 2A.3
spectro(guitar)
spectro(rain)
spectro(speak)

# Ejercicio 2A.4
guitar_pb <- ffilter(guitar, to = 1500, output = "Wave")
guitar_pb <- normalize(guitar_pb, unit = "16")
spectro(guitar_pb, flim = c(0, 5))

guitar_pa <- ffilter(guitar, from = 1500, output = "Wave")
guitar_pa <- normalize(guitar_pa, unit = "16")
spectro(guitar_pa, flim = c(0, 18))
