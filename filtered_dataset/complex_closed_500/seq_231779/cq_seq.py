import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0115, 0.0).lineTo(0.0115, 0.0).lineTo(0.00545, 0.02426).lineTo(-0.00545, 0.02426).lineTo(-0.0115, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.06949073610087843)
