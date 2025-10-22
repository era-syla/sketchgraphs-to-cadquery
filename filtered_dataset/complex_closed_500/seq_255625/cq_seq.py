import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.7, -0.7).lineTo(-0.7, -0.7).lineTo(-0.7, 0.7).lineTo(0.7, 0.7).lineTo(0.7, -0.7).close()
solid=wp_sketch0.add(loop0).extrude(2.112879139171579)
