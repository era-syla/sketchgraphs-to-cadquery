import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.9, 0.06).lineTo(0.85, 0.06).lineTo(0.85, 0.04).lineTo(0.9, 0.04).lineTo(0.9, 0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.11487321673585447)
