import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.74295, 0.381).lineTo(0.762, 0.381).lineTo(0.762, 0.4572).lineTo(0.74295, 0.4572).lineTo(0.74295, 0.381).close()
solid=wp_sketch0.add(loop0).extrude(0.06250138945915275)
