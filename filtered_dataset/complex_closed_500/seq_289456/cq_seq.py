import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.015, 0.045).lineTo(0.06, 0.045).lineTo(0.06, 0.06).lineTo(0.015, 0.06).lineTo(0.015, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.09205886494566647)
