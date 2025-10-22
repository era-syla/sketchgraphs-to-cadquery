import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0076, 0.0044).lineTo(-0.0076, 0.0128).lineTo(0.0026, 0.0128).lineTo(0.0026, 0.0044).lineTo(0.0006, 0.0044).lineTo(0.0006, 0.0108).lineTo(-0.0056, 0.0108).lineTo(-0.0056, 0.0044).lineTo(-0.0076, 0.0044).close()
solid=wp_sketch0.add(loop0).extrude(-0.013401884058715037)
