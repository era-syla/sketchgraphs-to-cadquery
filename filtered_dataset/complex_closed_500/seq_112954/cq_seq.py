import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01316, 0.0025).lineTo(0.01316, 0.00723).lineTo(0.00396, 0.0025).lineTo(0.01316, 0.0025).close()
solid=wp_sketch0.add(loop0).extrude(0.011942522062185308)
