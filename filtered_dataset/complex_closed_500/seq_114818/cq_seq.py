import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.005, 0.102).lineTo(0.007, 0.102).lineTo(0.007, 0.077).lineTo(0.005, 0.077).lineTo(0.005, 0.102).close()
solid=wp_sketch0.add(loop0).extrude(-0.007609072912526836)
