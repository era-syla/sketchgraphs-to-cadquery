import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.029).lineTo(-0.07, 0.029).lineTo(-0.07, -0.024).lineTo(0.0, -0.024).lineTo(0.0, 0.029).close()
solid=wp_sketch0.add(loop0).extrude(0.2010760704801185)
