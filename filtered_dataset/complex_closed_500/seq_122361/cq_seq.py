import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.2, 0.2).lineTo(0.192, 0.2).lineTo(0.192, 0.1).lineTo(0.2, 0.1).lineTo(0.2, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(-0.056675901219643256)
