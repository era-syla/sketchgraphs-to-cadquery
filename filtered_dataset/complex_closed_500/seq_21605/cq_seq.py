import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(2.74, -0.88).lineTo(2.66, -0.88).lineTo(2.66, -2.1).lineTo(2.74, -2.1).lineTo(2.74, -0.88).close()
solid=wp_sketch0.add(loop0).extrude(3.1905895214342865)
