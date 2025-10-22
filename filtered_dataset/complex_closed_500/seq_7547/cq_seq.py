import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.075, 0.0).lineTo(-0.075, 0.091).lineTo(-0.055, 0.091).lineTo(-0.055, 0.061).lineTo(-0.05, 0.061).lineTo(-0.05, -0.0).lineTo(-0.075, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.21688320834736396)
