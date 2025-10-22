import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03204, 0.00569).lineTo(0.02295, 0.00569).lineTo(0.02295, 0.01066).lineTo(0.03204, 0.01066).lineTo(0.03204, 0.00569).close()
solid=wp_sketch0.add(loop0).extrude(-0.004855366717568776)
