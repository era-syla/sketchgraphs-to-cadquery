import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.53481, -2.4).lineTo(0.58481, -2.4).lineTo(0.58481, -2.35).lineTo(0.53481, -2.4).close()
solid=wp_sketch0.add(loop0).extrude(0.048060220761623994)
