import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0885, 0.1265).lineTo(0.0885, 0.1265).lineTo(0.0885, 0.0115).lineTo(-0.0885, 0.0115).lineTo(-0.0885, 0.1265).close()
solid=wp_sketch0.add(loop0).extrude(-0.46616642421914073)
