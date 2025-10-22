import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(4.1004, 0.0).lineTo(2.5004, 0.0).lineTo(2.5004, 1.15).lineTo(4.1004, 1.15).lineTo(4.1004, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(4.074304114375971)
