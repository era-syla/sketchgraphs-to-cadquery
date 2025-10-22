import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.728, -0.307).lineTo(0.75, -0.329).lineTo(0.75, 0.0).lineTo(0.728, -0.022).lineTo(0.728, -0.307).close()
solid=wp_sketch0.add(loop0).extrude(-0.24599874581951583)
