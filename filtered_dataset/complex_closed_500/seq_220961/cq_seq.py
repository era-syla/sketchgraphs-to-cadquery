import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00847, 0.01133).threePointArc((0.00674, 0.01244), (0.00486, 0.01329)).lineTo(0.00625, 0.01694).threePointArc((0.00868, 0.01583), (0.01092, 0.01437)).lineTo(0.00847, 0.01133).close()
solid=wp_sketch0.add(loop0).extrude(-0.017689157923526277)
