import cmath

# Read the input complex number as a string
z = input().strip()

# Convert the string to a complex number
c = complex(z)

# Compute the magnitude and phase using cmath.polar
magnitude, phase = cmath.polar(c)

# Print the results
print(magnitude)
print(phase)
