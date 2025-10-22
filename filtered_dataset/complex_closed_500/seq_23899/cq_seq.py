import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.285, 0.0).lineTo(0.285, 0.35).lineTo(-0.0, 0.35).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.11291243570794701)
