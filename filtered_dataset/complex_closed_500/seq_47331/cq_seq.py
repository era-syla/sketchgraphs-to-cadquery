import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0059, 0.0075).lineTo(0.0, 0.0075).lineTo(0.0, 0.0035).lineTo(-0.0019, 0.0035).lineTo(-0.0059, 0.0075).close()
solid=wp_sketch0.add(loop0).extrude(-0.009212349640011759)
