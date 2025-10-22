import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01491, 0.00427).lineTo(-0.01867, 0.00427).lineTo(-0.01867, 0.0075).threePointArc((-0.01816, 0.00938), (-0.01679, 0.01075)).threePointArc((-0.01541, 0.00938), (-0.01491, 0.0075)).lineTo(-0.01491, 0.00427).close()
solid=wp_sketch0.add(loop0).extrude(-0.009223292051392148)
