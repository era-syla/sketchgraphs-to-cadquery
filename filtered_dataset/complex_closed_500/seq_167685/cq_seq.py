import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, -0.01588).lineTo(0.00635, -0.01588).lineTo(0.00635, 0.0).lineTo(0.0, 0.0).lineTo(0.0, -0.01588).close()
solid=wp_sketch0.add(loop0).extrude(0.02430031608900521)
