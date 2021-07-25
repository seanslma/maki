# xml

https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2

```python
import xml.etree.ElementTree as et

def parse_con(dir, file, duid): 
    """Parse the input XML file and store the result in a pandas 
    DataFrame with the given columns. 

    #<NEMSPDCaseFile>
    #    <NemSpdInputs>
    #        <RegionCollection>
    #        <TraderCollection>
    #        <InterconnectorCollection>
    #        <ConstraintScadaDataCollection>
    #        <GenericEquationCollection>
    #        <GenericConstraintCollection>
    """

    print(f'    {file}')
    tree = et.parse(os.path.join(dir,file))
    root = tree.getroot()

    pth1 = './NemSpdInputs/GenericConstraintCollection/GenericConstraint'
    pth2 = f'/LHSFactorCollection/TraderFactor[@TraderID="{duid}"]'

    #get periodending, UIGF_ATime="20201204104000"
    pe = root.find('NemSpdInputs').find('Case').attrib.get('UIGF_ATime')
    pe = pd.to_datetime(pe, format='%Y%m%d%H%M%S')

    #get generic constraint info
    rows = []
    cols = ['SettlementDate', 'ConstraintID','Version','EffectiveDate',
            'VersionNo','Type','ViolationPrice','RHS','Force_SCADA', f'LHS_{duid}']
    for gc in root.findall(f'{pth1}{pth2}/../..'):
        row = [pe] + [gc.attrib.get(col) for col in cols[1:-1]]
        lhs = gc.findall(f'.{pth2}')
        row.append(lhs[0].attrib.get('Factor'))
        rows.append(row)
    df = pd.DataFrame(rows, columns=cols)

    return df

def parse_sol(dir, file, duid): 
    """Parse the input XML file and store the result in a pandas 
    DataFrame with the given columns. 

    #<NEMSPDCaseFile>
    #    <NemSpdInputs>
    #        <RegionCollection>
    #        <TraderCollection>
    #        <InterconnectorCollection>
    #        <ConstraintScadaDataCollection>
    #        <GenericEquationCollection>
    #        <GenericConstraintCollection>
    """

    print(f'    {file}')
    tree = et.parse(os.path.join(dir,file))
    root = tree.getroot()

    pth3 = f'./NemSpdOutputs/TraderSolution[@TraderID="{duid}"]'

    #get gen solution info
    sol = root.find(pth3)
    srw = [sol.attrib.get(col) for col in scls]

    return srw
```