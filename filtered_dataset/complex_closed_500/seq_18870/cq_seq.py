import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.008, 0.006).lineTo(-0.014, 0.006).lineTo(-0.014, -0.006).lineTo(-0.008, -0.006).lineTo(-0.008, 0.006).close()
solid=wp_sketch0.add(loop0).extrude(0.011924282440058396)
