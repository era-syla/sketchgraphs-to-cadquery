import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01235, 0.00763).lineTo(0.0241, 0.00763).lineTo(0.0241, 0.01201).lineTo(0.01235, 0.01201).lineTo(0.01235, 0.00763).close()
solid=wp_sketch0.add(loop0).extrude(-0.007200817914109309)
