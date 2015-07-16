from refractiveIndex import *

catalog = RefractiveIndex("../RefractiveIndex")
mat = catalog.getMaterial('other', 'pmma_resists', 'Microchem495')
print(mat.getRefractiveIndex(500))
#f = open('Hass.yml')
#a = yaml.safe_load(f)
#f.close()
#print(a)

#print(mat.getExtincionCoefficient(500))


#
# Iterate the shit out of the catalog
#
i = 0
for sh in catalog.catalog:
    for b in sh['books']:
        if not 'divider' in b:
            for p in b['pages']:
                try:
                    mat = catalog.getMaterial(sh['SHELF'], b['BOOK'], p['PAGE'])
                    a = mat.getRefractiveIndex((mat.refractiveIndex.rangeMin + mat.refractiveIndex.rangeMax)*1000.0/2)
                    #b = mat.getExtinctionCoefficient((mat.extinctionCoefficient.rangeMin + mat.extinctionCoefficient.rangeMax)*1000.0/2)
                except (FormulaNotImplemented):
                    pass
                except (NoExtinctionCoefficient):
                    pass
                except (Exception, NotImplementedError) as inst:
                    print("caugth exception in {}".format(p['path']))
                    print(inst)
                    i += 1
                    pass

print('Caught {} exceptions while parsing catalog'.format(i))