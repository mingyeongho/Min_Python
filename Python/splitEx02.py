example = 'python,jquery,javascript'
print(example.split(','))

a,b,c = example.split(',')
print(a,b,c)

example = 'theteamlab.univ.edu'
subdomain, domain, tld = example.split('.')
print(subdomain, domain, tld)