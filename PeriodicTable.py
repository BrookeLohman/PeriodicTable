
electrons = {
  'O' : 6,
  'H' : 1,
  'C' : 4,
  'N' : 5,
  'F' : 7
}

def sortElectrons(electrons):
  s = sorted(electrons)
  for _ in s:
    print _, electrons[_]


sortElectrons(electrons)

  

