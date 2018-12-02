for i in range(4000,4130):
    string = '''<Part id="'''+str(i)+'''" partType="Detacher-2" position="-3.814697E-07,12.4301,36.54868" rotation="90,0,0" drag="0,0,0,0,0,0" materials="8" scale="0.12,0.12,0.1216" massScale="0.008">
      <Detacher.State enabled="True" group="0" detachForce="50000" detacherUiMaxForce="50000" />
    </Part>
    <Part id="'''+str(i+1)+'''" partType="Bomb-2" position="-3.814697E-07,12.4301,36.94862" rotation="0,0,0" drag="0,0,0,0,0,0" materials="0,1,3" disableAircraftCollisions="true" scale="0.36,0.36,0.3648" massScale="0.216000021">
      <Bomb.State activationGroup="0" firingDelay="0.5"/>
      <CameraVantage.State viewMode="None" autoOrient="true" lookAtCockpit="false" autoZoomOnCockpit="false" autoCenterCamera="false" />
    </Part>'''
    print(string)
