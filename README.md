# EECS217_VLSI

batch replace schematic symbol command:

procedure(replace_instance_in_schematic(oldLibName oldCellName newLibName newCellName)
  let((cv inst instMaster newInst newName uniqueSuffix)
    cv = geGetEditCellView()
    uniqueSuffix = 0 ; Initialize a suffix for creating unique names
    foreach(inst cv~>instances
      when(inst~>libName == oldLibName && inst~>cellName == oldCellName
        ; Get the master of the new instance
        instMaster = dbOpenCellViewByType(newLibName newCellName "symbol" "" "r")

        ; Generate a unique name for the new instance
        newName = sprintf(nil "%s_%d" inst~>name uniqueSuffix)
        uniqueSuffix = uniqueSuffix + 1

        ; Create a new instance with the same xy coordinates and orientation as the old one
        newInst = dbCreateInst(cv instMaster newName inst~>xy inst~>orient)

        ; Copy the properties from the old instance to the new one
        dbCopyProp(inst newInst)

        ; Delete the old instance
        dbDeleteObject(inst)
      )
    )
  )
)

; Call the procedure with the specific libraries and cell names
replace_instance_in_schematic("tsmcN65" "nch" "gpdk045" "nmos1v")
