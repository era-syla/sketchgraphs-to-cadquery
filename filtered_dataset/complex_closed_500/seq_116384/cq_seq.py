import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0125, -0.0).lineTo(0.0125, -0.0).lineTo(0.00814, 0.0175).lineTo(-0.00814, 0.0175).lineTo(-0.0125, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0694983174453739)
