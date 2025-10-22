import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02, 0.00883).lineTo(-0.0, -0.02117).lineTo(0.02, 0.00883).lineTo(-0.02, 0.00883).close()
solid=wp_sketch0.add(loop0).extrude(-0.031366970246913)
