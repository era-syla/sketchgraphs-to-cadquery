import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0015, 0.0295).lineTo(-0.0015, 0.0295).lineTo(-0.0015, 0.0325).lineTo(0.0015, 0.0325).lineTo(0.0015, 0.0295).close()
solid=wp_sketch0.add(loop0).extrude(-0.0072311960523574245)
