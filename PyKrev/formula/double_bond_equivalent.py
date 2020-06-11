def double_bond_equivalent(count_list):
    
      
    """ 
	Docstring for function pyKrev.double_bond_equivalent
	====================
	This function takes a list of element counts and gives the double bond equivalent.
    
	Use
	----
	double_bond_equivalent(Y)
    
	Returns a list of len(Y) in which each item is the double bond equivalent.  
    
	Parameters
	----------
	Y: A list of dictionary items containing atomic counts as produced by element_counts.
    
	Info
	----------
    
	Double bond equivalent (DBE; UN; degree of unsaturation; PBoR [Pi Bonds or Rings]): 
	The number of molecules of H2 that would have to be added to a molecule to convert all pi bonds to single bonds, 
	and all rings to acyclic structures. 
	The DBE number can be calculated from the formula using the following equation:

	DBE = UN = PBoR = C - (H/2) + (N/2) +1,
	where: C = number of carbon atoms, H = number of hydrogen and halogen atoms, and N = number of nitrogen atoms.
    
    
    """    
    DBE_list = []
    
    for count in count_list:
        Halogens = ['H','Cl','Br','I','F','At','Ts']
        Hal = 0 
        for el in Halogens: 
            try:
                Hal += count[el]
            except KeyError:
                pass 
            
        DBE_counts = count['C'] - (Hal/2) + (count['N']/2) + 1 
        DBE_list.append(DBE_counts)
    
    return DBE_list 