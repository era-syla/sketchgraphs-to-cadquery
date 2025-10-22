import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0051).lineTo(0.0, 0.007).lineTo(0.001, 0.007).lineTo(0.001, 0.019).lineTo(0.002, 0.019).lineTo(0.002, 0.015).lineTo(0.0256, 0.015).lineTo(0.0256, 0.019).lineTo(0.0266, 0.019).lineTo(0.0266, 0.007).lineTo(0.0276, 0.007).lineTo(0.0276, 0.0051).lineTo(0.0, 0.0051).close()
solid=wp_sketch0.add(loop0).extrude(0.07019943733234298)
