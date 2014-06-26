from mean_sightings import get_sightings

filename = 'sightings_tab_sm.csv'

def test_water_is_correct():
    waterrec,watermean = get_sightings(filename,'Water')
    assert waterrec==2, 'Number of records for water is wrong'
    assert watermean==17, 'Mean for water is wrong'

def test_clay_is_correct():
    clayrec,claymean = get_sightings(filename,'Clay')
    assert clayrec==2, 'Number of records for clay is wrong' 
    assert claymean==25.5, 'Mean for clay is wrong'

def test_not_present():
    norec,nomean = get_sightings(filename,'Not Present')
    assert norec==0, 'Biosignature not present has zero recs'
    assert nomean==0, 'Mean is not present for missing biosig'

