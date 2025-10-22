import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1397, -0.00635).lineTo(-0.1397, -0.00635).lineTo(-0.1397, 0.00635).lineTo(0.1397, 0.00635).lineTo(0.1397, -0.00635).close()
solid=wp_sketch0.add(loop0).extrude(0.5053922713849304)
